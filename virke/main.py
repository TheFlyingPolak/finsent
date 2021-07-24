import sentence_finder


def main():
    keyword = input("What word would you like me to find:")
    content = scraper.scrape(10)
    sentences = sentence_finder.find_sentences(content, keyword)

    for s in sentences:
        print(s)


if __name__ == '__main__':
    main()