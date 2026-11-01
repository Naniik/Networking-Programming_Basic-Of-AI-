import requests
import matplotlib.pyplot as plt
url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
rates={}
for code in ["usd", "eur"]:
    params = {
        "start": "20261012",
        "end": "20261018",
        "valcode": code,
        "sort": "exchangedate",
        "order": "asc",
        "json": "",
    }
    data = requests.get(url, params=params).json()
    dates = []
    values = []

    for item in data:
        dates.append(item["exchangedate"][:5])
        values.append(item["rate"])
        
    rates[code]={"dates": dates, "values": values}
    
plt.title('Values of exchange rates', fontsize=20, fontname='Times New Roman')
plt.xlabel('Dates', color='gray')
plt.ylabel('Values',color='gray')
plt.plot(rates["usd"]["dates"], rates["usd"]["values"], label='USD', color='orange')
plt.plot(rates["eur"]["dates"], rates["eur"]["values"], label='EUR', color='green')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


