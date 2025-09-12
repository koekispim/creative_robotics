"""Enter here your solutions to the flowchart exercises. 
each student does one on their computer and commit/push to the repository"""


# ---------- Flowchart Exercise 1 ---------- #
def exercise1(output):
    print(output)

exercise1('hello')


# ------ Flowchart Exercise 2 -----
def flowchart2(n):
    n = n+2
    print(n)

n = int(input("Enter a number: "))
flowchart2(n)


# ---------- Flowchat Exercise 3 ---------- #
def exercise3(input):
    if input > 0:
        print('Greater than 0')
    else:
        pass

exercise3(eval(input('Enter a number')))


# ------ Flowchart Exercise 4 -----
def flowchart4(i):
    if i > 0:
        print("Greater than 0")
    elif i < 0:
        print("Less than 0")
    else:
        print("Done")

i = int(input("Enter a number: "))
flowchart4(i)


