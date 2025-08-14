import requests

def cripto(filters = {}):
  url = f"https://api.coingecko.com/api/v3/simple/price"
  response = requests.get(url, params = filters)

  if response.status_code == 200:
    return response.json()
  else:
    return None

moeda = input("Digite o nome da moeda que você quer saber sobre: ")

coin = cripto({"ids": moeda, "vs_currencies": "brl"})

if coin and moeda in coin:
    preco = coin[moeda]["brl"]
    print(f"O preço atual de {moeda} é R$ {preco}")
else:
    print("Moeda não encontrada ou erro na requisição.")