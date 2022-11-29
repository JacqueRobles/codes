class PC():

    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def __repr__(self):
        return str(self.__dict__)

arr = []
arr.append(PC('a', 'b', 'c'))
arr.append(PC('d', 'e', 'f'))
arr.append(PC('g', 'h', 'i'))
arr.append(PC('j', 'k', 'l'))
print(arr)
