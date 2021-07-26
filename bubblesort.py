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

def bubble_sort(arr, draw_array, speed_input, pauseBool):
    global swap_count
    swap_count = 0
    bubble_sort_alg(arr, draw_array, speed_input, pauseBool)
    
def bubble_sort_alg(arr, draw_array, speed_input, pauseBool):
    
    global swap_count
    
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            swap = False
            if j + 1 < n and arr[j + 1] < arr[j]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                swap_count += 1
                swap = True
                
            colorArray = []    
            for x in range(n):
                if x == j or x == j + 1 and not swap: colorArray.append(LIGHT_BLUE)
                elif swap and x == j + 1: colorArray.append(FRIENDLY_BLACK)
                elif x > n - i - 1: colorArray.append(LIGHT_GREEN)
                else: colorArray.append(DEEP_PINK)
            draw_array(arr,colorArray,swap_count)
            time.sleep(max_time - (speed_input * max_time / 100))
        
        
    colorArray = [LIGHT_GREEN for _ in range(len(arr))]
    draw_array(arr, colorArray, swap_count)