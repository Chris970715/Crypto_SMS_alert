# Crypto_SMS_alert
I wrote code to send me a SMS message about Bitcoin decreasing or  increasing

![unnamed](https://user-images.githubusercontent.com/39882035/226503175-9efa9788-616c-4732-bef8-b6268ccac9bd.jpg)

This is a test picture. I decreased if statement condition down and changed targeted crypto to test.


This code is a Python program that fetches the daily closing price of a cryptocurrency (in this case, Bitcoin or BTC) and determines whether the price has increased or decreased by more than 5% from the previous day's closing price. If the price has increased or decreased by more than 5%, the program fetches the top two news articles related to Bitcoin and sends an SMS message via the Twilio API to a specific phone number, along with a link to the news article.


![liberary](https://user-images.githubusercontent.com/39882035/226504101-f51a522d-50ee-4bc7-988a-200d70e90053.png)


The program first imports the necessary libraries and defines some constants and parameters for the APIs used to fetch cryptocurrency price and news data. It also sets up the Twilio client for sending SMS messages.

![mainfsdfsd](https://user-images.githubusercontent.com/39882035/226504649-d613eeae-4d0d-4756-9290-e3eff5290ac4.png)


Next, the program fetches the current day's and previous day's cryptocurrency price data using the AlphaVantage API and calculates the percentage change in price. If the percentage change is greater than 5%, the program fetches the top two news articles related to Bitcoin using the NewsAPI and selects one at random. It then sends an SMS message to the specified phone number using the Twilio API, including the percentage change in price, the title and description of the selected news article, and a link to the article.

If the percentage change in price is less than or equal to 5%, no SMS message is sent.
