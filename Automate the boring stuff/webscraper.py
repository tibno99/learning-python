import webbrowser
import requests
#webbrowser.open('https://www.autotrader.ca/')
#webbrowser.open('https://www.avalanche.ca/')


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code
print(res.text[:100])

