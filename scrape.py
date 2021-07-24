from finscraper.spiders import ISArticle

spider = ISArticle().scrape(10)

articles = spider.get()

for index, row in articles.iterrows():
    print(row['content'])

