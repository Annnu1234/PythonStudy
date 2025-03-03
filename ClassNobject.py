

class Book:
    rool = "Aniruddha"
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def increse(self):
        Book.count +=1


if __name__=="__main__":
    cls = Book("Bhai",29)
    #print(cls.name, cls.age)
    #cls.age = 50
    cls1 = Book("edi",29)
    #cls = Book()
    print(cls.count)
    cls.increse()
    print(cls.count)
    cls1.increse()
    print(cls.count)