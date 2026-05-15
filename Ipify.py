import sys
import requests

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
