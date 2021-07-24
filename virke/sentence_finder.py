import scraper
from acora import AcoraBuilder
import re
import os.path
from os import path


def find_sentences(keyword):
    sentences = []
    #builder = AcoraBuilder(keywords)
    #ac = builder.build()

    #for text in data:
    #    type(text)
    #    #sentences.append(re.findall("[^.]*? päivä [^.]*\.", text))
    #    sentences.append([sentence for sentence in text.split('.') if keyword in sentence])
    # check if index directory exists
    if not path.exists("index"):
        os.mkdir("index")

    if not path.exists("index/" + keyword + ".txt"):
        sentences.append(_scrape_for_sentences(keyword))
    else:


    return sentences


def _find_indexed_sentences(keyword):
    #TODO


def _scrape_for_sentences(keyword):
    file = open("index/" + keyword + ".txt", "a")

    for content in scraper.scrape(10):
        lines = [sentence for sentence in content.split('.') if keyword in sentence]
        for line in lines:
            file.write(line)

