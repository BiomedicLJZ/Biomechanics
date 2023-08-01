import numpy as np
import matplotlib.pyplot as plt
import math as m
import semmov as sm

%matplotlib qt5

head=sm.Articulation('head',5,0,20)
neck=sm.Articulation('neck',5,0,18)
torso=sm.Articulation('torso',5,0,16)
R_shoulder=sm.Articulation('R_shoulder',5,2,17.6)
L_shoulder=sm.Articulation('L_shoulder',5,-2,17.6)
L_elbow=sm.Articulation('L_elbow',5,-2,15)
R_elbow=sm.Articulation('R_elbow',5,2,15)
L_wrist=sm.Articulation('L_wrist',5,-2,13)
R_wrist=sm.Articulation('R_wrist',5,2,13)
L_hand=sm.Articulation('L_hand',5,-2,11)
R_hand=sm.Articulation('R_hand',5,2,11)
C_hip=sm.Articulation('C_hip',5,0,13)
L_hip=sm.Articulation('L_hip',5,-1.5,12)
R_hip=sm.Articulation('R_hip',5,1.5,12)
L_knee=sm.Articulation('L_knee',5,-1.5,10)
R_knee=sm.Articulation('R_knee',5,1.5,10)
L_ankle=sm.Articulation('L_ankle',5,-1.5,6)
R_ankle=sm.Articulation('R_ankle',5,1.5,6)
R_foot=sm.Articulation('R_foot',5.5,1.5,5)
L_foot=sm.Articulation('L_foot',5.5,-1.5,5)
L_heel=sm.Articulation('L_heel',4.5,-1.5,5)
R_heel=sm.Articulation('R_heel',4.5,1.5,5)

articulations=[head,neck,torso,L_shoulder,R_shoulder,L_elbow,R_elbow,L_wrist,R_wrist,L_hand,R_hand,C_hip,L_hip,R_hip,L_knee,R_knee,L_ankle,R_ankle,L_foot,R_foot,L_heel,R_heel]
connections=[[head,neck],[neck,torso],[torso,C_hip],[C_hip,L_hip],[C_hip,R_hip],[L_hip,L_knee],[R_hip,R_knee],[L_knee,L_ankle],[R_knee,R_ankle],[L_ankle,L_foot],[R_ankle,R_foot],[L_ankle,L_heel],[R_ankle,R_heel],[neck,L_shoulder],[neck,R_shoulder],[L_shoulder,L_elbow],[R_shoulder,R_elbow],[L_elbow,L_wrist],[R_elbow,R_wrist],[L_wrist,L_hand],[R_wrist,R_hand]]
fig=plt.figure()
sm.graph_connections(articulations,connections,fig)


#Rotate leg 
angles= np.linspace(0,45,5)
fig=plt.figure(1)
ax=fig.add_subplot(111,projection='3d')
ax.set_aspect('equal',adjustable='box')
origin=[R_hip.x,R_hip.z]
p1=[R_knee.x,R_knee.z]
p2=[R_ankle.x,R_ankle.z]
p3=[R_foot.x,R_foot.z]
p4=[R_heel.x,R_heel.z]
vec=np.vstack([origin,p1,p2,p3,p4])
for angle in angles:
    R=np.array([[np.cos(np.deg2rad(angle)),-np.sin(np.deg2rad(angle))],[np.sin(np.deg2rad(angle)),np.cos(np.deg2rad(angle))]])
    for i in range(np.shape(vec)[0]):
        vec[i]=vec[i]-origin
        vec[i]=np.dot(R,vec[i])
        vec[i]=vec[i]+origin
    ax.cla()
    R_hip.x=vec[0,0]
    R_hip.z=vec[0,1]
    R_knee.x=vec[1,0]
    R_knee.z=vec[1,1]
    R_ankle.x=vec[2,0]
    R_ankle.z=vec[2,1]
    R_foot.x=vec[3,0]
    R_foot.z=vec[3,1]
    R_heel.x=vec[4,0]
    R_heel.z=vec[4,1]
    L_hip.x=vec[0,0]
    L_hip.z=vec[0,1]
    L_knee.x=vec[1,0]
    L_knee.z=vec[1,1]
    L_ankle.x=vec[2,0]
    L_ankle.z=vec[2,1]
    L_foot.x=vec[3,0]
    L_foot.z=vec[3,1]
    L_heel.x=vec[4,0]
    L_heel.z=vec[4,1]
    sm.graph_connections(articulations,connections,fig)
    plt.pause(0.1)
    articulations=[head,neck,torso,L_shoulder,R_shoulder,L_elbow,R_elbow,L_wrist,R_wrist,L_hand,R_hand,C_hip,L_hip,R_hip,L_knee,R_knee,L_ankle,R_ankle,L_foot,R_foot,L_heel,R_heel]
    connections=[[head,neck],[neck,torso],[torso,C_hip],[C_hip,L_hip],[C_hip,R_hip],[L_hip,L_knee],[R_hip,R_knee],[L_knee,L_ankle],[R_knee,R_ankle],[L_ankle,L_foot],[R_ankle,R_foot],[L_ankle,L_heel],[R_ankle,R_heel],[neck,L_shoulder],[neck,R_shoulder],[L_shoulder,L_elbow],[R_shoulder,R_elbow],[L_elbow,L_wrist],[R_elbow,R_wrist],[L_wrist,L_hand],[R_wrist,R_hand]]
    sm.graph_connections(articulations,connections,fig)
    plt.pause(0.5)
#Rotate legs
angles= np.linspace(0,-45,5)
fig=plt.figure(1)
ax=fig.add_subplot(111,projection='3d')
ax.set_aspect('equal',adjustable='box')
origin=[R_knee.x,R_knee.z]
p1=[R_ankle.x,R_ankle.z]
p2=[R_foot.x,R_foot.z]
p3=[R_heel.x,R_heel.z]
vec=np.vstack([origin,p1,p2,p3])
for angle in angles:
    R=np.array([[np.cos(np.deg2rad(angle)),-np.sin(np.deg2rad(angle))],[np.sin(np.deg2rad(angle)),np.cos(np.deg2rad(angle))]])
    for i in range(np.shape(vec)[0]):
        vec[i]=vec[i]-origin
        vec[i]=np.dot(R,vec[i])
        vec[i]=vec[i]+origin
    ax.cla()
    R_knee.x=vec[0,0]
    R_knee.z=vec[0,1]
    R_ankle.x=vec[1,0]
    R_ankle.z=vec[1,1]
    R_foot.x=vec[2,0]
    R_foot.z=vec[2,1]
    R_heel.x=vec[3,0]
    R_heel.z=vec[3,1]
    L_knee.x=vec[0,0]
    L_knee.z=vec[0,1]
    L_ankle.x=vec[1,0]
    L_ankle.z=vec[1,1]
    L_foot.x=vec[2,0]
    L_foot.z=vec[2,1]
    L_heel.x=vec[3,0]
    L_heel.z=vec[3,1]
    sm.graph_connections(articulations,connections,fig)
    plt.pause(0.1)
    articulations=[head,neck,torso,L_shoulder,R_shoulder,L_elbow,R_elbow,L_wrist,R_wrist,L_hand,R_hand,C_hip,L_hip,R_hip,L_knee,R_knee,L_ankle,R_ankle,L_foot,R_foot,L_heel,R_heel]
    connections=[[head,neck],[neck,torso],[torso,C_hip],[C_hip,L_hip],[C_hip,R_hip],[L_hip,L_knee],[R_hip,R_knee],[L_knee,L_ankle],[R_knee,R_ankle],[L_ankle,L_foot],[R_ankle,R_foot],[L_ankle,L_heel],[R_ankle,R_heel],[neck,L_shoulder],[neck,R_shoulder],[L_shoulder,L_elbow],[R_shoulder,R_elbow],[L_elbow,L_wrist],[R_elbow,R_wrist],[L_wrist,L_hand],[R_wrist,R_hand]]
    sm.graph_connections(articulations,connections,fig)
    plt.pause(0.5)
