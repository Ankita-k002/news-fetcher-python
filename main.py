import requests


query=input("What kind of NEWS are you interested today?\n")
api="YOUR_API_KEY"  # Put your API key here, from NEWSAPI u can get that

url=f"https://newsapi.org/v2/everything?q={query}&from=2026-03-17&sortBy=publishedAt&apiKey={api}"

r=requests.get(url)


data=r.json()
articles=data["articles"]

for index,article in enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("\n**************************************************\n")

print("URL=",url)
print("\n**************************************************\n")
