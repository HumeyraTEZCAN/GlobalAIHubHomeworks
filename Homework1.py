
mylist=[]
for i in range(5):
    value=input("enter 5 different values:")
    if(value.isdigit()):
     print("value is integer")
    elif (value.isalpha()):
     print("value is string")
    else:
        print("value is float")

