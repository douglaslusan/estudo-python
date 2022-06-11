import requests
import json

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao = requisicao.json()

cotacao_dolar = requisicao['USDBRL']['bid']

print(cotacao_dolar)


