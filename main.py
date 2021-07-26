# Author: scjt18
# Date:

import sys

orig_stdin = sys.stdin
orig_stdout = sys.stdout
f_i = open("input.txt", "r")
f_o = open("output.txt", "w")
sys.stdin = f_i
sys.stdout = f_o

#################################################################################################

"""YOUR CODE GOES HERE, CREATE AN INPUT FILE"""

# --------------------------------------------------------------------
VIOLET = "#9803fc"
ORANGE = "#f24900"
LIGHT_GREEN = "#02ed12"
LIGHT_BLUE = "#00c3ff"
BLACK = "#000000"
WHITE = "#ffffff"
DEEP_PINK = "#ed025c"
LIGHT_PINK = "#fc03a9"
LIGHT_YELLOW = "#f4fc03"
#################################
WIDTH, HEIGHT = 1130, 650
array = []
algos = (
    "Bubble Sort",
    "Merge Sort",
    "Quick Sort",
    "Selection Sort",
    "Heap Sort",
    "Insertion Sort",
)
sizes = (3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
speeds_name = ("Very Slow", "Slow", "Medium", "Fast", "Very Fast")
speed_dict = {"Very Slow": 2, "Slow": 10, "Medium": 30, "Fast": 60, "Very Fast": 90}
speeds = (1, 2, 5, 10, 20, 30, 40, 50)
pauseBool = False
# --------------------------------------------------------------------

# --------------------------------------------------------------------
import tkinter as tk
from tkinter import font
from tkinter import ttk
import random
import numpy as np
import sys, time, os
import math

import mergesort as mg_sort
import selectionsort as sl_sort
import bubblesort as bbl_sort
import heapsort as hp_sort
import insertionsort as in_sort
import quicksort as qk_sort

# --------------------------------------------------------------------

# --------------------------------------------------------------------
root = tk.Tk()
algo_canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
algo_canvas.pack()
# --------------------------------------------------------------------

# --------------------------------------------------------------------
def generate_random_array(array_size, low=10, high=100):
    arr = [np.unique(random.randint(low, high)) for i in range(array_size)]
    array = []
    for i in range(array_size):
        array.append(arr[i][0])
    return array


def normalize_array(arr):
    return [i / max(arr) for i in arr]


def draw_array(array, array_color, swap_count):

    algo_canvas.delete("all")
    n = len(array)

    can_ht = 390
    can_wdt = 930

    bar_width = can_wdt / (n + 1)
    spacing = 4
    offset_x = 20
    normalised_array = normalize_array(array)

    for i, h in enumerate(normalised_array):
        # top - left
        x0 = i * bar_width + offset_x + spacing
        y0 = can_ht - h * 330

        # bottom-right
        x1 = (i + 1) * bar_width + offset_x
        y1 = can_ht

        algo_canvas.create_rectangle(x0, y0, x1, y1, fill=array_color[i])
        algo_canvas.create_text(
            x0 + 2,
            y0,
            anchor="sw",
            text=str(array[i]),
            font=("Cascadia Code", 300 // n, font.BOLD),
            fill=array_color[i],
        )

    ##display swapCount
    swapCountLabel = tk.Label(
        algo_canvas,
        text="#Swap Count : " + str(swap_count),
        fg="white",
        bg="black",
        font=("Cascadia Font", 15),
    )
    algo_canvas.create_window(1025, 40, height=50, window=swapCountLabel)

    root.update_idletasks()


def generate_main():
    global array
    n = int(size_combo.get())
    array = generate_random_array(array_size=n)
    # array = normalize_array(array)
    array_color = [VIOLET for i in range(n)]
    swap_count = 0
    draw_array(array, array_color, swap_count)


def start_sort():
    global array
    select = select_combo.get()
    if select == "Merge Sort":
        mg_sort.merge_sort(
            array, draw_array, int(speed_dict[speed_combo.get()]), pauseBool
        )

    elif select == "Selection Sort":
        sl_sort.selection_sort(
            array, draw_array, int(speed_dict[speed_combo.get()]), pauseBool
        )

    elif select == "Bubble Sort":
        bbl_sort.bubble_sort(
            array, draw_array, int(speed_dict[speed_combo.get()]), pauseBool
        )

    elif select == "Heap Sort":
        hp_sort.heap_sort(
            array, draw_array, int(speed_dict[speed_combo.get()]), pauseBool
        )

    elif select == "Insertion Sort":
        in_sort.insertion_sort(
            array, draw_array, int(speed_dict[speed_combo.get()]), pauseBool
        )

    elif select == "Quick Sort":
        qk_sort.quick_sort(
            array, draw_array, int(speed_dict[speed_combo.get()]), pauseBool
        )


# --------------------------------------------------------------------

# --------------------------------------------------------------------
ui_frame = tk.Frame(root, bg=LIGHT_PINK, bd=20)
ui_frame.place(relwidth=1, relheight=0.35)

title_label = tk.Label(
    ui_frame,
    text="Sorting Algorithm Visualizer",
    font=("Cascadia Code", 20),
    bg="#03fca1",
)
title_label.place(relx=0.25, relwidth=0.5, relheight=0.18)

select_label = tk.Label(
    ui_frame, text="Algorithm:", font=("Cascadia Code", 20), bg="#03c2fc"
)
select_label.place(relx=0.01, rely=0.35, relwidth=0.17, relheight=0.18)

select_combo = ttk.Combobox(ui_frame, values=algos, font=("Cascadia Code", 20))
select_combo.place(relx=0.20, rely=0.35, relwidth=0.25, relheight=0.18)

size_label = tk.Label(
    ui_frame, text="Set Size:", font=("Cascadia Code", 20), bg="#03c2fc"
)
size_label.place(relx=0.01, rely=0.58, relwidth=0.17, relheight=0.18)

# size_entry = tk.Entry(ui_frame, font = ('Cascadia Code', 20))
# size_entry.place(relx = 0.20, rely = 0.58, relwidth = 0.25, relheight = 0.18)

size_combo = ttk.Combobox(ui_frame, values=sizes, font=("Cascadia Code", 20))
size_combo.place(relx=0.20, rely=0.58, relwidth=0.25, relheight=0.18)

speed_label = tk.Label(
    ui_frame, text="Set Speed:", font=("Cascadia Code", 20), bg="#03c2fc"
)
speed_label.place(relx=0.01, rely=0.8, relwidth=0.17, relheight=0.18)

# speed_entry = tk.Entry(ui_frame, font = ('Cascadia Code', 20))
# speed_entry.place(relx = 0.20, rely = 0.8, relwidth = 0.25, relheight = 0.18)

speed_combo = ttk.Combobox(ui_frame, values=speeds_name, font=("Cascadia Code", 20))
speed_combo.place(relx=0.20, rely=0.8, relwidth=0.25, relheight=0.18)

generate_button = tk.Button(
    ui_frame,
    text="Generate",
    font=("Cascadia Code", 20),
    bg="red",
    command=generate_main,
)
generate_button.place(relx=0.7, rely=0.4, relwidth=0.25, relheight=0.2)

sort_button = tk.Button(
    ui_frame, text="Sort", font=("Cascadia Code", 20), bg="blue", command=start_sort
)
sort_button.place(relx=0.7, rely=0.65, relwidth=0.25, relheight=0.2)

# --------------------------------------------------------------------

# --------------------------------------------------------------------
algo_canvas = tk.Canvas(root, bg=LIGHT_YELLOW, bd=20)
algo_canvas.place(rely=0.35, relwidth=1, relheight=1)

# --------------------------------------------------------------------

# --------------------------------------------------------------------
root.mainloop()
# --------------------------------------------------------------------

####################################################################################################
sys.stdin = orig_stdin
sys.stdout = orig_stdout
f_i.close()
f_o.close()
