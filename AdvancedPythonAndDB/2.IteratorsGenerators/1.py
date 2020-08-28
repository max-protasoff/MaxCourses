import json


with open('1.json', 'r', encoding='utf-8') as json_file:
    json_dict = json.load(json_file)

class CustomIterator:
    def __iter__(self):
        return self

    def __init__(self, filename):
        with open(filename, 'r', encoding='utf-8') as json_file:
            self.json_dict = json.load(json_file)
        self.x = 0

    def __next__(self):
        try:
            country = self.json_dict[self.x]["name"]["common"]
            url = 'https://en.wikipedia.org/wiki/' + country
            self.x += 1
            return country + ' - ' + url
        except IndexError:
            raise StopIteration




iterator1 = CustomIterator('1.json')
for i in iterator1:
    print(i)
