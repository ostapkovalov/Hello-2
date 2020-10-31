
import tkinter as tk
from tkinter import messagebox
import random

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


def draw_board(canvas,block_list):
    for ri in range(R):
        for ci in range(C):
            cell_type = block_list[ri][ci]
            if cell_type:
                draw_cell_by_cr(canvas,ci,ri,SHAPESCOLOR[cell_type])
            else:
                draw_cell_by_cr(canvas,ci,ri)
def check_row_complete(row):
    for cell in row:
        if cell=='':
            return False
    return True

def draw_cells(canvas, c, r, cell_list, color="#CCCCCC"):

    for cell in cell_list:
        cell_c, cell_r = cell
        ci = cell_c + c
        ri = cell_r + r

        if 0 <= c < C and 0 <= r < R:
            draw_cell_by_cr(canvas, ci, ri, color)

score = 0
window.title("SCORES:%s"% score)

def check_and_clear():
    has_complete_row = False
    for ri in range(len(block_list)):
        if check_row_complete(block_list[ri]):
            has_complete_row=True
            if ri>0:
                for cur_ri in range(ri,0,-1):
                    block_list[cur_ri]=block_list[cur_ri[:]]
                block_list[0]=[''for j in range (C)]
            else:
                block_list[ri] = ['' for j in range(C)]
                global score
                score+=10
    if has_complete_row:
        draw_board(canvas,block_list)
        window.title("SCORES: %s"%score)




window = tk.Tk()
canvas = tk.Canvas(window, width=width, height=height, )
canvas.pack()


block_list=[]
for i in range(R):
    i_row=[''for j in range(C)]
    block_list.append((i_row))
draw_board(canvas,block_list)

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
    window.update()
    global current_block
    if current_block is None:
        new_block = generate_new_block()
        # The newly generated Tetris must be drawn at the generated location
        draw_block_move(canvas, new_block)
        current_block = new_block
        if not check_move(current_block, [0, 0]):
            messagebox.showinfo("Game Over!", "Your Score is %s" % score)
            window.destroy()
            return
    else:
        if check_move(current_block, [0, 1]):
            draw_block_move(canvas, current_block, [0, 1])
        else:
            # Unable to move, add to block_list
            save_block_to_list(current_block)
            current_block = None

    check_and_clear()

    window.after(FPS, game_loop)