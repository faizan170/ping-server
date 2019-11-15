import requests 
import time
import random


def processUrls():
    timeRand = random.randint(60, 300)
    try:
        # api-endpoint 
        URL = "https://weexpat.azurewebsites.net/"
        
        # sending get request and saving the response as response object 
        r = requests.get(url = URL) 

        print(r.json)
    except:
        print("Error")
    print("Sleeping for:", timeRand/60, "minutes")
    time.sleep(timeRand)

processUrls()