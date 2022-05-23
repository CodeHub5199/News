import requests
import json
import streamlit as st
from datetime import date
import time
import pyttsx3

st.title('Breaking News')
date_stamp = time.strftime('%a , %d  %b %Y , %I:%M %p',time.localtime())
c1,c2,c3 = st.columns(3)
with c3:
    st.write(date_stamp)

st.sidebar.subheader('Filters')
country_list = st.sidebar.selectbox('Select Country: ',['India','United States','United Kingdom','Singapore','Germany','France','Canada','Russia','Saudi Arabia','Ukraine'])
country_dict = {'India':'in','United States':'us','United Kingdom':'gb','Singapore':'sg','Germany':'de','France':'fr','Canada':'ca','Russia':'ru','Saudi Arabia':'sa','Ukraine':'ua'}
country = country_dict[country_list]
headlines = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=7c053139fa444fd1b03371509b60b9b2'
business = f'https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey=7c053139fa444fd1b03371509b60b9b2'
entertainment = f'https://newsapi.org/v2/top-headlines?country={country}&category=entertainment&apiKey=7c053139fa444fd1b03371509b60b9b2'
health = f'https://newsapi.org/v2/top-headlines?country={country}&category=health&apiKey=7c053139fa444fd1b03371509b60b9b2'
science = f'https://newsapi.org/v2/top-headlines?country={country}&category=science&apiKey=7c053139fa444fd1b03371509b60b9b2'
sports = f'https://newsapi.org/v2/top-headlines?country={country}&category=sports&apiKey=7c053139fa444fd1b03371509b60b9b2'
technology = f'https://newsapi.org/v2/top-headlines?country={country}&category=technology&apiKey=7c053139fa444fd1b03371509b60b9b2'

st.sidebar.markdown('''---''')

category = st.sidebar.radio('Select News Category',['Headlines','Business','Entertainment','Health','Science','Sports','Technology'])

if category == 'Headlines':
    st.subheader(f'Top 10 {category} in {country_list}')
    re = requests.get(headlines)
    data = json.loads(re.content)
    for i in range(10):
        news = data['articles'][i]['title']
        description = data['articles'][i]['description']
        link = data['articles'][i]['url']
        st.write(i+1,' ',news)
        st.write('Description: ',description)
        st.write('Read full article: ',link)
        if st.button(f'Listen short news {i+1}'):
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-20)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) 
            engine.say(description)
            engine.runAndWait()

elif category == 'Business':
    st.subheader(f'Top 10 {category} News in {country_list}')
    re = requests.get(business)
    data = json.loads(re.content)
    for i in range(10):
        news = data['articles'][i]['title']
        description = data['articles'][i]['description']
        link = data['articles'][i]['url']
        st.write(i+1,' ',news)
        st.write('Description: ',description)
        st.write('Read full article: ',link)
        if st.button(f'Listen short news {i+1}'):
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-20)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) 
            engine.say(description)
            engine.runAndWait()

elif category == 'Entertainment':
    st.subheader(f'Top 10 {category} News in {country_list}')
    re = requests.get(entertainment)
    data = json.loads(re.content)
    for i in range(10):
        news = data['articles'][i]['title']
        description = data['articles'][i]['description']
        link = data['articles'][i]['url']
        st.write(i+1,' ',news)
        st.write('Description: ',description)
        st.write('Read full article: ',link)
        if st.button(f'Listen short news {i+1}'):
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-20)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) 
            engine.say(description)
            engine.runAndWait()

elif category == 'Health':
    st.subheader(f'Top 10 {category} News in {country_list}')
    re = requests.get(health)
    data = json.loads(re.content)
    for i in range(10):
        news = data['articles'][i]['title']
        description = data['articles'][i]['description']
        link = data['articles'][i]['url']
        st.write(i+1,' ',news)
        st.write('Description: ',description)
        st.write('Read full article: ',link)
        if st.button(f'Listen short news {i+1}'):
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-20)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) 
            engine.say(description)
            engine.runAndWait()

elif category == 'Science':
    st.subheader(f'Top 10 {category} News in {country_list}')
    re = requests.get(science)
    data = json.loads(re.content)
    for i in range(10):
        news = data['articles'][i]['title']
        description = data['articles'][i]['description']
        link = data['articles'][i]['url']
        st.write(i+1,' ',news)
        st.write('Description: ',description)
        st.write('Read full article: ',link)
        if st.button(f'Listen short news {i+1}'):
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-20)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) 
            engine.say(description)
            engine.runAndWait()

elif category == 'Sports':
    st.header(f'Top 10 {category} News in {country_list}')
    re = requests.get(sports)
    data = json.loads(re.content)
    for i in range(10):
        news = data['articles'][i]['title']
        description = data['articles'][i]['description']
        link = data['articles'][i]['url']
        st.write(i+1,' ',news)
        st.write('Description: ',description)
        st.write('Read full article: ',link)
        if st.button(f'Listen short news {i+1}'):
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-20)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) 
            engine.say(description)
            engine.runAndWait()

elif category == 'Technology':
    st.subheader(f'Top 10 {category} News in {country_list}')
    re = requests.get(technology)
    data = json.loads(re.content)
    for i in range(10):
        news = data['articles'][i]['title']
        description = data['articles'][i]['description']
        link = data['articles'][i]['url']
        st.write(i+1,' ',news)
        st.write('Description: ',description)
        st.write('Read full article: ',link)
        if st.button(f'Listen short news {i+1}'):
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-20)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) 
            engine.say(description)
            engine.runAndWait()