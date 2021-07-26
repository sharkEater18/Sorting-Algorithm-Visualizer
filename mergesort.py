"""
In merge sort the array is divided till the size is 'one', then the small chunks are 
merged (conquer step).
"""




ORANGE = '#f24900'
LIGHT_GREEN = '#02ed12'
LIGHT_BLUE = '#00c3ff'
BLACK = '#000000'
WHITE = '#ffffff'
DEEP_PINK = '#ed025c'
GREY = '#a19292'


import time


max_time = 0.256
swap_count = 0

def merge_sort(arr, draw_array, speed_input, pauseBool):
    global swap_count
    swap_count = 0
    l, r = 0, len(arr) - 1
    merge_sort_alg(arr, l, r, draw_array, speed_input, pauseBool)
    print(arr)

def merge_sort_alg(arr, l, r, draw_array, speed_input, pauseBool):
    if l >= r: return
    m = (l + r) // 2
    merge_sort_alg(arr, l, m, draw_array, speed_input, pauseBool)
    merge_sort_alg(arr, m + 1, r, draw_array, speed_input, pauseBool)
    merge(arr, l, m, r, draw_array, speed_input, pauseBool)
    
def merge(arr, l, m, r, draw_array, speed_input, pauseBool):
    colorArray = []
    global swap_count
    for i in range(len(arr)):
        # Left list is colored orange
        if i >= l and i < m:
            colorArray.append(ORANGE)
            
        # Right list is colored light blue
        elif i >= m + 1 and i <= r:
            colorArray.append(LIGHT_BLUE)
            
        # Mid is colored grey
        elif i == m: 
            colorArray.append(GREY)
        else:
            colorArray.append(DEEP_PINK)

    draw_array(arr, colorArray, swap_count)
    time.sleep(max_time - (speed_input * max_time / 100))
    
    left = arr[l : m + 1]
    right = arr[m + 1 : r + 1]
    i, j, k = 0, 0, l
    while i < len(left) and j < len(right):
        
        # Merging from the left list
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            swap_count += 1
            for x in range(l, k):
                colorArray[x] = LIGHT_GREEN
            draw_array(arr, colorArray, swap_count)
            time.sleep(max_time - (speed_input * max_time / 100))
            
        # Merging from the right list
        else:
            arr[k] = right[j]
            j += 1
            swap_count += 1
            for x in range(l, k):
                colorArray[x] = LIGHT_GREEN
            draw_array(arr, colorArray, swap_count)
            time.sleep(max_time - (speed_input * max_time / 100))
        k += 1
        
    # Merging remaining left list
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        swap_count += 1
        for x in range(l, k):
            colorArray[x] = LIGHT_GREEN
        draw_array(arr, colorArray, swap_count)
        time.sleep(max_time - (speed_input * max_time / 100))
    
    # Merging remaining right list
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        swap_count += 1
        for x in range(l, k):
            colorArray[x] = LIGHT_GREEN
        draw_array(arr, colorArray, swap_count)
        time.sleep(max_time - (speed_input * max_time / 100))