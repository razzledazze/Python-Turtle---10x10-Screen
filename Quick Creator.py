#quick creator

name = input("Enter the name of the new file WITH .csv extension: ")
a = input("\nEnter colour A: ")
b = input("Enter colour B: ")
c = input("Enter colour C: ")
d = input("Enter colour D: ")
e = input("Enter colour E: ")
values = [a,b,c,d,e]
namevalues = ["a","b","c","d","e"]
final = ""
header = ""

import csv

with open(name, "w") as csvfile:
    csvout = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in range(1,11):
        header += str(row)+"," #writes the header line of numbers
    csvout.writerow([header])
    
    for row in range(10):
        row = input("Enter the row of ten values, separated by commas but no spaces: ")
        temprow = ""
        for i in row: #for each letter in the previous input
            if i != ",": #as long as it isn't a comma:
                if i in namevalues: #if it relates to a colour chosen at the start:
                    temprow += values[namevalues.index(i)] + "," #append the colour to the row
                else:
                    temprow += '#ffffff' + "," #otherwise write white

        csvout.writerow([temprow]) #write the whole row
    
    


print(final)
