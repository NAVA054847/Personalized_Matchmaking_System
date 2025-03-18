
from traceback import print_list
import os

from men import men
from women import women


m = men("benyamin lederman", 13.5, 160, "Ashkenaz", True, 986)
w = women("nava lederman", 19.5, 167, "Ashkenaz", True, 539)

listmen = [
    men("David Cohen", 30, 175, "Ashkenaz", "yes", 123),
    men("Moshe Levi", 28, 180, "Sfaradi", "no", 345),
    men("Avram shtrause ", 22, 182, "Sfaradi", "no", 346),
    men("Meir Shts", 28, 180, "Sfaradi", "no", 347),
    men("Yechiel Cohen", 23, 167, "Ashkenaz", "yes", 578),
]

listwomen = [
    women("Sara Levy", 25, 165, "Ashkenaz", "yes", 129),
    women("Rachel Cohen", 27, 170, "Sfaradi", "no", 543),
    women("Racheli Dan", 20, 180, "Sfaradi", "yes", 897),
    women("Rivka Chock", 22, 165, "Sfaradi", "no", 456),
    women("Chaya Strause", 19.5, 162, "Ashkenaz", "yes", 384),
]

def look_for():
    flag=False
    print("Hello! We're here to help you find a shidduch.")
    minn = input("If you're  women, type 'women'. If you're men, type 'men': ")
    age = int(input("Please enter the age: "))
    high = int(input("Please enter the height (in centimeters): "))
    typee = input("Please specify the background ('Ashkenaz'/'Sfaradi'): ")

    if minn == "men":
        learning = input("Do you want him to learn? (yes/no): ")
    else:
        learning = input("Do you want your husband to learn? (yes/no): ")

    if minn == "men":
        with open("filtered_women.txt", "w") as file:
            for women in listwomen:
                if women.age < age and women.height < high and women.typee == typee and women.learning == learning:
                    file.write(f"FullName: {women.fullname}, Age: {women.age}, Height: {women.height}, Type: {women.typee}, Learning: {women.learning}, Tz:{women.tz}\n")
                    flag=True

    else:
        with open("filtered_men.txt", "w") as file:
            for men in listmen:
                if men.age > age and men.height > high and men.typee == typee and men.learning == learning:
                    file.write(f"FullName: {men.fullname}, Age: {men.age}, Height: {men.height}, Type: {men.typee}, Learning: {men.learning}, Tz:{men.tz}\n")
                    flag = True

    if flag==False:
        print("we dont have a shiduch for you")
    else:
        print("go to 'filtered_men.txt'/'filtered_women.txt' in the left side")



def new_men():
    global listmen
    name = input("Please enter the name:")
    age = int(input("Please enter the age: "))  # Convert to int
    high = int(input("Please enter the height (in centimeters): "))  # Convert to int
    typee = input("Please specify the background ('Ashkenaz'/'Sfaradi'): ")
    learning = input("Do you want him to learn? (yes/no): ")
    tz = int(input("Please enter the tz: "))  # Convert to int
    m = men(name, age, high, typee, learning, tz)
    listmen.append(m)
    print("New list:")
    [print(i.fullname) for i in listmen]

def new_women():
    global listwomen
    name = input("Please enter the name:")
    age = int(input("Please enter the age: "))  # Convert to int
    high = int(input("Please enter the height (in centimeters): "))  # Convert to int
    typee = input("Please specify the background ('Ashkenaz'/'Sfaradi'): ")
    learning = input("Do you want her to learn? (yes/no): ")
    tz = int(input("Please enter the tz: "))  # Convert to int
    w = women(name, age, high, typee, learning, tz)
    listwomen.append(w)
    print("New list:")
    [print(i.fullname) for i in listwomen]

def delete():
    min = input("Enter which one you want to delete('men'/'women'): ")
    while min != "men" and min != "women":
        min = input("Enter which one you want to delete('men'/'women'): ")

    tzz = int(input("Enter the tz: "))  # Make sure it's an int

    if min == "men":
        global listmen
        listmen = [man for man in listmen if man.tz != tzz]
        print("New list:")
        [print(i.fullname) for i in listmen]
    else:
        global listwomen
        listwomen = [women for women in listwomen if women.tz != tzz]
        print("New list:")
        [print(i.fullname) for i in listwomen]


def dellfile(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted")
    except FileNotFoundError:
        print(f"{filename} not found")
    except Exception as e:
        print(f"an error occurred: {e}")



pressing = (input("Enter 'a' to add a man, enter 'b' to add a woman, enter 'c' to delete someone, enter 'd' to look for a shidduch ,if you whant to finish press 'z' : "))

# and type(pressing)==int

while pressing != "z":
    if pressing == "a":
        new_men()
    elif pressing == "b":
        new_women()
    elif pressing == "C":
        delete()
    elif pressing == "d":
        look_for()
    else:
        print("Enter 'a' or 'b' or 'c' or 'd' or 'z' only")
    print("if you whant to finish press 'z"
          "'")
    pressing = (input("Enter 'a' to add a man, enter 'b' to add a woman, enter 'c' to delete someone, enter 'd' to look for a shidduch ,if you whant to finish press 'z' : "))

print("Thank you! We wish you find your shidduch!!")



temp=int(input("if you want to del your 'filtered_men.txt' press 1 else if you want to del your 'filtered_women.txt' press 2 else if you want to del your 'filtered_women.txt'and  'filtered_men.txt' press 3"))
if temp==1:
    dellfile("filtered_men.txt")
elif temp==2:
    dellfile("filtered_women.txt")
elif temp==3:
    dellfile("filtered_men.txt")
    dellfile("filtered_women.txt")
else:
    print("we are sorry, you didnt press a good number")

























