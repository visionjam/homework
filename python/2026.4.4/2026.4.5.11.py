import turtle as tt
MAX_LEVEL = 2
INITIAL_LENGTH = 500
def draw_square(length):
    for _ in range(4):
        tt.forward(length)
        tt.left(90)

def fractal(level,length,x,y):
    if level == 1:
        tt.penup()
        tt.goto(x, y)
        tt.pendown()
        draw_square(length)
        return
     
    new_length =length/3
    new_level =level-1
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            sub_x = x + i * new_length
            sub_y = y + j * new_length
            fractal(new_level, new_length, sub_x, sub_y)

def main():
    tt.speed(0)
    tt.hideturtle()
    tt.tracer(0, 0)
    tt.penup()
    tt.goto(-INITIAL_LENGTH / 2, -INITIAL_LENGTH / 2)
    tt.pendown()
    fractal(MAX_LEVEL,INITIAL_LENGTH,-INITIAL_LENGTH/2,-INITIAL_LENGTH/2)
    tt.update()
    tt.exitonclick()

main()