from fastapi import FastAPI
from write_read import escrita, leitura

app = FastAPI()
produtostxt = "arquivos_textos/produto.txt"
logintxt = "arquivos_textos/login.txt"
carrinhotxt = "arquivos_textos/carrinho.txt"
leituraProdutos = leitura(produtostxt)
leituraLogin = leitura(logintxt)
cart = {}

@app.post("/carrinho/{user_id}/{produto_id}/{quantidade}/add")
async def add_carrinho(user_id: int, produto_id: int, quantidade: int):
    produto_encontrado = None
    for produto in leituraProdutos.get("produtos", []):
        if produto["id"] == produto_id:
            produto_encontrado = produto
            break

    if int(user_id) != int(leituraLogin.get("id")):
        return {"status": "ERRO", "mesagem": "usuário nao encontrado!"}
    elif produto_encontrado == None:
        return {"status": "ERRO", "mesagem": "produto nao encontrado!"}
     
    if user_id not in cart:
        cart[user_id] = []
        
    carrinho_atual = {"produto_id": produto_id, "quantidade": quantidade}
    cart[user_id].append(carrinho_atual)
    escrita(carrinhotxt, cart)
    return {"status": "sucesso", "mensagem": "Produto adicionado ao carrinho"}

@app.get("/carrinho")
async def listarCarrinho():
    return leitura(carrinhotxt)