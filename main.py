import requests

link = 'https://api.drom.ru/v1.2/bulls/search'

payload = {'firmId': 5, 'cityId': 6}


# firmId - Фирма автомобиля (int)
# modelId - Модель автомобиля (int)
# generationNumber - Номер поколения (int)
# restylingNumber - Номер рестайлинга (int)
# cityId - Город (int)

r = requests.get('https://httpbin.org/get', params=payload)


# r = requests.get('https://api.github.com/events')
print(r.url)
print(r.text)
