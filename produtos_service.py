from fastapi import FastAPI
from write_read import leitura, escrita

app = FastAPI()

produtostxt = "arquivos_textos/produto.txt"
todos_produtos = {}
produtos = []

@app.post("/produtos/{nome}/{preco}")
async def criarProduto(nome: str, preco: float):
    
    produtos_temp = {"id": len(produtos) + 1, "nome": nome, "preco": preco}
    produtos.append(produtos_temp)
    todos_produtos = {"produtos": produtos}
    
    escrita(produtostxt, todos_produtos)
    return{"status": "produto criado!", "descricao": produtos_temp}


@app.get("/produtos")
async def listar_produtos():
    return leitura(produtostxt) 
