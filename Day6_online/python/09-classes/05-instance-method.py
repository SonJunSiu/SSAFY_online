class Counter:
    def __init__(self):
        self.count = 0
    def incremnet(self) :
        self.count += 1

c = Counter()
# Counter.__init__(인스턴스)
print(c.count) # 0
c.incremnet()
print(c.count)


c2 = Counter()

print(c2.count)  # 