import turtle

def draw_tree(t, branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        return
    t.pencolor("brown" if depth > 4 else "green")
    t.pensize(depth)
    t.forward(branch_length)
    t.left(left_angle)
    draw_tree(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    t.right(left_angle)
    t.right(right_angle)
    draw_tree(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    t.left(right_angle)
    t.backward(branch_length)

def main():
    left_angle = int(input("Enter the angle for the left branch (e.g 20): "))
    right_angle = int(input("Enter the angle for the right branch (e.g 25): "))
    branch_length = int(input("Enter the initial branch length (e.g 100): "))
    depth = int(input("Enter the recursion depth (e.g 5): "))
    reduction_factor = float(input("Enter the reduction factor for branch length (e.g 0.7): "))
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Recursive Tree Pattern")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    draw_tree(t, branch_length, left_angle, right_angle, depth, reduction_factor)
    screen.mainloop()

if __name__ == "__main__":
    main()