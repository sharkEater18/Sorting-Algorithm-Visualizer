ORANGE = '#f24900'
LIGHT_GREEN = '#02ed12'
LIGHT_BLUE = '#00c3ff'
BLACK = '#000000'
WHITE = '#ffffff'
DEEP_PINK = '#ed025c'
GREY = '#a19292'
FRIENDLY_BLACK = '#483b52'

import time


max_time = 0.256
swap_count = 0

def quick_sort(arr, draw_array, speed_input, pauseBool):
    global swap_count
    swap_count = 0
    l, r = 0, len(arr) - 1
    quick_sort_alg(arr, l, r, draw_array, speed_input, pauseBool)
    colorArray = [LIGHT_GREEN for _ in range(len(arr))]
    draw_array(arr, colorArray, swap_count)
    print(arr)

def quick_sort_alg(arr, l, r, draw_array, speed_input, pauseBool):
    if l >= r: return
    pi = partition(arr, l, r, draw_array, speed_input, pauseBool)
    quick_sort_alg(arr, l, pi - 1, draw_array, speed_input, pauseBool)
    quick_sort_alg(arr, pi + 1, r, draw_array, speed_input, pauseBool)
    
def partition(arr, l, r, draw_array, speed_input, pauseBool):
    global swap_count
    
    pi = arr[r]
    i = l
    
    # draw_array(arr, color_array_helper(l, r, i, i, len(arr), False), swap_count)
    # time.sleep(max_time - (speed_input * max_time / 100))
    
    for j in range(l, r):
        if arr[j] < pi:
            
            draw_array(arr, color_array_helper(l, r, i, j, len(arr), True), swap_count)
            time.sleep(max_time - (speed_input * max_time / 100))
            
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            swap_count += 1
            
        draw_array(arr, color_array_helper(l, r, i, j, len(arr), False), swap_count)
        time.sleep(max_time - (speed_input * max_time / 100))
        
    draw_array(arr, color_array_helper(l, r, i, r, len(arr), False), swap_count)
    time.sleep(max_time - (speed_input * max_time / 100))
    
    arr[i], arr[r] = arr[r], arr[i]
    swap_count += 1
    
    # colorArray = [LIGHT_GREEN for _ in range(len(arr))]
    # draw_array(arr, colorArray, swap_count)
    
    return i

def color_array_helper(l, r, i, curr, n, swap):
    colorArray = [None for _ in range(n)]
    for x in range(n):
        if x >= l and x <= r:  colorArray[x] = WHITE # colorArray.append(WHITE)
        else:  colorArray[x] = DEEP_PINK # colorArray.append(DEEP_PINK)
        
        if x == i: colorArray[x] = GREY
        
        elif x == r: colorArray[x] = FRIENDLY_BLACK
        
        elif x == curr: colorArray[x] = LIGHT_BLUE
        
        if swap and (x == curr or x == i): colorArray[x] = ORANGE
    
    assert len(colorArray) == n
    return colorArray
        