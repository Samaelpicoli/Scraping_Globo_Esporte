from globo_esporte import ScrapingGloboEsporte

"""_    
Esse projeto irá fazer um scraping de notícias novas do seu time no 
Globo Esporte, ao final ele irá escrever um arquivo json
no formato "noticias_nome do time-data atual"
com o título da matéria e o link da mesma.
"""

time = 'cruzeiro'
scraping = ScrapingGloboEsporte(time)
scraping.scraping()
scraping.exibe_scraping
scraping.salvar_arquivo()