# Akbhar padkhe sunaooo
import json
import requests
def speak_good(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak_good("Breaking news!!")
    speak_good("Headlines of the day are:-")
    url = "https://api.wazirx.com/sapi/v1/tickers/24hr"
    essay = requests.get(url).text
    essay = json.loads(essay)
    print(essay["symbol"])
    a = essay["symbol"]
    speak_good(a)











