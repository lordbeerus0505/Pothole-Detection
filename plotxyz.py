import numpy  # Import numpy
import pandas 
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *
from time import sleep


def makeFig():  # Create a function that makes our desired plot
      # plt.ylim(0,1000)                #Set the limit on the y axis
    plt.title('Sensor data')  # Set the title
    plt.grid(True)  # Set The grid
    plt.ylabel('Depth')  # Label the y axis
    plt.plot(accelX, 'ro-', label='Raw X Acceleration')  # Set the line plot
    ax = plt.gca()
    ax.set_ylim([-50,50])
    # plt.ylim(-20, 1000)
    plt.legend(loc='upper left')
    plt2 = plt.twinx()  # Create a new object of plt2
    plt2.plot(accelY, 'b^-', label='Y variation')
    # plt2.ylim(-20,1000)
    plt2.legend(loc='center right')
    plt2.ticklabel_format(useOffset=False)  # Compel matplotlib not to autoscale
    plt3 = plt.twinx()
    # plt3.plot(z, 'go-', label='Raw Z Acceleration')
    # plt3.legend(loc='upper right')
    # plt3.ylim(0, 1000)
# dataframe = pandas.read_csv("dataset/Flight02_imu.csv", header=0, usecols=lambda x: x in ['timestamp','acc_x', 'acc_y','acc_z'])
# dataframe = pandas.read_csv("dataset/Flight02_pointcloud.csv", header=0, usecols=lambda x: x in ['timestamp','x', 'y','z'])
# dataset = dataframe.values

# accelX = dataset[:,1]
# accelY = dataset[:,2]
# accelZ = dataset[:,3]

accelX = []
accelY = []
accelZ = []

# X = dataset[20000:28217,1]
# Y = dataset[20000:28217,2]
# Z = dataset[20000:28217,3]

plt.ion()  # Tell matplotlib you want interactive mode to plot live data
cnt = 0
import csv

with open('Flight02_pointcloud.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    counter=0
    altitude=[]
    x=[]
    y=[]
    z=[]
    altitude.append(500)
    lat=[]
    lon=[]
    count=1
    c=0
    counter=1
    for row in csv_reader:
        # count+=1
        c1=c
        if counter>20000:
            c=int(row[0])
            if c>c1: #new timestamp
                count+=1
                print("Timestamp:",c)
            if count>2:
                break
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
                counter+=1
            else:
                # print(f'\t{row[5]} altitude')
                x.append(float(row[2]))
                y.append(float(row[3]))
                z.append(float(row[4]))
                # lat.append(int(row[2]))
                # lon.append(int(row[3]))
                line_count += 1
                counter+=1
                makeFig()
                
        else:
            counter+=1


cnt = 0

for i in range(len(x)):
    xAxis = float(x[i])  # Convert first element to int insert in xAxis
    yAxis = float(y[i])  # Convert second element to int insert in yAxis
    zAxis = float(z[i])  # Convert third element to int insert in zAxis
    print ( xAxis, ",", yAxis, ",", zAxis)
    accelX.append(xAxis)  # Build our x axis array by appending to accelX
    accelY.append(yAxis)  # Build our y axis array by appending to accelY
    accelZ.append(zAxis)  # Build our z axis array by appending to accelZ
    drawnow(makeFig)  # Call drawnow to update our live graph
    drawnow(makeFig)
    plt.pause(.000001)
    # sleep(10)
    cnt = cnt+1
    if(cnt > 50):
        accelX.pop(0)
        accelY.pop(0)
        accelZ.pop(0)
