# 1º passo
python -m venv fastapi_env

# 2º passo
Windows: fastapi_env\Scripts\activate
macOS/Linux: source fastapi_env/bin/activate

# 3º passo
pip install fastapi uvicorn
pip install httpx

# 4º passo
pip freeze > requirements.txt                            <br>
uvicorn login_service:app --reload --port 8001           <br>
uvicorn produtos_service:app --reload --port 8002        <br>
uvicorn carrinho_service:app --reload --port 8003        <br>
uvicorn pedido_service:app --reload --port 8004          <br>


# 5º (instalar em outro local) passo 1 e passo 2 
pip install -r requirements.txt
