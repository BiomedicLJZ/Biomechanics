import kineticstoolkit.lab as ktk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk as tk, filedialog as fd

%matplotlib qt5

#Create a point
p1=np.array([[2,2,5,1]])
origen=p1
p2=np.array([[10,2,3,1]])
#Create Rotation Matrix
T=ktk.geometry.create_transforms(seq='y',angles=[[45]],translations=[[0,0,0]],degrees=True)
#Apply the rotation matrix
p1_rotated=p1-origen
p2_rotated=p2-origen
p1_rotated=ktk.geometry.matmul(T,p1_rotated)
p2_rotated=ktk.geometry.matmul(T,p2_rotated)
p1_rotated=p1_rotated+origen
p2_rotated=p2_rotated+origen

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(p1[0,0],p1[0,1],p1[0,2],label="Punto 1",color="red")
ax.scatter(p2[0,0],p2[0,1],p2[0,2],label="Punto 2",color="blue")
ax.plot([p1[0,0],p2[0,0]],[p1[0,1],p2[0,1]],[p1[0,2],p2[0,2]],color="blue")
#Add te points to the origin
origin=np.array(
    [[0,0,0,1]])
ax.scatter(origin[0,0],origin[0,1],origin[0,2],label="Origen",color="black")
#Plot the axis from the origin
ax.plot([origin[0,0],25],[origin[0,1],0],[origin[0,2],0],color="black")
ax.plot([origin[0,0],0],[origin[0,1],25],[origin[0,2],0],color="black")
ax.plot([origin[0,0],0],[origin[0,1],0],[origin[0,2],25],color="black")
ax.text(25,0,0,"X")
ax.text(0,25,0,"Y")
ax.text(0,0,25,"Z")
#Scatter the rotated points
ax.scatter(p1_rotated[0,0],p1_rotated[0,1],p1_rotated[0,2],label="Punto 1 Rotado",color="green")
ax.scatter(p2_rotated[0,0],p2_rotated[0,1],p2_rotated[0,2],label="Punto 2 Rotado",color="orange")
ax.plot([p1_rotated[0,0],p2_rotated[0,0]],[p1_rotated[0,1],p2_rotated[0,1]],[p1_rotated[0,2],p2_rotated[0,2]],color="orange")

#Create a 5 point vector
vec=np.array([[1,1,1,1],[2,2,2,1],[3,3,3,1],[4,4,4,1],[5,5,5,1]])
#Scatter the points
ax.cla()
for i in range(0,vec.shape[0]):
    ax.scatter(vec[i,0],vec[i,1],vec[i,2],color="red")
T=ktk.geometry.create_transforms(seq='x',angles=[[90]],translations=[[0,0,0]],degrees=True)
#Apply the rotation matrix
vec_rotated=ktk.geometry.matmul(T,vec)
#Scatter the rotated points
for i in range(0,vec_rotated.shape[0]):
    ax.scatter(vec_rotated[i,0],vec_rotated[i,1],vec_rotated[i,2],color="blue")


#Plot a line from each point to the origin
for i in range(0,vec.shape[0]):
    ax.plot([vec[i,0],0],[vec[i,1],0],[vec[i,2],0],color="red")
for i in range(0,vec_rotated.shape[0]):
    ax.plot([vec_rotated[i,0],0],[vec_rotated[i,1],0],[vec_rotated[i,2],0],color="blue")

markers = ktk.read_c3d(
    ktk.doc.download("kinematics_racing_full.c3d")
)["Points"]

# Interconnect markers for easier visualization
interconnections = {
    "ArmR": {
        "Color": [1, 0.25, 0],
        "Links": [
            ["AcromionR", "MedialEpicondyleR"],
            ["AcromionR", "LateralEpicondyleR"],
            ["AcromionR", "OlecraneR"],
        ],
    },
    "ForearmR": {
        "Color": [1, 0.5, 0],
        "Links": [
            ["MedialEpicondyleR", "RadialStyloidR"],
            ["MedialEpicondyleR", "UlnarStyloidR"],
            ["LateralEpicondyleR", "RadialStyloidR"],
            ["LateralEpicondyleR", "UlnarStyloidR"],
            ["OlecraneR", "RadialStyloidR"],
            ["OlecraneR", "UlnarStyloidR"],
            ["UlnarStyloidR", "RadialStyloidR"],
        ],
    },
}

# Visualize in the player
ktk.Player(markers, interconnections=interconnections)

origin = markers.data["AcromionR"]

y = markers.data["AcromionR"] - 0.5 * (
    markers.data["LateralEpicondyleR"] + markers.data["MedialEpicondyleR"]
)

yz = markers.data["LateralEpicondyleR"] - markers.data["MedialEpicondyleR"]

frames = ktk.TimeSeries(time=markers.time)


frames.data["ArmR"] = ktk.geometry.create_frames(origin=origin, y=y, yz=yz)

ktk.Player(
    markers, frames, interconnections=interconnections
)

origin = markers.data["UlnarStyloidR"]

y = (
    0.5
    * (markers.data["LateralEpicondyleR"] + markers.data["MedialEpicondyleR"])
    - markers.data["UlnarStyloidR"]
)

yz = markers.data["RadialStyloidR"] - markers.data["UlnarStyloidR"]


frames.data["ForearmR"] = ktk.geometry.create_frames(origin=origin, y=y, yz=yz)

ktk.Player(
    markers, frames, interconnections=interconnections
)


arm_to_forearm = ktk.geometry.get_local_coordinates(
    frames.data["ForearmR"], frames.data["ArmR"]
)

arm_to_forearm

euler_angles = ktk.geometry.get_angles(arm_to_forearm, "ZXY", degrees=True)

euler_angles


angles = ktk.TimeSeries(time=markers.time)

angles.data["Elbow flexion"] = euler_angles[:, 0]
angles.data["Forearm pronation"] = euler_angles[:, 2]

angles = angles.add_data_info("Elbow flexion", "Unit", "deg")
angles = angles.add_data_info("Forearm pronation", "Unit", "deg")

angles.plot()

## 2nd Part

root = tk()
root.withdraw()
file_path = fd.askopenfilename(filetypes=[("C3D files", "*.c3d")], title="Select a C3D file")

markers = ktk.read_c3d(file_path)["Points"]
markers.data
connections= dict()
connections["Column"] = {
    "Color": [1, 0.25, 0],
    "Links": [
    ["CV7",'SJN','SXS','TV10']
    ]
}
connections["L_leg"] = {
    "Color": [0.55, 0.1, 0.65],
    "Links": [
    ['L_IAS','L_FTC','L_FLE','L_FAX','L_FAL','L_FCC','L_FM1','L_FM2','L_FM5'],
    ['L_FTC','L_FME','L_TTC','L_TAM','L_FCC','L_FM1','L_FM2','L_FM5']
    ]
}
connections["R_leg"] = {
    "Color": [1, 0.5, 0.5],
    "Links": [
    ['R_IAS','R_FTC','R_FLE','R_FAX','R_FAL','R_FCC','R_FM1','R_FM2','R_FM5'],
    ['R_FTC','R_FME','R_TTC','R_TAM','R_FCC','R_FM1','R_FM2','R_FM5']
    ]
}
ktk.Player(markers,up='z', interconnections=connections)

origin=markers.data['L_FLE']
y=markers.data["L_FLE"]-0.5*(markers.data['L_TAM']+markers.data['L_FAL'])
yz=markers.data['L_TAM']-markers.data['L_FAL']
frames = ktk.TimeSeries(time=markers.time)
frames.data['L_leg']=ktk.geometry.create_frames(origin=origin,y=y,yz=yz)

origin2=markers.data['L_IAS']
y2=markers.data["L_IAS"]-0.5*(markers.data['L_FME']+markers.data['L_FLE'])
yz2=markers.data['L_FME']-markers.data['L_FLE']
frames2 = ktk.TimeSeries(time=markers.time)
frames.data['L_Hipi']=ktk.geometry.create_frames(origin=origin2,y=y2,yz=yz2)

ktk.Player(markers,frames,up='z')

hip2knee=ktk.geometry.get_local_coordinates(frames.data['L_leg'],frames.data['L_Hipi'])
euler_angles = ktk.geometry.get_angles(hip2knee, "ZXY", degrees=True)
angles = ktk.TimeSeries(time=markers.time)
angles.data["Knee flexion"] = euler_angles[:, 0]
angles.data["Knee abduction"] = euler_angles[:, 1]
angles.data["Knee rotation"] = euler_angles[:, 2]
angles = angles.add_data_info("Knee flexion", "Unit", "deg")
angles = angles.add_data_info("Knee abduction", "Unit", "deg")
angles = angles.add_data_info("Knee rotation", "Unit", "deg")
angles.plot()