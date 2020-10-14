import requests

mainurl = "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f44629a0b55645128a79629181445176"

openpage = requests.get(mainurl).json()
article = openpage['articles']

for i in article:
    print(f"""  author: {i['author']}
                title: {i['title']}
                description: {i['description']}
                url: {i['url']}
        """)

