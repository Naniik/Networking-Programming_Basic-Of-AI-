import requests
url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20261012&end=20261018&valcode=usd&sort=exchangedate&order=desc&json"
for code in ["usd", "eur"]:
    params = {
        "start": "20261012",
        "end": "20261018",
        "valcode": code,
        "sort": "exchangedate",
        "order": "desc",
        "json": "",
    }
    data = requests.get(url, params=params).json()

    print(code.upper())
    for item in data:
        print(item["exchangedate"], item["rate"])