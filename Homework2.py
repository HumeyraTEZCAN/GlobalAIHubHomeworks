
name=input("Please enter your name:")
surname=input("Please enter your surname:")
age=input("Please enter your age:")
birthYear=input("Please enter your birth year:")
userlist=[name, surname, age, birthYear]

for i in range(len(userlist)):
    print(userlist[i])


if(int(age)<18):
    print("You can't go out because it's too dangerous")

else:
    print("You can go out to the street")
