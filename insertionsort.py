ORANGE = '#f24900'
LIGHT_GREEN = '#02ed12'
LIGHT_BLUE = '#00c3ff'
BLACK = '#000000'
WHITE = '#ffffff'
DEEP_PINK = '#ed025c'
GREY = '#a19292'
FRIENDLY_BLACK = '#483b52'



import time
import copy

max_time = 0.256
swap_count = 0

def insertion_sort(arr, draw_array, speed_input, pauseBool):
    global swap_count
    swap_count = 0
    insertion_sort_alg(arr, draw_array, speed_input, pauseBool)
    
def insertion_sort_alg(arr, draw_array, speed_input, pauseBool):
    
    global swap_count
    n = len(arr)
    for i in range(1, n):
        k = arr[i]
        j = i - 1
        
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            
            colorArray = []    
            for x in range(n):
                if x == i: colorArray.append(FRIENDLY_BLACK)
                if x == j: colorArray.append(LIGHT_BLUE)
                else: colorArray.append(DEEP_PINK)
                if i == n - 1 and x == j: colorArray.append(LIGHT_GREEN)
            
            draw_array(arr,colorArray,swap_count)
            time.sleep(max_time - (speed_input * max_time / 100))
            
            j -= 1
            
        arr[j + 1] = k
        
        
        
    colorArray = [LIGHT_GREEN for _ in range(len(arr))]
    draw_array(arr, colorArray, swap_count)