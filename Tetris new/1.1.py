
import tkinter as tk


cell_size = 30
C = 12
R = 20
height = R * cell_size
width = C * cell_size

FPS = 200  

SHAPES = {
    "O": [(-1, -1), (0, -1), (-1, 0), (0, 0)],
    "S": [(-1, 0), (0, 0), (0, -1), (1, -1)],
    "T": [(-1, 0), (0, 0), (0, -1), (1, 0)],
    "I": [(0, 1), (0, 0), (0, -1), (0, -2)],
    "L": [(-1, 0), (0, 0), (-1, -1), (-1, -2)],
    "J": [(-1, 0), (0, 0), (0, -1), (0, -2)],
    "Z": [(-1, -1), (0, -1), (0, 0), (1, 0)],
}

SHAPESCOLOR = {
    "O": "blue",
    "S": "red",
    "T": "yellow",
    "I": "green",
    "L": "purple",
    "J": "orange",
    "Z": "Cyan",
}


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


def draw_cells(canvas, c, r, cell_list, color="#CCCCCC"):

    for cell in cell_list:
        cell_c, cell_r = cell
        ci = cell_c + c
        ri = cell_r + r

        if 0 <= c < C and 0 <= r < R:
            draw_cell_by_cr(canvas, ci, ri, color)


win = tk.Tk()
canvas = tk.Canvas(win, width=width, height=height, )
canvas.pack()

draw_blank_board(canvas)


def draw_block_move(canvas, block, direction=[0, 0]):

    shape_type = block['kind']
    c, r = block['cr']
    cell_list = block['cell_list']

    draw_cells(canvas, c, r, cell_list)

    dc, dr = direction
    new_c, new_r = c+dc, r+dr
    block['cr'] = [new_c, new_r]
    draw_cells(canvas, new_c, new_r, cell_list, SHAPESCOLOR[shape_type])


a_block = {
    'kind': 'O',
    'cell_list': SHAPES['O'],
    'cr': [3, 3]
}

draw_block_move(canvas, a_block)


def game_loop():
    win.update()

    down = [0, 1]
    draw_block_move(canvas, a_block, down)

    win.after(FPS, game_loop)

win.update()
win.after(FPS, game_loop)


win.mainloop()