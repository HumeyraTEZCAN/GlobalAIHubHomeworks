
import random as ran
import random
import string


def pickaword(randomnumber):
    f = open("words.txt", "r")
    readwhole =f.read()
    wordslist =readwhole.splitlines()
    return wordslist[randomnumber]


def generatemenum():
    return ran.randint(1,999)


def getmeletter():
    return random.choice(string.ascii_letters)

name =input("Let's start playing, how should I call you?")
print("Welcome  " +name.capitalize())

stop =1
stop2=1


while stop==1:
 stop2=1
 mynum = generatemenum()
 picked = pickaword(mynum).lower()
 print("Word's length is:" + str(len(picked)))
 letter = input("please enter a letter:  ")
 while stop2==1:

  print("Word is:::::" + str(picked))
  print("Word's length is:" + str(len(picked)))

  if letter in picked:
   here=picked.index(letter)+1
   print( "It's "+str(here)+"th letter is: "+letter.capitalize())
   choose=input("Do you want to guess the word or want to enter a new letter? ((G) for guess, (L) for new letter)")
   if choose =='G':
    guess=input("Enter your guess:")
    if guess==picked:
     print("WELL DONE, YOU FOUND MY GUESS!!!!!!!")
     stop2=0
    else:
     print("POOR YOU, MY GUESS WAS: "+str(picked)+":D :D :D")
     stop2=0
   else:
     letter = input("enter a letter:")
     stop2 = 1
  else:
       print("try again")
       letter = input("please enter new value:")
       stop2 = 1

 stop = int(input("do you want to continue:"))




