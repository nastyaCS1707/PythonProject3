import json

from Ipify import Ipify

class FileManager:
    @staticmethod
    def check_file_name(file_name):
        if file_name.endswith(".json"):
            pass
        else:
            file_name += ".json"
        return file_name

    @staticmethod
    def create_file_with_city(file_name):
        city = Ipify.get_city()
        with open(file_name, "w", encoding="utf-8") as write_file:
            json_city = {
                "city": city,
            }
            json.dump(json_city, write_file)