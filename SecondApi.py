import requests

api_key = "037a018cacc80be5140667fd5804eb226b6c29999483edaae3b307d009252dcf"
url = f"https://min-api.cryptocompare.com/data/top/mktcapfull?limit=2&tsym=USD&api_key={api_key}&lang=tr"

response = requests.get(url)
data = response.json()
print(data)
for coin in data['Data']: 
    print(f"Ad: {coin['CoinInfo']['FullName']}")
    print(f"Piyasa Değeri: {coin['DISPLAY']['USD']['MKTCAP']}")
    print(f"24 Saatlik Hacim: {coin['DISPLAY']['USD']['TOTALVOLUME24H']}")
    print("----------------------------------------------------")
