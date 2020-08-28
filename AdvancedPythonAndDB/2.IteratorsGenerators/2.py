class CustomIterator:
    def __iter__(self):
        return self

    def __init__(self, filename):
        self.filename = filename
        self.x = 0
        file = open(self.filename, 'r', encoding='utf-8')
        self.lines_list = file.readlines()
        file.close()

    def __next__(self):
        try:
            line = self.lines_list[self.x]
            self.x += 1
            return line.rstrip()
        except IndexError:
            raise StopIteration




iterator1 = CustomIterator(input('Enter filename (2.txt for test): '))

print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
