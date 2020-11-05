from GoogleNews import GoogleNews

def todaysNews(str):
    googlenews = GoogleNews()
    googlenews = GoogleNews('en', 'd')

    googlenews.search(str)
    googlenews.getpage(1)

    googlenews.result()
    g = googlenews.gettext()
    return g

keyword = input("Enter the country or keyword: ")
todaynews = todaysNews(keyword)
for news in todaynews:
    print(news)
    
    
# we can directly return googlenews.result and this will show complete news with title, link, description and dates.
