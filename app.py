import requests
import datetime
import notifypy
import time

api_key="TYPE_API_KEY_HERE" # API key
base_url = f"https://api.worldnewsapi.com/search-news?api-key={api_key}"

curr_dt = str(datetime.datetime.today())
split_dt = curr_dt.split()
split_dt[1] = '00:00:00'
today = " ".join(split_dt)
sources = "https://english.alarabiya.net" #Source links seperated by commas

def get_news(keyword):
    url = f"{base_url}&text={keyword}&earliest-publish-date={today}&language=en&news-sources={sources}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
news = get_news("subject") #Replace with news subject

notification = notifypy.Notify()
notification.title = "News"
for i in range(3): #Change for number of summaries to recieve
        notification.message = news["news"][i]["summary"]
        notification.send()
        time.sleep(5)