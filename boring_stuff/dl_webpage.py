import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
with open('RomeoAndJuliet.txt', 'wb') as f:
    if response.status_code == 200:
        for chunk in response   :
            f.write(chunk)
    else:
        print("Error Code=%d" %(response.status_code))

