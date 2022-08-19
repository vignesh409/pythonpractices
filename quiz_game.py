from tkinter import N
from tkinter.messagebox import YES


print("Welcome to Quiz Game!!")

playing=input('Want to Play Game? yes or no  ')

if playing !="yes":
    quit()


print("Welcome Let`s Play")
score=0
answer=input("What does CPU stand for?")
if answer =="central processing unit":
    print("Correct")
    score+=1
else:
    print("Wrong Answer!! \n Hint:Brain")
answer=input("Why Mouse used for?")

if answer =="Tracking":
    print("Correct")
    score+=1
else:
    print("Wrong Answer!! \n Hint:mice")
answer=input("What does CPU stand for?")

if answer =="central processing unit":
    print("Correct")
    score+=1
else:
    print("Wrong Answer!! \n Hint:Brain")

answer=input("What does CPU stand for?")
if answer =="central processing unit":
    print("Correct")
    score+=1
else:
    print("Wrong Answer!! \n Hint:Brain")

answer=input("What does CPU stand for?")
if answer =="central processing unit":
    print("Correct")
    score+=1
else:
    print("Wrong Answer!! \n Hint:Brain")

answer=input("What does CPU stand for?")
if answer =="central processing unit":
    print("Correct")
    score+=1
else:
    print("Wrong Answer!! \n Hint:Brain")

print("You scored"+ str(score) + "points")