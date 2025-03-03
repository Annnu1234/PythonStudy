from enum import Enum

class data(Enum):
    Aniruddha = 0
    Aradhya = 1
    Advika = 2


if __name__=="__main__":
    print(data(0).name, data(0).value)

  