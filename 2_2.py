def Display(iNo):
    for i in range(1, iNo+1):
        for j in range(1, iNo+1):
            print("*", end=" ")
        print()

def main():
    print("Enter a number: ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>python 2_2.py
Enter a number:
5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>

'''