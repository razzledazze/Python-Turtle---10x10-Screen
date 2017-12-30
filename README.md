# Python-Turtle---10x10-Screen
A 10x10 pixel screen created using Python and the turtle module, which can take information from a csv file to draw an image

To use the pixel screen code, either manually enter the colours in the program, or create a file for it to read.
An example file of a rocket ship shows the format. 
Every line must have ten comma separated colour values, of either red, blue, green, yellow, orange, or purple. 
The colours can also be hex values, in the format #0a0a0a with the hash and lower case letters. 
There should be ten lines of this format, underneath one line of 1,2,3,4,5,6,7,8,9,10 as column headers.

------------------------------
QUICK CREATOR
------------------------------
If you choose to use the quick creator tool, you can enter 5 different colours to utilise in your drawing, which are each assigned to a letter. You then input a row with the letter in place of the colour it represents.
e.g.
Enter colour A: Blue
Enter colour B: Red
Enter the row: a,a,a,a,b,b,b,a,a,a

The above use would write to the csv file:
blue,blue,blue,blue,red,red,red,blue,blue,blue

You then have to enter the csv file and remove the quotation marks from the start and end of each row, after which it will run perfectly with the pixel screen code as a file to read.
