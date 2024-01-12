''' for GUI  -- tkinter
    for NLP  -- nltk
    for sentiment analysis  -- textblob
'''
import tkinter as tk
import nltk
from textblob import TextBlob 
from newspaper import Article

nltk.download('punkt')

#  url of the website from which news is read

url='https://www.hindustantimes.com/world-news/usuk-launch-massive-airstrikes-against-houthi-rebels-in-yemen-after-red-seai-shipping-attacks-101705019574947.html'

article=Article(url)

''' download article object obtained from the website,
        disect the data into required parts 
            and then parse it'''

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

#for sentiment analysis of the whole article on the website
analysis = TextBlob(article.text)

print(analysis.polarity)

# sentiment of the article

print(f'Sentiment: {"positive" if analysis.polarity >0 else "negative" if analysis.polarity <0 else "neutral"}')












'''  -----------------------------------     Shortened news from the website    -------------------------------

Title: US-UK launch massive airstrikes against Houthi rebels in Yemen after Red Sea shipping attacks
Authors: []
Publication Date: 2024-01-12 06:27:38+05:30
Summary: Iran based Houthis have taken responsibility of hijacking ships on the Red Sea, REUTERS/Khaled Abdullah(REUTERS)The airstrikes by US and UK, aimed at destroying Houthi bases in Yemen, has further escalated the conflicts in the area in the midst of the Israel-Hamas war.
The attacks against cargo ships in the Red Sea have disrupted the import-export chain in multiple countries, with the oil prices taking a hit in the process.
Houthi rebel attacks on the Red SeaThe Iran-based rebel group claimed responsibility for multiple hijackings and attacks on vessels and cargo ships travelling through the Red Sea, belonging to countries that have an “Israel link”.
The attack against Houthi rebels came after Iran's Navy on Thursday captured an oil tanker off the coast of Oman.
The attacks on Red Sea have seriously impacted the supply chain and oil prices for many countries, prompting strong action by US and UK.

'''
