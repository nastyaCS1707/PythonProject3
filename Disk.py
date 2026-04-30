import requests

class Disk:

    @staticmethod
    def create_directory(token):
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': "QAMIDPY-132"}
        requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)

    @staticmethod
    def get_link(filename, token):
        Disk.create_directory(token)
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': f'QAMIDPY-132/{filename}'}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers=headers,
                                params=params)
        return response.json()['href']

    @staticmethod
    def upload_at_disk(filename, token):
        link = Disk.get_link(filename, token)
        with open("city.json", 'rb') as f:
            requests.put(link, files={'file': f})