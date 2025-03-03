
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

#in public and private method only __ required to add before veriable / function name
#public menthod
    def salary(self):
        return self.__salary  # Access through public method

#private menthod
    def __salary(self):
        return self.__salary  # Access through private method

obj = Private()
print(obj.salary())  # public method
#print(obj.__salary)  # private method
