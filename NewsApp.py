import requests
import tkinter as tk


def getNews():
    api_key = "69098ca7575f42069325e5168a565e07"
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n"

    label.config(text = my_news)



canvas = tk.Tk()
canvas.geometry("1080x800")
canvas.title("Taja News")

label = tk.Label(canvas, font = 20, justify = "left")
label.pack(pady = 10)

getNews()

canvas.mainloop()