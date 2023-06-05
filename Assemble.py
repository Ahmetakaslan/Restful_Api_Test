from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/weather')
def get_weather_data():
   
    url = "https://api.openweathermap.org/data/2.5/weather"
    iladi = request.args.get('q')
    params = {
        "q": f"{iladi}",
        "appid": "2cca848d9a97f8dd3b06b8f4960f5b7a",
        "lang":"tr"
    }

    response = requests.get(url, params=params)
    
    def convert(kelvin):
       return kelvin-273
    if response.status_code == 200:
        data = response.json()
        if data:
            temperature = data["main"]["temp"]
            aciklama = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]
            il = data["name"]
            sicaklik = convert(temperature)
            sicaklik = str(sicaklik)
            sicaklik = sicaklik[0:6]
            a=str(aciklama)
            a= a.replace('ı','i').replace('ç','c').replace('ğ','g')
            
            
            return {"il": il, "Sicaklik": sicaklik, "Icon": icon, "Aciklama": a}
        else:
            return {"message": "No results found."}
    else:
        return {"message": f"Error {response.status_code}"}


@app.route('/crypto', methods=['GET'])
def get_crypto():
    api_key = "037a018cacc80be5140667fd5804eb226b6c29999483edaae3b307d009252dcf"
    url = f"https://min-api.cryptocompare.com/data/top/mktcapfull?limit=30&tsym=USD&api_key={api_key}&lang=tr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = []
        for coin in data['Data']:
            ad = coin['CoinInfo']['FullName']
            piyasa_degeri = coin['DISPLAY']['USD']['MKTCAP']
            saatlik_hacim = coin['DISPLAY']['USD']['TOTALVOLUME24H']
            result.append({
                "ad": ad,
                "piyasa_degeri": piyasa_degeri,
                "saatlik_hacim": saatlik_hacim
            })
        return jsonify(result)
    else:
        return jsonify({"error": f"Error {response.status_code}: {response.text}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
