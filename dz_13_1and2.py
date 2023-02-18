import random
import string
import time

int_list = {}
for i in range(5000):
    int_list[i] = random.randint(0, 1000)

float_list = {}
for i in range(5000):
    float_list[i] = round(random.uniform(0.1, 100.0), 2)

str_list = {}
for i in range(5000):
    str_list[i] = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))



def sort_int_list(int_list):
    sorted_list = sorted(int_list.items(), key=lambda x: x[1])
    return dict(sorted_list)



def calculate_avg_time(sort_func, data_list, num_iterations):
    total_time = 0
    for i in range(num_iterations):
        start_time = time.time()
        sorted_list = sort_func(data_list)
        end_time = time.time()
        total_time += (end_time - start_time)
    avg_time = total_time / num_iterations
    return avg_time



num_iterations = 10
avg_time = calculate_avg_time(sort_int_list, int_list, num_iterations)
sorted_int_list = sort_int_list(int_list)
print(f"Sorted int_list dictionary: {sorted_int_list}")
print(f"Average running time of sorting algorithm: {avg_time:.6f} seconds")