#This program calculate standard deviation and standard error by putting your data.

import math

def calculate_stats(data_list):
    n = len(data_list)
    if n == 0: return 0, 0

    mean = sum(data_list) / n

    square_total = sum((i - mean) ** 2 for i in data_list)
    variance = square_total / (n-1)

    std_dev = math.sqrt(variance)  #Calulation standard deviation

    std_err = std_dev / math.sqrt(n)  #Calculate standard error

    return std_dev, std_err, mean

num_of_data = int(input("How many data do you have?: "))
while num_of_data < 0:
    num_of_data = int(input("Invalid. How many data do you have?: "))

data_list = []
for i in range(num_of_data):
    data = float(input(f"Enter data No{i + 1}: "))
    data_list.append(data)

sd, sr, av = calculate_stats(data_list)

raw_sig_fig = input("Please enter significant figure if you would like to use. If don't, don't enter anything."
                    "(It will automatically 4 significant figure.): ")

if raw_sig_fig == "": 
    sig_fig = 4
else: 
    sig_fig = int(raw_sig_fig)


print("-" *40)
print(f"Standard Diviation: {sd:.{sig_fig}}")
print(f"Standard Error: {sr:.{sig_fig}}")
print(f"Mean: {av:.{sig_fig}}")
print("-" * 40)




