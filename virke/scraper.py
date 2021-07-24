from finscraper.spiders import ISArticle

def scrape(num_items):
    content = []
    spider = ISArticle().scrape(num_items)
    articles = spider.get()
    for index, row in articles.iterrows():
        content.append(row['content'])
    
    return content