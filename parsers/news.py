from newsapi import NewsApiClient
from config import newsApiKey
from config import newsLanguage
from config import country

newsapi = NewsApiClient(api_key=newsApiKey)

def parseNews():
    news = newsapi.get_top_headlines(
        language=newsLanguage,
        country=country)

    return news