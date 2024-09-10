import turtle
import random
import time

myScreen = turtle.Screen()
myScreen.bgcolor("light green")
myScreen.title("Catch The Turtle")

t = turtle.Turtle()
t.color("green")
t.shape("turtle")
t.shapesize(2, 2)
t.penup()

t2 = turtle.Turtle()
t2.hideturtle()
t2.penup()
t2.goto(0, 250)

score = 0
remainingTime = 15
original_time = remainingTime # süreyi saklamak

def increase_score(x, y):
    global score
    score += 1

def move_turtle():
    global remainingTime
    if remainingTime > 0:
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        t.goto(x, y)
        myScreen.ontimer(move_turtle, 400)  
        
def update_timer():
    global remainingTime
    if remainingTime > 0:
        remainingTime -= 1
        t2.clear()
        t2.write(f"Süreniz: {remainingTime}, Skorunuz: {score}", font=("Arial", 24, "bold"), align="center")
        myScreen.ontimer(update_timer, 1000)  # Her saniye güncelleme
        if remainingTime == 1:
            time.sleep(1)
            t2.write(f"Süreniz: 0, Skorunuz: {score}", font=("Arial", 24, "bold"), align="center")
            t2.clear()
            t.home()
            t.hideturtle()
            t.write(f"Süreniz: {original_time}, Skorunuz: {score}", font=("Arial", 24, "bold"), align="center")

t.onclick(increase_score)

move_turtle() 
update_timer()

turtle.mainloop()
