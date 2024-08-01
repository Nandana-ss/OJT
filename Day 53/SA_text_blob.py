from textblob import TextBlob

texts = [
    "I love NLP",
    "I am disappointed"
]

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment

for text in texts:
    sentiment = analyze_sentiment(text)
    print(f'Text: {text}')
    print(f'Sentiment: {sentiment}')
