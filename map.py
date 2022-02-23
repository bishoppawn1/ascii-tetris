class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        print("hi my age and name are " + self.name + " " + self.age)

list1 = []
list1.append(Person("Bishop", "8"))
list1.append(Person("Aires", "4"))
list1.append(Person("mom", "37"))
list1.append(Person("dad", "38"))
i = 0
while len(list1) > i:
    z = list1[i]
    z.hi()
    i += 1