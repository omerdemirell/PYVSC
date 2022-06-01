import feedparser

#First of all, I enter the url of the news source that I want to shoot the news.
url = "http://www.cnnturk.com/feed/rss/news"
news = feedparser.parse(url)


#Finally, I pull my news from the source using the for loop.
i = 0 
for new in news.entries:
    i += 1
    print(i)
    print(new.title)
    print(new.link)
    print(new.summary)
    print("\n")
    