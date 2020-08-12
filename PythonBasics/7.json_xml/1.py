import json
import xml


# PARSING JSON
print('=====PARSING JSON=====')
with open('file.json', 'r', encoding='utf-8') as file:
    json_dict = json.load(file)

words = dict()
for news in json_dict['rss']['channel']['items']:

    all_words = news['description'].lower().split()
    for word in all_words:
        if len(word) > 6:
            words[word] = words.get(word, 0) + 1

counter = 0
for w in sorted(words, key=words.get, reverse=True):
    if counter < 10:
        print(w, words[w])
        counter += 1
# Если нужно одно значение
# max_value = max(words.values())
# max_keys = [k for k,v in words.items() if v == max_value]
# print(max_keys, max_value)


# PARSING XML
print('=====PARSING XML=====')
words_x = dict()
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file='file.xml')
lst = tree.findall('channel/item/description')
for item in lst:
    article = item.text
    words_x_list = article.lower().split()
    for word in words_x_list:
        if len(word) > 6:
            words_x[word] = words_x.get(word, 0) + 1

counter_x = 0
for w in sorted(words_x, key=words_x.get, reverse=True):
    if counter_x < 10:
        print(w, words_x[w])
        counter_x += 1
