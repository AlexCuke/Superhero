import requests

def get_the_smartest_superhero(superheros_ids):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    data = response.json()
    
    smartest_hero = ['', 0]  # [name, intelligence]
    
    # Поиск героя с максимальным intelligence из переданных id
    for hero in data:
        if hero['id'] in superheros_ids:
            intelligence = hero.get('powerstats', {}).get('intelligence', 0)
            if intelligence > smartest_hero[1]:
                smartest_hero[0] = hero['name']
                smartest_hero[1] = intelligence
                
    return smartest_hero[0]

# Пример использования:
hero_ids = [332, 149, 655]  # например, id для Hulk, Captain America, Thanos
print(get_the_smartest_superhero(hero_ids))
