import turtle
from PIL import Image

def draw_branch(t, branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0 or branch_length <= 0:
        return

    # Draw the main branch
    t.forward(branch_length)

    # Draw the left subtree
    t.left(angle_left)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
    t.right(angle_left)  # Restore original angle

    # Draw the right subtree
    t.right(angle_right)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
    t.left(angle_right)  # Restore original angle

    # Go back to the starting position
    t.backward(branch_length)

def save_canvas_as_image(canvas, filename):
    # Save the canvas as a postscript file
    canvas.postscript(file=f"{filename}.ps", colormode='color')
    
    # Use Pillow to convert the .ps file to .png
    img = Image.open(f"{filename}.ps")
    img.save(f"{filename}.png")

def main():
    # Get user input
    angle_left = float(input("Enter the left branch angle (degrees): "))
    angle_right = float(input("Enter the right branch angle (degrees): "))
    starting_length = float(input("Enter the starting branch length (pixels): "))
    depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    # Setup the turtle environment
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)  # Point upwards
    t.penup()
    t.goto(0, -300)  # Start at the bottom of the screen
    t.pendown()

    # Draw the tree
    draw_branch(t, starting_length, angle_left, angle_right, depth, reduction_factor)

    # Save the drawing as an image
    canvas = turtle.getcanvas()
    save_canvas_as_image(canvas, "tree_output")

    # Notify the user
    print("Tree saved as 'tree_output.png' in the current directory.")

    # Finish
    screen.mainloop()

if __name__ == "__main__":
    main()
