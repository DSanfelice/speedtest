from os import read
import matplotlib.pyplot as plt
import numpy as np

#open the file and read the contents, line by line
file = open('speedtest.txt')
read_lines = file.readlines()

#find every line with a 'D' in it
split_list = []
for i in read_lines:
    if i[0] == 'D':
        split_list.append(i)

#split the lines by the whitespace
speed = []
for i in split_list:
    i = i.split()
    speed.append(i)

#create a list with just the internet speed as a string
speed_final = []
for i in speed:
    speed_final.append(i[1])

#convert string to integer for final list conversion
speed_num = []
for i in speed_final:
    i = float(i)
    speed_num.append(i)

#DO THE SAME FOR THE TIME
#open the file and read the contents, line by line
file = open('speedtest_time.txt')
read_lines = file.readlines()

#loop through the text file for times
time_list = []
for i in read_lines:
    i = int(i)
    time_list.append(i)

while len(time_list) != len(speed_num):
    if len(time_list) > len(speed_num):
        time_list.pop()
    elif len(speed_num) > len(time_list):
        speed_num.pop()


#MATPLOTLIB convert to numpy array
y = np.array(speed_num)
x = np.array(time_list)

#Plot the MAtplotlib
plt.plot(x, y)
plt.ylabel("MB/S")
plt.xlabel("Time")
plt.show()