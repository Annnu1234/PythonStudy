import numpy as np

arr=np.array([0x00,0x01])

def main():
    print(arr)

if __name__=="__main__":
    main()
    arr= np.append(arr,55)
    main()