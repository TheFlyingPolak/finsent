import libvoikko

v = libvoikko.Voikko(u"fi")
word = "kissoja"
voikko_dict = v.analyze(word)
word_baseform = voikko_dict[0]['BASEFORM']
print(word_baseform)
