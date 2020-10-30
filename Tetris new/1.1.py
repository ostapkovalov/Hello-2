
import tkinter as tk

cell_size = 30
C = 12
R = 20
height = R * cell_size
width = C * cell_size


def draw_cell_by_cr(canvas, c, r, color="#CCCCCC"):
    x0 = c * cell_size
    y0 = r * cell_size
    x1 = c * cell_size + cell_size
    y1 = r * cell_size + cell_size
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=2)

def draw_blank_board(canvas):
    for ri in range(R):
        for ci in range(C):
            draw_cell_by_cr(canvas, ci, ri)


win = tk.Tk()
canvas = tk.Canvas(win, width=width, height=height, )
canvas.pack()

draw_blank_board(canvas)

win.mainloop()
