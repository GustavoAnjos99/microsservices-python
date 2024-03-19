from fastapi import FastAPI, HTTPException
from write_read import leitura, escrita

app = FastAPI()
logintxt = "arquivos_textos/login.txt"

@app.post("/login/{username}/{password}")
async def login(username: str, password: str):
    if username == "user" and password == "password":
        logins = {"id": 1, "username": username, "password": password}
        escrita(logintxt, logins)
        return {"status": "sucesso", "mensagem": "Usuário autenticado"}
    
    raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
@app.get("/login")
async def listarLogins():
    return leitura(logintxt)
