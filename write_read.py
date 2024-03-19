import json

def leitura(arquivo):
    try:
        with open(arquivo, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def escrita(arquivo, data):
    with open(arquivo, "w") as file:
        json.dump(data, file)