import numpy as np
import pandas as pd
import kineticstoolkit as ktk
import matplotlib.pyplot as plt
import os
import tkinter as tk, tkinter.filedialog as fd

root=tk.Tk()
root.withdraw()
path=fd.askopenfilename(title='Select file',filetypes=[('text files','.txt'),('all files','.*')])

#Read txt file
with open(path, 'r') as f:
    data = f.readlines()
    f.close()
#Create a list with the data from marker 1 and marker 2
d1 = data[4:339]
d2 = data[341:676]
d3 = data[678:]

framerate=60
n_markers=3
n_frames=335

#Separate the list in 4 lists, one for time and one for each axis x y z
time = [float(d1[i].split()[0]) for i in range(n_frames)]
time = np.array(time)
x1 = [float(d1[i].split()[1]) for i in range(n_frames)]
y1 = [float(d1[i].split()[2]) for i in range(n_frames)]
x2 = [float(d2[i].split()[1]) for i in range(n_frames)]
y2 = [float(d2[i].split()[2]) for i in range(n_frames)]
x3 = [float(d3[i].split()[1]) for i in range(n_frames)]
y3 = [float(d3[i].split()[2]) for i in range(n_frames)]
# Create a list of zeros for z
z1 = [0 for i in range(n_frames)]
z2 = [0 for i in range(n_frames)]
z3 = [0 for i in range(n_frames)]
ones = [1 for i in range(n_frames)]

#Create an array with time tih shape(n_frames,)
time_array = np.array(time)
#Create an array with the data of the markers with shape(n_frames,4)
marker1 = np.array([x1,y1,z1,ones])
marker1 = marker1.T
marker2 = np.array([x2,y2,z2,ones])
marker2 = marker2.T
marker3 = np.array([x3,y3,z3,ones])
marker3 = marker3.T

#Normalize the data of the markers 
marker1 = marker1/1000
marker2 = marker2/1000
marker3 = marker3/1000



ts= ktk.TimeSeries()
ts.time = time_array
ts.data["marker1"] = marker1
ts.data["marker2"] = marker2
ts.data["marker3"] = marker3

%matplotlib qt5

ktk.Player(ts)

interconnections =dict()

interconnections["Limb"]={
    "Color":[1,0,0],
    "Links":[
        ["marker1","marker2","marker3"]
    ]
}
ktk.Player(ts,interconnections=interconnections)

df=ts.to_dataframe()
df.to_csv("df_c3d.csv")
#Corregir falta de 0 en el tiempo
ktk.write_c3d("df_c3d",ts)