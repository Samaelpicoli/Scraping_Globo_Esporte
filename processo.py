import requests
import bs4
import json
from datetime import datetime

def requisicao_noticias(meu_time):
    #solicitando as noticias sobre seu time no globo esporte
    try: 
        meu_time = meu_time.lower()

        url = f'https://ge.globo.com/futebol/times/{meu_time}/'

        #fazendo a requisição 

        noticias = requests.get(url)

        return noticias

    except Exception as error:
        print(f'Erro durante a requisição dos dados: {error}')
        raise Exception('Erro durante a requisição dos dados.')

def extraindo_dados(noticias):
    try:
        #ao instanciar o bs4, passo o texto da requisição e 
        #html.parser que diz qual o tipo do conteúdo que esta dentro, 
        #parser é porque ele vai decodificar esse texto no formato html

        pagina = bs4.BeautifulSoup(noticias.text, "html.parser")

        #pegar os elementos "a" que tenham a classe "feed-post-link"
        #no find_all do bs4, primeiro passo o elemento que quero e depois o seletor
        #nesse caso a classe

        lista_noticias = pagina.find_all('a', class_="feed-post-link")

        #agora que já estou pegando as notícias, o que vou extrair delas:
        #título e o link da notícia

        titulos = []
        links = []

        for noticia in lista_noticias:
            titulos.append(noticia.text)
            links.append(noticia.get("href"))

        #juntado titulo e link em um dicionário
        if not titulos or not links:
            print("Não possui dados sobre esse time. Tente com um time Brasileiro!")
            return 0
            
        dict_noticias = dict(zip(titulos, links))

        print(dict_noticias)
        
        
        return dict_noticias
    
    except Exception as error:
        print(f'Erro durante o scraping dos dados: {error}')
        raise Exception('Erro durante o scraping dos dados.')

def converte_em_json(dados, time):
    #Convertendo o dict em json e escrevendo um arquivo json com as notícias
    #a partir desse arquivo posso realizar novas funcionalidades no projeto,
    #o arquivo ficará na pasta do processo

    #coloquei a data atual, pois assim pode-se armazenar notícias de diferentes
    #datas sobre seu time na pasta do projeto

    try:
        data_atual = datetime.now()
        data_atual = data_atual.strftime('%d-%m-%Y')
        dados = json.dumps(dados, ensure_ascii=False, indent=3)
        with open(f'noticias_{time}-{data_atual}.json', 'w', encoding="utf-8") as arquivo:
            arquivo.write(dados)
    
    except Exception as error:
        print(f'Erro durante a conversão em json: {error}')
        raise Exception('Erro durante a conversão em json.')


