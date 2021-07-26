# def partition(arr, l, r):
#     pi = arr[r]
#     i = l
#     for j in range(l, r):
#         if arr[j] < pi:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#     arr[i], arr[r] = arr[r], arr[i]
#     return i

# def quick_sort(arr, l, r):
#     if l >= r: return
#     pi = partition(arr, l, r)
#     quick_sort(arr, l, pi - 1)
#     quick_sort(arr, pi + 1, r)

# def fun(arr):
#     l = 0
#     r = len(arr) - 1
#     quick_sort(arr, l, r)
   
# arr = [10, 31, 1, 2, 3, 14, 5, 16, 19]
# # quick_sort(arr, 0, len(arr) - 1)
# fun(arr)
# print(arr)
        
        
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
speeds_name = ('Very Slow', 'Slow', 'Medium', 'Fast', 'Very Fast')
speed_dict = {
        'Very Slow': 5,
        'Slow': 20,
        'Medium': 30,
        'Fast': 60,
        'Very Fast': 90
}
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
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
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


print(normalize_array(generate_random_array(10, 0, 100)))

# root.mainloop()
