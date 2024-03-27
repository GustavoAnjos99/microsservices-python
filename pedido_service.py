from fastapi import FastAPI, HTTPException
from write_read import leitura, escrita
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins="http://localhost:5500",
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

pedidostxt = "arquivos_textos/pedido.txt"
teste_login = leitura("login.txt")

@app.post("/pedido/{user_id}/add")
async def criar_pedido(user_id: int):
   if int(user_id) == teste_login.get("id"):
      pedidos = {"user_id": user_id, "order_id": 123}
      escrita(pedidostxt, pedidos)
      return {"status": "sucesso", "mensagem": "Pedido criado", "order_id": 123}
   
   raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.get("/pedido")
async def listarPedidos():
   return leitura(pedidostxt)
