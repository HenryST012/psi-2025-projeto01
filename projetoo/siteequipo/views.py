from django.shortcuts import render

def index(request):
    contexto = {
        'titulo': 'Seleção Brasileira de Futebol',
        'descricao': 'A Seleção Brasileira é a mais vitoriosa da história da Copa do Mundo.',
        'imagem_url': 'images/selecaocomp.jpeg'
    }
    return render(request, 'siteequipo/index.html', contexto)

def elenco(request):
    jogadores = [
        {'nome': 'Alisson Becker', 'idade': 31, 'posicao': 'Goleiro', 'nascimento': 'Novo Hamburgo', 'foto': 'images/alisson.webp'},
        {'nome': 'Marquinhos', 'idade': 29, 'posicao': 'Zagueiro', 'nascimento': 'São Paulo', 'foto': 'images/marquinhos.webp'},
        {'nome': 'Beraldo', 'idade': 20, 'posicao': 'Zagueiro', 'nascimento': 'Piracicaba - SP', 'foto': 'images/beraldo.jpg'},
        {'nome': 'Danilo', 'idade': 33, 'posicao': 'Lateral', 'nascimento': 'Bicas', 'foto': 'images/danilo.webp'},
        {'nome': 'Alex Sandro', 'idade': 33, 'posicao': 'Lateral', 'nascimento': 'Catanduva', 'foto': 'images/alexsandro.webp'},
        {'nome': 'Casemiro', 'idade': 32, 'posicao': 'Volante', 'nascimento': 'São José dos Campos', 'foto': 'images/casemiro.webp'},
        {'nome': 'Antony', 'idade': 24, 'posicao': 'Ponta Direita', 'nascimento': 'Osasco - SP', 'foto': 'images/antony.webp'},        
        {'nome': 'Neymar Jr.', 'idade': 32, 'posicao': 'Atacante', 'nascimento': 'Mogi das Cruzes', 'foto': 'images/neymar.webp'},
        {'nome': 'Raphinha', 'idade': 27, 'posicao': 'Ponta Direita', 'nascimento': 'Porto Alegre - RS', 'foto': 'images/raphinha.webp'},
        {'nome': 'Vinícius Jr.', 'idade': 24, 'posicao': 'Atacante', 'nascimento': 'São Gonçalo', 'foto': 'images/vini.webp'},
        {'nome': 'Rodrygo', 'idade': 23, 'posicao': 'Atacante', 'nascimento': 'Osasco', 'foto': 'images/rodrygo.jpg'}
    ]
    return render(request, 'siteequipo/elenco.html', {'jogadores': jogadores})

def sobre(request):
    info = {
        'autores': ['Thierry Henry'],
        'descricao': 'Este site é um projeto Django para divulgar a Seleção Brasileira.',
        'instituicao': 'IFRN'
    }
    return render(request, 'siteequipo/sobre.html', {'info': info})
