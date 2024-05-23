import requests
import bs4
import json
from datetime import datetime
from pathlib import Path


class ScrapingGloboEsporte:
   
    """
    Classe para realizar scraping de notícias de um time de 
    utebol no site Globo Esporte.
    """
    
    def __init__(self, time):
        """
        Inicializa a instância da classe com o nome do time.

        Args:
            time (str): Nome do time o qual as notícias serão coletadas.
        """
        self._time = time.lower()
        self._url =  f'https://ge.globo.com/futebol/times/{self._time}/'
        self._session = requests.Session()

    def _realiza_request(self):
        """
        Realiza a requisição HTTP para obter o conteúdo da página do time.

        Raises:
            requests.RequestException: Erro durante a requisição.

        Returns:
            requests.Response: Resposta contendo o HTML da página.
        """
        try:
            resposta = self._session.get(self._url)
            resposta.raise_for_status()  
            return resposta
        
        except Exception as error:
            raise Exception(f'Erro durante a realização do Requests: {error}')

    def scraping(self):
        """
        Extrai os links de notícias da página.

        Returns:
            lista_noticias : list of bs4.element.Tag
            Lista de elementos <a> contendo as notícias.
        """
        dados = self._realiza_request()
        pagina = bs4.BeautifulSoup(dados.text, "html.parser")
        lista_noticias = pagina.find_all('a', class_="feed-post-link")
        return lista_noticias
    
    def _manipula_dados(self):
        """
        Extrai e organiza os títulos e links das notícias em um dicionário.

        Raises:
            Exception: Se não houver dados sobre o time no Globo Esporte.
            Exception: Erro durante a manipulação nas estruturas de dados.

        Returns:
            dict:  Dicionário com os títulos das notícias como chaves 
            e os links como valores.
        """
            
        try:
            noticias = self.scraping()
            titulos = []
            links = []

            for noticia in noticias:
                titulos.append(noticia.text)
                links.append(noticia.get("href"))

            if not titulos or not links:
                raise Exception(
                    'Não possui dados sobre o time no Globo Esporte.')
            
            dict_noticias = dict(zip(titulos, links))
            return dict_noticias
    
        except Exception as error:
            raise Exception(f'Erro durante a manipulação dos dados: {error}')
    
    @property
    def exibe_scraping(self):
        """
        Exibe os títulos e links das notícias no console.
        """
        dados = self._manipula_dados()
        for noticia, link in dados.items():
            print(f'{noticia} : {link}\n')


    def _converte_em_json(self, nome_arquivo):
        """
        Converte os dados das notícias em JSON e salva em um arquivo.

        Args:
            nome_arquivo (str): Nome do arquivo onde os dados JSON serão
            salvos.

        Raises:
            Exception: Erro durante a conversão para JSON ou escrita 
            no arquivo.
        """

        try:
            noticias = self._manipula_dados()
            dados = json.dumps(noticias, ensure_ascii=False, indent=3)
            with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
                arquivo.write(dados)
        
        except Exception as error:
            raise Exception('Erro durante a conversão em json.')


    def salvar_arquivo(self):
        """
        Cria o diretório do time e salva as notícias em um arquivo JSON.

        Raises:
            Exception: Erro ao salvar o arquivo JSON.
        """
        try:
            pasta = Path(f'./{self._time}')
            pasta.mkdir(exist_ok=True)
            data_atual = datetime.now()
            data_atual = data_atual.strftime('%d-%m-%Y')
            nome_arquivo = f'noticias_{self._time}_ [{data_atual}].json'
            caminho_arquivo = pasta / nome_arquivo
            self._converte_em_json(caminho_arquivo)
            print(f'Arquivo JSON salvo em: {caminho_arquivo}')
        except Exception as error:
            raise Exception(f'Erro ao salvar o arquivo: {error}')
   
    
