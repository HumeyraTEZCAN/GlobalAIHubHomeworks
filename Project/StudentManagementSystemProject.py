
def readstudents():
    f = open("Students.txt", "r")
    readwhole= f.read()
    studentslist=readwhole.splitlines()
    return studentslist


def wrongenter():
    for i in range(0,3):
        nameandsurname = input("Please enter your name and surname correctly:")



def calculatepercentage(grades):
  grades["Midterm"]*=0.30
  grades["Final"]*=0.50
  grades["Project"] *=0.20
  total=grades["Midterm"]+grades["Final"]+grades["Project"]
  return total


def passinggrades(total):
    if total > 90:
        return "AA"
    elif 70<total<90:
        return "BB"
    elif 50<total<70:
        return "CC"
    elif 30<total<50:
        return "DD"
    elif total<30:
        return "FF"



def courses(gradesdict):

 coursenumber = int(input("Please enter how many courses you took:"))
 if coursenumber > 3:
    print("1- CS101 HOW TO BE KING - OMER CENGIZ")
    print("2- CS102 PATIENCE LESSON -ELIF YIGIT")
    print("3- CS103 HOW TO BECOME DJ AND CALM AT THE SAME TIME- KUTAY AKALIN")
    print("4- CS1O4 HOW TO MAKE CHRISTMAS MERRY - AYSUDA CEYLAN")
    print("5- CS105 TURKISH GRAMMAR LESSON - DEMET AKALIN")
    for i in range(coursenumber):
        coursename = input("Please enter your " + str(int(i+1)) + "th course order number:")
        courselist.append(coursename)
    exam=input("Enter the code of the course that you took exam:")
    midtermgrade=int(input("Please enter the grade of your Midterm exam :"))
    finalgrade = int(input("Please enter the grade of your Final exam :"))
    projectgrade= int(input("Please enter the grade of your Project :"))
    gradesdict={"Midterm": midtermgrade, "Final": finalgrade, "Project": projectgrade}
    total=calculatepercentage(gradesdict)
    lettergrade=passinggrades(total)
    ffgrd="FF"
    if lettergrade==ffgrd:
        print("YOU FAILED FROM THE LESSON "+exam+" DO NOT WORRY: HAYAT KISA KUŞLAR UÇUYOR!")
    else:
     print("YOUR LETTER GRADE FROM THE "+exam+" LESSON IS: "+passinggrades(total)+"!!!")

 else:
    return print("You failed in class")



stop=1
nameandsurname=input("please enter your name and surname:")
mylist=readstudents();
courselist=[]
gradesdict={}
if nameandsurname in mylist:
    print("Welcome "+nameandsurname)
    courses(gradesdict)

else:
     wrongenter()
     print("Please try again later!!!!!!")


