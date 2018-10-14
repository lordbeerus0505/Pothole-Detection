import csv
import numpy 
import pandas

def give_locations(input_timestamp):
    input_timestamp = input_timestamp//1000
    # print(input_timestamp)

    dataframe = pandas.read_csv("Flight02_gps.csv", header=0, usecols=lambda x: x in ['timestamp','lat', 'lon'])
    dataset = dataframe.values

    timestamp = dataset[:,0]
    lat = dataset[:,1]/10000000
    lon = dataset[:,2]/10000000

    locations = []

    for i in range(len(timestamp)):
        if abs(input_timestamp-timestamp[i]) <110000:
            locations.append((lat[i],lon[i]))
            break
        else:
            continue
    return locations



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
    timestamp=[]
    counter=1
    t1=0
    max=0
    min=10000000000000
    abc=0
    for row in csv_reader:
        # count+=1
        c1=c
        # if abc==0:
        #     abc+=1
        #     continue
        # if counter>20000:
        c=int(row[0])
        if c>c1: #new timestamp
            count+=1
            print("Timestamp:",c)
        if count>14400:
            t1+=1
            timestamp.append(c)
            if t1>1024:
                break
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
                counter+=1
            else:
                # print(f'\t{row[5]} altitude')
                if float(row[2])<min:
                    min=float(row[2])
                elif float(row[2])>max:
                    max=float(row[2])
                x.append(float(row[2]))
                y.append(float(row[3]))
                z.append(float(row[4]))
                # lat.append(int(row[2]))
                # lon.append(int(row[3]))
                line_count += 1
                counter+=1
                
        # else:
        #     counter+=1
    print(f'Processed {line_count} lines.')

    # for i in range(1,1052):
    #     print("altitude:",altitude[i],"latitude",lat[i],"longitude",lon[i])
    value=[]
    for i in range(0,2106,2):
        value.append(i/10)
    # print(type(lat[1]))


    import matplotlib.pyplot as plt
    import numpy as np
    plt.subplot(2,1,1)
    plt.scatter(y,x)
    plt.subplot(2,1,2)
    plt.scatter(z,x)
    # plt.axis([0, 210, 0, 75000])
    plt.ylabel('x')
    # plt.yscale('linear')
    plt.show()

    print("Volume assuming its a hemispherical area = ",2*np.pi*(max-min)**3/3)
    print("Timestamp =",timestamp[0])
    [(lat,lon)]=give_locations(timestamp[0])
    print("Latitude",lat,"Longitude",lon)
    display(timestamp[0]/600)

import tkinter as tk
from PIL import ImageTk, Image

def display(n):

	window = tk.Tk()
	window.title("Join")
	window.geometry("600x800")
	window.configure(background='grey')

	path = str(n)+".JPEG"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = tk.Label(window, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")

	#Start the GUI
	window.mainloop()