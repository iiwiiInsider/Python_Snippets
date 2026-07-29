import requests
import twilio

# -----------------------------
# CONFIGURATION
# -----------------------------
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# -----------------------------
# STEP 1 — STOCK PRICE CHECK
# -----------------------------
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()  # ensures request didn't fail

data = response.json().get("Time Series (Daily)")
if not data:
    raise ValueError("AlphaVantage response missing 'Time Series (Daily)' — check API key or rate limits.")

# Convert dict → list sorted by date (newest first)
data_list = [value for (_, value) in sorted(data.items(), reverse=True)]

yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

print("Yesterday:", yesterday_closing_price)
print("Day Before:", day_before_yesterday_closing_price)

# Price difference
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"

# Percentage difference
diff_percent = round((difference / yesterday_closing_price) * 100)
print("Change:", diff_percent, "%")

# -----------------------------
# STEP 2 — GET NEWS IF CHANGE > 5%
# -----------------------------
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    articles = news_response.json().get("articles", [])
    three_articles = articles[:3]

    print("Top 3 Articles:", three_articles)

    # -----------------------------
    # STEP 3 — SEND SMS VIA TWILIO
    # -----------------------------
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"Headline: {article.get('title', 'No title')}\n"
        f"Brief: {article.get('description', 'No description')}"
        for article in three_articles
    ]

    client = twilio.rest.Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
        print("Message sent:", message.sid)
else:
    print("Price change not large enough — no news fetched.")
