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

def selection_sort(arr, draw_array, speed_input, pauseBool):
    global swap_count
    swap_count = 0
    selection_sort_alg(arr, draw_array, speed_input, pauseBool)
    
def selection_sort_alg(arr, draw_array, speed_input, pauseBool):
    
    global swap_count
    n = len(arr)
    for i in range(n):
        min_id = i
        # Stroing the initial minimum (assumed)
        tmp = copy.deepcopy(min_id)
        for j in range(i + 1, n):
            if arr[j] < arr[min_id]: 
                min_id = j
                swap_count += 1
                
            colorArray = []    
            for x in range(n):
                if x == tmp: colorArray.append(FRIENDLY_BLACK)
                elif x < i: colorArray.append(LIGHT_GREEN)
                elif x == j: colorArray.append(LIGHT_BLUE)
                elif x == min_id: colorArray.append(GREY)
                else: colorArray.append(DEEP_PINK)
            draw_array(arr,colorArray,swap_count)
            time.sleep(max_time - (speed_input * max_time / 100))
        
        arr[min_id], arr[i] = arr[i], arr[min_id]
        swap_count += 1
        colorArray = [LIGHT_GREEN if x<=i else DEEP_PINK for x in range(len(arr))]
        draw_array(arr,colorArray,swap_count)
        time.sleep(max_time - (speed_input * max_time / 100))
        
        
        
    colorArray = [LIGHT_GREEN for _ in range(len(arr))]
    draw_array(arr, colorArray, swap_count)