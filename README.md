# Scraping_Globo_Esporte

# Sobre o projeto

Esse projeto é um Webscraping do site de qualquer time brasileiro no Globo Esporte, utilizando Python, Beautiful Soup e Requests, este projeto captura as 
últimas notícias, estatísticas e resultados do time que você preferir diretamente do site do GE. 

Durante o processo, o robô faz uma requisição ao site, realiza a extração dos dados das últimas notícias e ao final do processo ele grava as notícias
em um arquivo json, em uma pasta com o nome do time e o arquivo possui o nome da data que a requisição foi feita. Exemplo:
'Noticias_Internacional- 20-02-2024.json'

Assim você pode armazenar as notícias de datas diferentes sobre o seu time.

# Tecnologias Utilizadas

Python

## Bibliotecas Utilizadas

Beautiful Soup 4
Requests


## Sobre o código

O projeto foi realizado em POO, onde o arquivo (globo_esporte.py) contém todos os métodos utilizadas, onde o robô faz a requisição ao site do GE,
realiza a extração dos dados (título e link da matéria) e converte em um dicionário onde a chave é o título e o valor é o link da notícia,
ao final ele escreve esse dicionário em um arquivo json que ficará salvo na pasta do processo, com o nome "noticias_{seu_time}-{data atual}.json".

As funções são chamados dentro do arquivo main, onde é inserido qual o time que o robô fará o scraping no seguinte trecho:
```python
#Eu inseri o Internacional como o time, pois é meu time do coração, mas você deve realizar a alteração caso torcer para outro clube.
time = 'Internacional'
scraping = ScrapingGloboEsporte(time)
```
Após isso, será possível acessar os métodos da classe com a váriavel scraping.

# Como executar o projeto
Pré-requisitos: Python 3.11

```bash
#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
pip install -r requirements.txt
```

# Executar o projeto
python main.py

## Observações:

Por ser um WebScraping baseado no código fonte do site e utilizando seletores da página, pode ser que em 
algum momento o Scraping pare de funcionar caso o site mude.

# Autor
Samael Muniz Picoli
