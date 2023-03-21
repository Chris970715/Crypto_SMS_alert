# Crypto_SMS_alert
I wrote code to send me a SMS message about Bitcoin decreasing or  increasing

![unnamed](https://user-images.githubusercontent.com/39882035/226503175-9efa9788-616c-4732-bef8-b6268ccac9bd.jpg)

This is a test picture. I decreased if statement condition down and changed targeted crypto to test.


This code is a Python program that fetches the daily closing price of a cryptocurrency (in this case, Bitcoin or BTC) and determines whether the price has increased or decreased by more than 5% from the previous day's closing price. If the price has increased or decreased by more than 5%, the program fetches the top two news articles related to Bitcoin and sends an SMS message via the Twilio API to a specific phone number, along with a link to the news article.

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


The program first imports the necessary libraries and defines some constants and parameters for the APIs used to fetch cryptocurrency price and news data. It also sets up the Twilio client for sending SMS messages.
