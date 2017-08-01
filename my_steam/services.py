import requests
import json

def get_player_apps(steam_id):
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=9ACA027FB904D3DE671F6DFF07A0C69B&steamid="+ steam_id +"&format=json"
    response = requests.get(url)
    player_apps = json.loads(response.text)
    app_list = []
    for game in player_apps['response']['games']:
        app_list.append(game['appid'])
    return app_list

def get_app_data(appid):
    url =  "http://store.steampowered.com/api/appdetails?appids=" + str(appid)
