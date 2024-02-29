#Author's names are: Therese Burns ans Allison Macrowski
import turtle
riley= turtle.Turtle()
riley.width(5)
riley.speed(0)
def draw_star(color):
    for side in range(5):
        riley.color(color)
        riley.forward(100)
        riley.right(144)
        
def moodstar():
    x=input("How are you today?\n")
    if x=="happy":
        draw_star("pink")
    elif x=="sad":
        draw_star("blue")
    elif x=="sleepy":
        draw_star("green")
    elif x=="angry":
        draw_star("red")

moodstar()    
moodstar()    
moodstar()
moodstar()
