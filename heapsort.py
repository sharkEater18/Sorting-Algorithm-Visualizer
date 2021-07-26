"""
For heap sort first the given list is converted to max heap, onece the max heap is formed
we get a tree where for every parent its children are smaller than it. Thus on swapping
the first and last element of the tree (or list) repetatively, the list is sorted. One question
may arise why max heap is not formed again, well once the max heap is formed then after swapping
only heapify is enough to formed the next max heap with reduced nodes.
"""

ORANGE = '#f24900'
LIGHT_GREEN = '#02ed12'
LIGHT_BLUE = '#00c3ff'
BLACK = '#000000'
WHITE = '#ffffff'
DEEP_PINK = '#ed025c'

import time

max_time = 0.256
swap_count = 0
done_max_heap = False # Keep a boolean to check whwther max-heap build is over or not

def heap_sort(arr, draw_array, speed_input, pauseBool):
    global swap_count
    swap_count = 0
    heap_sort_alg(arr, draw_array, speed_input, pauseBool)

def heap_sort_alg(arr, draw_array, speed_input, pauseBool):
    global done_max_heap
    done_max_heap = False
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, draw_array, speed_input, pauseBool)
    
    # After max heap is formed, the list is coloued 'orange' 
    done_max_heap = True   
    colorArray = [ORANGE for _ in range(n)]
    draw_array(arr, colorArray, swap_count)
    
    
    time.sleep(2)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, draw_array, speed_input, pauseBool)
    
    # Finally color the array with green
    colorArray = [LIGHT_GREEN for _ in range(len(arr))]
    draw_array(arr, colorArray, swap_count)
    
def heapify(arr, n, i, draw_array, speed_input, pauseBool):
    
    global done_max_heap
    global swap_count
    
    # Booleans for left and right child if they are the largest
    largest_changed_left, largest_changed_right = False, False
    
    largest, l, r = i, 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]: 
        largest = l
        largest_changed_left = True
    if r < n and arr[r] > arr[largest]: 
        largest = r
        largest_changed_right = True
    
    if largest != i: swap_count += 1
    
    # Remember 'n' reduces, so use len(arr) for coloring purposes
    colorArray = []    
    for x in range(len(arr)):
        # Color the parent with light blue
        if x == i: colorArray.append(LIGHT_BLUE)
        
        # Coloring black and white according to left and right child
        if x == largest and largest != i:
            if largest_changed_left and not largest_changed_right: colorArray.append(BLACK)
            else: colorArray.append(WHITE)
        # After max heap is formaed now the sorting happens from the last elements, n is reduced size
        if done_max_heap and x >= n - 2: colorArray.append(LIGHT_GREEN)
        else: colorArray.append(DEEP_PINK)
    draw_array(arr,colorArray,swap_count)
    time.sleep(max_time - (speed_input * max_time / 100))
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, draw_array, speed_input, pauseBool)
    
    