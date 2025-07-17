from django.shortcuts import render

def index(request):
    contexto = {
        'titulo': 'Seleção Brasileira de Futebol',
        'descricao': 'A Seleção Brasileira é a mais vitoriosa da história da Copa do Mundo.',
        'imagem_url': 'https://upload.wikimedia.org/wikipedia/commons/8/82/Brazil_national_football_team_2022.jpg'
    }
    return render(request, 'siteequipo/index.html', contexto)

def elenco(request):
    jogadores = [
        {'nome': 'Alisson Becker', 'idade': 31, 'posicao': 'Goleiro', 'nascimento': 'Novo Hamburgo', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Marquinhos', 'idade': 29, 'posicao': 'Zagueiro', 'nascimento': 'São Paulo', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Thiago Silva', 'idade': 39, 'posicao': 'Zagueiro', 'nascimento': 'Rio de Janeiro', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Danilo', 'idade': 33, 'posicao': 'Lateral', 'nascimento': 'Bicas', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Alex Sandro', 'idade': 33, 'posicao': 'Lateral', 'nascimento': 'Catanduva', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Casemiro', 'idade': 32, 'posicao': 'Volante', 'nascimento': 'São José dos Campos', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Paquetá', 'idade': 26, 'posicao': 'Meia', 'nascimento': 'Rio de Janeiro', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Neymar Jr.', 'idade': 32, 'posicao': 'Atacante', 'nascimento': 'Mogi das Cruzes', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Richarlison', 'idade': 27, 'posicao': 'Atacante', 'nascimento': 'Nova Venécia', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Vinícius Jr.', 'idade': 24, 'posicao': 'Atacante', 'nascimento': 'São Gonçalo', 'foto': 'https://via.placeholder.com/100'},
        {'nome': 'Rodrygo', 'idade': 23, 'posicao': 'Atacante', 'nascimento': 'Osasco', 'foto': 'https://via.placeholder.com/100'}
    ]
    return render(request, 'siteequipo/elenco.html', {'jogadores': jogadores})

def sobre(request):
    info = {
        'autores': ['Thierry Henry'],
        'descricao': 'Este site é um projeto Django para divulgar a Seleção Brasileira.',
        'instituicao': 'IFRN'
    }
    return render(request, 'siteequipo/sobre.html', {'info': info})
