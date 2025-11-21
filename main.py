

'''import requests  # Для HTTP-запросов
import time      # Для функции sleep


# Список популярных городов Великобритании
POPULAR_UK_CITIES =['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York'] # Заполните список городами Великобритании

# Ключ доступа к API
API_KEY = '6920c53755d3c414928463kzv932756'

def find_uk_city(coordinates: list) -> str:
    url= "https://geocode.maps.co/reverse?"
    for coordinat in coordinates:
        lat= list(coordinat)
        param= {'lat': lat[0],
                'lon': lat[1],
                'api_key': API_KEY,
                }
       
        response=requests.get(url,params=param)
        city=response.json()['address']['city']
        if  city in POPULAR_UK_CITIES:
            print(response.json()['address']['city'])
            return response.json()['address']['city']


if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),  # Москва
        ('52.3727598', '4.8936041'),          # Амстердам
        ('53.4071991', '-2.99168')            # Ливерпуль
    ]
    assert find_uk_city(_coordinates) == 'Liverpool''''
