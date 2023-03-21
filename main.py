import requests
import datetime
import random
from twilio.rest import Client
import os

CRYPTO = "BTC"
COMPANY_NAME = "Tesla Inc"

CRYPTO_ENDPOINT = "https://www.alphavantage.co/query"
CRYPTO_API = os.environ['CRYPTO_API_1']
CRYPTO_PARMETER = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "BTC",
    "market": "USD",
    "apikey": CRYPTO_API
}

# News
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEW_API = os.environ['NEWS_API']
NEWS_PARAMETER = {
    "apiKey": NEW_API,
    "q": "BTC",
    "pageSize": 2,
}

#Twilio
ACCOUNT_ID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

client = Client(ACCOUNT_ID,AUTH_TOKEN)


#Time set
currentTime = datetime.datetime.now()

yesterday = str(currentTime.date() - datetime.timedelta(days = 1))
today = str(currentTime.date())




#Crypto response
crypto_response = requests.get(url=CRYPTO_ENDPOINT, params=CRYPTO_PARMETER)
crypto_response.raise_for_status()
crypto_data_today = crypto_response.json()["Time Series (Digital Currency Daily)"][today]
crypto_data_yesterday = crypto_response.json()["Time Series (Digital Currency Daily)"][yesterday]
revenue = (float(crypto_data_today["4a. close (USD)"]) - float(crypto_data_yesterday["4a. close (USD)"]))
percentage = abs(round((revenue / float(crypto_data_today["4a. close (USD)"]) ) * 100))
print(float(crypto_data_today["4a. close (USD)"]) - float(crypto_data_yesterday["4a. close (USD)"]))
print(percentage)
print(5/100)



#Determineing whether increased or descrease
crypto_news_response = requests.get(url = NEWS_ENDPOINT, params=NEWS_PARAMETER)
crypto_news_response.raise_for_status()
crypto_news_data = crypto_news_response.json()

news_list = [news for news in crypto_news_data["articles"][:3]]

if (revenue < 0 and percentage > 5):
    #decrease
    
    random_ = random.choice(news_list)
    message = client.messages.create(
        body = f"BTC is having a tough time 🔻{percentage}% \n"
               f"Title: {random_['title']}\n\n"
               f"{random_['description']}\n\n"
               f"Link to check: {random_['url']}\n\n",
        from_="+15076186462",
        to="+14379737554"
    )

    print(message.status)


elif(revenue > 0 and percentage > 5):
    #increase
    random_ = random.choice(news_list)
    message = client.messages.create(
        body=f"BTC skyrokets!! 🔺{percentage}% \n\n"
             f"Title: {random_['title']}\n\n"
             f"{random_['description']}\n\n"
             f"Link to check: {random_['url']}\n\n",
        from_="+15076186462",
        to="+1437973755"
    )

    print(message.status)

