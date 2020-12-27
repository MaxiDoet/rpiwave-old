from newsapi import NewsApiClient
from config import *

newsapi = NewsApiClient(api_key=newsApiKey)

def parseNews():
    news = newsapi.get_top_headlines(
        language=config["services"]["newsLanguage"],
        country=config["services"]["newsCountry"])

    return news