import requests

def get_into_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('query'),
        }

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


    def main():
        ip = input('Please enter a target IP: ')

        get_into_by_ip(ip=ip)


    if name == 'main':

