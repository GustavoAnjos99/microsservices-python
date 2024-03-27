const baseURL = "http://localhost:5500"

const btnlogin = document.getElementById('btnlogin')
const btnpedido = document.getElementById('btnpedido')
const btnproduto = document.getElementById('btnproduto')
const btncarrinho = document.getElementById('btncarrinho')

function listaritens(btn, rota){
    btn.addEventListener('click', function(){
        fetch(rota)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao listar itens');
            }
            return response.json();
        })
        .then(json => {
            var data = JSON.stringify(json)
            const item = document.createElement('p');
            item.textContent = `${data}`;
            document.getElementById('lista').innerHTML = '';
            document.getElementById('lista').appendChild(item);
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    })
}



listaritens(btnlogin, "http://localhost:8001/login")
listaritens(btnproduto, "http://localhost:8002/produtos")
listaritens(btnpedido, "http://localhost:8004/pedido")
listaritens(btncarrinho, "http://localhost:8003/carrinho")
