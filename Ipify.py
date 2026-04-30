import sys
import requests
import json

class Ipify:

    @staticmethod
    def get_ip ():
        response = requests.get("https://api.ipify.org/?format=json")
        if response.status_code != 200:
            print('Произошла какая-то ошибка')
            sys.exit(0)
        return response.json()["ip"]

    @staticmethod
    def get_city ():
        ip = Ipify.get_ip()
        response = requests.get(f"https://ipinfo.io/{ip}/geo")
        return response.json()["city"]

    @staticmethod
    def create_file(file_name):
        city = Ipify.get_city()
        with open(file_name, "w", encoding="utf-8") as write_file:
            json_city = {
                "city": city,
            }
            json.dump(json_city, write_file)