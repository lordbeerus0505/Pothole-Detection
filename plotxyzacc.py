import numpy  # Import numpy
import pandas 
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *
from time import sleep

dataframe = pandas.read_csv("dataset/Flight02_imu.csv", header=0, usecols=lambda x: x in ['timestamp','acc_x', 'acc_y','acc_z'])
dataset = dataframe.values


accelX = []
accelY = []
accelZ = []

X = dataset[0::20,1]
Y = dataset[0::20,2]
Z = dataset[0::20,3]

plt.ion()  # Tell matplotlib you want interactive mode to plot live data
cnt = 0


def makeFig():  # Create a function that makes our desired plot
    plt.title('Sensor data')  # Set the title
    plt.grid(True)  # Set The grid
    plt.ylabel('Axis Acceleration')  # Label the y axis
    plt.plot(accelX, 'ro-', label='Raw X Acceleration')  # Set the line plot
    ax = plt.gca()
    ax.set_ylim([-50,50])               #Set the limit on the y axis
    plt.legend(loc='upper left')
    plt2 = plt.twinx()  # Create a new object of plt2
    plt2.plot(accelY, 'b^-', label='Raw Y Acceleration')
    plt2.legend(loc='center right')
    plt2.ticklabel_format(useOffset=False)  # Compel matplotlib not to autoscale
    plt3 = plt.twinx()
    plt3.plot(accelZ, 'go-', label='Raw Z Acceleration')
    plt3.legend(loc='upper right')

cnt = 0

for i in range(len(X)):
    xAxis = float(X[i])  # Convert first element to int insert in xAxis
    yAxis = float(Y[i])  # Convert second element to int insert in yAxis
    zAxis = float(Z[i])  # Convert third element to int insert in zAxis
    print ( xAxis, ",", yAxis, ",", zAxis)
    accelX.append(xAxis)  # Build our x axis array by appending to accelX
    accelY.append(yAxis)  # Build our y axis array by appending to accelY
    accelZ.append(zAxis)  # Build our z axis array by appending to accelZ
    drawnow(makeFig)  # Call drawnow to update our live graph
    plt.pause(.000001)
    cnt = cnt+1
    if(cnt > 50):
        accelX.pop(0)
        accelY.pop(0)
        accelZ.pop(0)
