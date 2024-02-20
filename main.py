import processo

#Esse projeto irá fazer um scraping de notícias novas do seu time no 
#Globo Esporte, ao final ele irá escrever um arquivo json
#no formato "noticias_nome do time-data atual"
#com o título da matéria e o link da mesma.

time = 'internacional'
noticias = processo.requisicao_noticias(time)
dados = processo.extraindo_dados(noticias)
processo.converte_em_json(dados, time)
