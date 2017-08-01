import requests
import json

def get_player_apps(steam_id):
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=9ACA027FB904D3DE671F6DFF07A0C69B&steamid="+ steam_id +"&format=json"
