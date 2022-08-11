import random

random_number = random.randint(0,5)
# print(random_number)
rand = random.random()* 100
# print(rand)
lst = ["star plus", "ccd","chichi"]
choice = random.choice(lst)
print(choice)
import sklearn


from emoji import emojize
print(emojize(":thumbs_up:"))
import emojis
emojified = emojis.encode("There is a :snake: in my boot")
print(emojified)
print(emojize(":snake:"))
print(emojis.encode(":heart::heart::snake::heart:"))

# This will import urlopen
# class from urllib module


from urllib.request import urlopen

page = urlopen("http://geeksforgeeks.org/")

# Fetches the code
# of the web page
content = page.read()

print(content)

# This will import turtle module
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


# Turtle to draw a spiral
def drawSpiral(myTurtle, linelen):
    myTurtle.forward(linelen)
    myTurtle.right(90)
    drawSpiral(myTurtle, linelen - 10)


drawSpiral(myTurtle, 80)
myWin.exitonclick()




import wikipedia
print(wikipedia.summary("Debugging", sentences = 2))
