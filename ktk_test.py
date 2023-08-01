import kineticstoolkit.lab as ktk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk as tk, filedialog as fd

%matplotlib qt5


root=tk()
root.withdraw()
path=fd.askopenfilename(title='Select a C3D file',filetypes=[('C3D files','*.c3d'),('All files','*.*')])


c3d=ktk.read_c3d(path)
markers=c3d['Points']


ktk.Player(markers,up="z")