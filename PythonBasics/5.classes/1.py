class Animals():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print("This one was feeded")

    def info(self):
        print("Name:", self.name, "Weight:", self.weight)

class Birds(Animals):
    def collect_eggs(self):
        print("Eggs collected")
    def voice(self):
        print("Chirick")

class CowsAndKoza(Animals):
    def get_milk(self):
        print("They surrendered and gave their milk")

    def voice(self):
        print("Mu/Me")

class Sheeps(Animals):
    def cut_hair(self):
        print("Sheep's hair was cut")

    def voice(self):
        print("Megege sheep says")


goose1 = Birds("g1", 2)
goose2 = Birds("g2", 3)
cow1 = CowsAndKoza("c1", 35)
sheep1 = Sheeps("s1", 10)
sheep2 = Sheeps("s2", 11)
chicken1 = Birds("ch1", 2)
chicken2 = Birds("ch2", 3)
koza1 = CowsAndKoza("k1", 7)
koza2 = CowsAndKoza("k2", 8)
duck = Birds("d1", 4)


goose1.info()
goose2.feed()
cow1.get_milk()
sheep1.cut_hair()
chicken1.voice()
