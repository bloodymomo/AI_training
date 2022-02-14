import turtle

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)



def tree(branchLen):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-15)
        t.left(30)
        tree(branchLen-15)
        t.left(30)
        tree(branchLen-15)
        t.right(30)
        t.backward(branchLen)

tree(60)
t.hideturtle()
turtle.done()