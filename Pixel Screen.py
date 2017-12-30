
from turtle import Turtle
import csv

colours = ['blue','red','yellow','green','orange','purple']
turtles = []
names = []

def MakeScreen():
    for row in range(10):
        print("Setting up Column:"+str(row+1))
        for column in range(10):
            name = str(row)+str(column) #makes a unique name for the coordinates
            names.append(name) #adds the name to an array
            name = Turtle() #makes it into a turtle
            name.speed(0)
            turtles.append(name) #adds the turtle to a different array
            name.shape('square') #makes it a square (pixel)
            name.shapesize(3) #makes it the correct size
            name.penup()
            name.goto(row*60-300,column*60-250) #goes to its coordinates
        

MakeScreen()

if input("Enter M for manual of F for file: ")[0].upper() == "M": #takes the uppercase version of the first letter of the choice
    while True:
        rowchoice = input("\nEnter row: ")
        columnchoice = input("Enter column: ")
        colourchoice = input("Enter colour: ")

        turtles[names.index(str(rowchoice)+str(columnchoice))].color(colourchoice) #finds the matching turtle to the name and makes it the chosen colour
        
else:
    filename = input("\nEnter filename with .csv extension: ")
    with open(filename) as file:
        pixelreader = csv.DictReader(file)
        rowno = 0
        for row in pixelreader: #reads every line of the file
            for columnno in range(1,11): #for every column in the file
                print("Scanning row:"+str(rowno+1)+" Column:"+str(columnno)) #shows the location of the coordinate (colour) in the file
                turtles[names.index(str(columnno-1)+str(10-rowno-1))].color(row[str(columnno)]) #makes the relevant turtle that colour
            rowno += 1
