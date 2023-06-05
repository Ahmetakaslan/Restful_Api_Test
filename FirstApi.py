import requests
iladi=str(input("il ismi giriniz"))
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": f"{iladi}",
    "appid": "add api key",
    "lang":"tr"
}

response = requests.get(url, params=params)
data =response.json()

def convert(kelvin):
     celcius=(kelvin-273.15 )
     return celcius

if response.status_code == 200:
    data = response.json()
    if data:
        temperature = data["main"]["temp"]
        aciklama = data["weather"][0]["description"]
        icon= data["weather"][0]["icon"]
        il=data["name"]
        sicaklik=convert(temperature)
        sicaklik=str(sicaklik)
        sicaklik= sicaklik[0:4]
        print("il :" ,il)
        print("Sıcaklık :",sicaklik)
        print("Icon :",icon)
    
        print("Acıklama :", aciklama)
    else:
        print("No results found.")
else:
    print("Error:", response.status_code, response.text)
#print(data)
