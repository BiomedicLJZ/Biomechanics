#Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
import semmov

%matplotlib qt5

#Create a points x y z for each articulation
#Head
head_x = 5
head_y = 0
head_z = 20
#Neck
neck_x = 5
neck_y = 0
neck_z = 18
#Shoulders
R_shoulder_x = 5
R_shoulder_y = 2
R_shoulder_z = 17.6
L_shoulder_x = 5
L_shoulder_y = -2
L_shoulder_z = 17.6
#Core
core_x = 5
core_y = 0
core_z=16
#Elbows
R_elbow_x = 5
R_elbow_y = 2
R_elbow_z = 15
L_elbow_x = 5
L_elbow_y = -2
L_elbow_z = 15
#Wrist
R_wrist_x = 5
R_wrist_y = 2
R_wrist_z = 13
L_wrist_x = 5
L_wrist_y = -2
L_wrist_z = 13
#Hands
R_hand_x = 5
R_hand_y = 2
R_hand_z = 11
L_hand_x = 5
L_hand_y = -2
L_hand_z = 11
#Center Hip
C_hip_x = 5
C_hip_y = 0
C_hip_z = 13
#Hips
R_hip_x = 5
R_hip_y = 1.5
R_hip_z = 12
L_hip_x = 5
L_hip_y = -1.5
L_hip_z = 12
#Knees
R_knee_x = 5
R_knee_y = 1.5
R_knee_z = 9
L_knee_x = 5
L_knee_y = -1.5
L_knee_z = 9
#Ankles
R_ankle_x = 5
R_ankle_y = 1.5
R_ankle_z = 6
L_ankle_x = 5
L_ankle_y = -1.5
L_ankle_z = 6
#Heels
R_heel_x=4.9
R_heel_y=1.5
R_heel_z=5.5
L_heel_x=4.9
L_heel_y=-1.5
L_heel_z=5.5
#Feet
R_foot_x = 5.5
R_foot_y = 1.5
R_foot_z = 5.5
L_foot_x = 5.5
L_foot_y = -1.5
L_foot_z = 5.5
#References
xref=5
yref=8
zref=5.5



#Create Segment vectors

X=[xref,head_x,neck_x,R_shoulder_x,L_shoulder_x,core_x,R_elbow_x,L_elbow_x,R_wrist_x,L_wrist_x,R_hand_x,L_hand_x,C_hip_x,R_hip_x,L_hip_x,R_knee_x,L_knee_x,R_ankle_x,R_heel_x,L_ankle_x,L_heel_x,R_foot_x,L_foot_x]
Y=[yref,head_y,neck_y,R_shoulder_y,L_shoulder_y,core_y,R_elbow_y,L_elbow_y,R_wrist_y,L_wrist_y,R_hand_y,L_hand_y,C_hip_y,R_hip_y,L_hip_y,R_knee_y,L_knee_y,R_ankle_y,R_heel_y,L_ankle_y,L_heel_y,R_foot_y,L_foot_y]
Z=[zref,head_z,neck_z,R_shoulder_z,L_shoulder_z,core_z,R_elbow_z,L_elbow_z,R_wrist_z,L_wrist_z,R_hand_z,L_hand_z,C_hip_z,R_hip_z,L_hip_z,R_knee_z,L_knee_z,R_ankle_z,R_heel_z,L_ankle_z,L_heel_z,R_foot_z,L_foot_z]



#Create 3D plot
fig = plt.figure()
ax= fig.add_subplot(111, projection='3d')
ax.scatter(X,Y,Z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
#Legends for each articulation
#ax.text(xref,yref,zref,'Ref')
ax.text(head_x,head_y,head_z,'Head')
ax.text(neck_x,neck_y,neck_z,'Neck')
ax.text(R_shoulder_x,R_shoulder_y,R_shoulder_z,'R_shoulder')
ax.text(L_shoulder_x,L_shoulder_y,L_shoulder_z,'L_shoulder')
ax.text(core_x,core_y,core_z,'Core')
ax.text(R_elbow_x,R_elbow_y,R_elbow_z,'R_elbow')
ax.text(L_elbow_x,L_elbow_y,L_elbow_z,'L_elbow')
ax.text(R_wrist_x,R_wrist_y,R_wrist_z,'R_wrist')
ax.text(L_wrist_x,L_wrist_y,L_wrist_z,'L_wrist')
ax.text(R_hand_x,R_hand_y,R_hand_z,'R_hand')
ax.text(L_hand_x,L_hand_y,L_hand_z,'L_hand')
ax.text(C_hip_x,C_hip_y,C_hip_z,'C_hip')
ax.text(R_hip_x,R_hip_y,R_hip_z,'R_hip')
ax.text(L_hip_x,L_hip_y,L_hip_z,'L_hip')
ax.text(R_knee_x,R_knee_y,R_knee_z,'R_knee')
ax.text(L_knee_x,L_knee_y,L_knee_z,'L_knee')
ax.text(R_ankle_x,R_ankle_y,R_ankle_z,'R_ankle')
ax.text(L_ankle_x,L_ankle_y,L_ankle_z,'L_ankle')
ax.text(R_heel_x,R_heel_y,R_heel_z,'R_heel')
ax.text(L_heel_x,L_heel_y,L_heel_z,'L_heel')
ax.text(R_foot_x,R_foot_y,R_foot_z,'R_foot')
ax.text(L_foot_x,L_foot_y,L_foot_z,'L_foot')
#Create lines between each articulation
ax.plot(xref, yref, zref, 'o')
ax.plot([head_x,neck_x],[head_y,neck_y],[head_z,neck_z],"r")
ax.plot([neck_x,R_shoulder_x],[neck_y,R_shoulder_y],[neck_z,R_shoulder_z])
ax.plot([neck_x,L_shoulder_x],[neck_y,L_shoulder_y],[neck_z,L_shoulder_z])
ax.plot([neck_x,core_x],[neck_y,core_y],[neck_z,core_z])
ax.plot([R_shoulder_x,R_elbow_x],[R_shoulder_y,R_elbow_y],[R_shoulder_z,R_elbow_z])
ax.plot([L_shoulder_x,L_elbow_x],[L_shoulder_y,L_elbow_y],[L_shoulder_z,L_elbow_z])
ax.plot([R_elbow_x,R_wrist_x],[R_elbow_y,R_wrist_y],[R_elbow_z,R_wrist_z])
ax.plot([L_elbow_x,L_wrist_x],[L_elbow_y,L_wrist_y],[L_elbow_z,L_wrist_z])
ax.plot([R_wrist_x,R_hand_x],[R_wrist_y,R_hand_y],[R_wrist_z,R_hand_z])
ax.plot([L_wrist_x,L_hand_x],[L_wrist_y,L_hand_y],[L_wrist_z,L_hand_z])
ax.plot([core_x,C_hip_x],[core_y,C_hip_y],[core_z,C_hip_z])
ax.plot([C_hip_x,R_hip_x],[C_hip_y,R_hip_y],[C_hip_z,R_hip_z])
ax.plot([C_hip_x,L_hip_x],[C_hip_y,L_hip_y],[C_hip_z,L_hip_z])
ax.plot([R_hip_x,R_knee_x],[R_hip_y,R_knee_y],[R_hip_z,R_knee_z])
ax.plot([L_hip_x,L_knee_x],[L_hip_y,L_knee_y],[L_hip_z,L_knee_z])
ax.plot([R_knee_x,R_ankle_x],[R_knee_y,R_ankle_y],[R_knee_z,R_ankle_z])
ax.plot([L_knee_x,L_ankle_x],[L_knee_y,L_ankle_y],[L_knee_z,L_ankle_z])
ax.plot([R_ankle_x,R_heel_x],[R_ankle_y,R_heel_y],[R_ankle_z,R_heel_z])
ax.plot([L_ankle_x,L_heel_x],[L_ankle_y,L_heel_y],[L_ankle_z,L_heel_z])
ax.plot([R_ankle_x,R_foot_x],[R_ankle_y,R_foot_y],[R_ankle_z,R_foot_z])
ax.plot([L_ankle_x,L_foot_x],[L_ankle_y,L_foot_y],[L_ankle_z,L_foot_z])
ax.set_aspect("equal",adjustable='box')
plt.show()

#Calculate the length of all segments
head2neck=math.sqrt((head_x-neck_x)**2+(head_y-neck_y)**2+(head_z-neck_z)**2)
neck2R_shoulder=math.sqrt((neck_x-R_shoulder_x)**2+(neck_y-R_shoulder_y)**2+(neck_z-R_shoulder_z)**2)
neck2L_shoulder=math.sqrt((neck_x-L_shoulder_x)**2+(neck_y-L_shoulder_y)**2+(neck_z-L_shoulder_z)**2)
neck2core=math.sqrt((neck_x-core_x)**2+(neck_y-core_y)**2+(neck_z-core_z)**2)
core2C_hip=math.sqrt((core_x-C_hip_x)**2+(core_y-C_hip_y)**2+(core_z-C_hip_z)**2)
Torso=head2neck+neck2core+core2C_hip
R_shoulder2R_elbow=math.sqrt((R_shoulder_x-R_elbow_x)**2+(R_shoulder_y-R_elbow_y)**2+(R_shoulder_z-R_elbow_z)**2)
R_elbow_R_wrist=math.sqrt((R_elbow_x-R_wrist_x)**2+(R_elbow_y-R_wrist_y)**2+(R_elbow_z-R_wrist_z)**2)
R_wrist2R_hand=math.sqrt((R_wrist_x-R_hand_x)**2+(R_wrist_y-R_hand_y)**2+(R_wrist_z-R_hand_z)**2)
R_arm=R_shoulder2R_elbow+R_elbow_R_wrist+R_wrist2R_hand
L_shoulder2L_elbow=math.sqrt((L_shoulder_x-L_elbow_x)**2+(L_shoulder_y-L_elbow_y)**2+(L_shoulder_z-L_elbow_z)**2)
L_elbow2L_wrist=math.sqrt((L_elbow_x-L_wrist_x)**2+(L_elbow_y-L_wrist_y)**2+(L_elbow_z-L_wrist_z)**2)
L_wrists2L_hand=math.sqrt((L_wrist_x-L_hand_x)**2+(L_wrist_y-L_hand_y)**2+(L_wrist_z-L_hand_z)**2)
L_arm=L_shoulder2L_elbow+L_elbow2L_wrist+L_wrists2L_hand
R_hip2R_knee=math.sqrt((R_hip_x-R_knee_x)**2+(R_hip_y-R_knee_y)**2+(R_hip_z-R_knee_z)**2)
R_knee2R_ankle=math.sqrt((R_knee_x-R_ankle_x)**2+(R_knee_y-R_ankle_y)**2+(R_knee_z-R_ankle_z)**2)
R_ankle2R_foot=math.sqrt((R_ankle_x-R_foot_x)**2+(R_ankle_y-R_foot_y)**2+(R_ankle_z-R_foot_z)**2)
R_leg=R_hip2R_knee+R_knee2R_ankle+R_ankle2R_foot
L_hip2L_knee=math.sqrt((L_hip_x-L_knee_x)**2+(L_hip_y-L_knee_y)**2+(L_hip_z-L_knee_z)**2)
L_knee2L_ankle=math.sqrt((L_knee_x-L_ankle_x)**2+(L_knee_y-L_ankle_y)**2+(L_knee_z-L_ankle_z)**2)
L_ankle2L_foot=math.sqrt((L_ankle_x-L_foot_x)**2+(L_ankle_y-L_foot_y)**2+(L_ankle_z-L_foot_z)**2)
L_leg=L_hip2L_knee+L_knee2L_ankle+L_ankle2L_foot


#Move the right arm 45 degrees
R_elbow_z=R_shoulder_z+(R_shoulder2R_elbow*math.sin(math.radians(-45)))
R_elbow_x=R_shoulder_x+(R_shoulder2R_elbow*math.cos(math.radians(-45)))
R_wrist_z=R_elbow_z+(R_elbow_R_wrist*math.sin(math.radians(-45)))
R_wrist_x=R_elbow_x+(R_elbow_R_wrist*math.cos(math.radians(-45)))
R_hand_z=R_wrist_z+(R_wrist2R_hand*math.sin(math.radians(-45)))
R_hand_x=R_wrist_x+(R_wrist2R_hand*math.cos(math.radians(-45)))


#Change the arm to horizontal
R_elbow_z=R_shoulder_z+(R_shoulder2R_elbow*math.sin(math.radians(0)))
R_elbow_x=R_shoulder_x+(R_shoulder2R_elbow*math.cos(math.radians(0)))
R_wrist_z=R_elbow_z+(R_elbow_R_wrist*math.sin(math.radians(0)))
R_wrist_x=R_elbow_x+(R_elbow_R_wrist*math.cos(math.radians(0)))
R_hand_z=R_wrist_z+(R_wrist2R_hand*math.sin(math.radians(0)))
R_hand_x=R_wrist_x+(R_wrist2R_hand*math.cos(math.radians(0)))

R_elbow_z=R_shoulder_z+(R_shoulder2R_elbow*math.sin(math.radians(-90)))
R_elbow_x=R_shoulder_x+(R_shoulder2R_elbow*math.cos(math.radians(-90)))
R_wrist_z=R_elbow_z+(R_elbow_R_wrist*math.sin(math.radians(-90)))
R_wrist_x=R_elbow_x+(R_elbow_R_wrist*math.cos(math.radians(-90)))
R_hand_z=R_wrist_z+(R_wrist2R_hand*math.sin(math.radians(-90)))
R_hand_x=R_wrist_x+(R_wrist2R_hand*math.cos(math.radians(-90)))



articulations=[head,neck,torso,L_shoulder,R_shoulder,L_elbow,R_elbow,L_wrist,R_wrist,L_hand,R_hand,L_hip,R_hip,L_knee,R_knee,L_ankle,R_ankle,L_foot,R_foot,L_heel,R_heel]

angles=np.linspace(0,90,5)
fig = plt.figure(1,dpi=300,frameon=False,)
ax=fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
origin= np.array([R_hip_x,R_hip_z])
v1= np.array([R_knee_x,R_knee_z])
v2= np.array([R_ankle_x,R_ankle_z])
v3= np.array([R_foot_x,R_foot_z])
v4= np.array([R_heel_x,R_heel_z])
vec=np.vstack((origin,v1,v2,v3,v4))
vec_rot=np.zeros(np.shape(vec))
for angle in angles:
    R=np.array([[math.cos(math.radians(angle)),math.sin(math.radians(angle))],[-math.sin(math.radians(angle)),math.cos(math.radians(angle))]])
    for i in range(np.shape(vec)[0]):
        vec_rot[i,:]=vec_rot[i,:]-origin
        vec_rot[i,:]=np.dot(R,vec_rot[i,:])
        vec_rot[i,:]=vec_rot[i,:]+origin
    ax.cla()
    R_hip_x=vec_rot[0,0]
    R_hip_z=vec_rot[0,1]
    R_knee_x=vec_rot[1,0]
    R_knee_z=vec_rot[1,1]
    R_ankle_x=vec_rot[2,0]
    R_ankle_z=vec_rot[2,1]
    R_foot_x=vec_rot[3,0]
    R_foot_z=vec_rot[3,1]
    R_heel_x=vec_rot[4,0]
    R_heel_z=vec_rot[4,1]
    articulations=[head,neck,torso,L_shoulder,R_shoulder,L_elbow,R_elbow,L_wrist,R_wrist,L_hand,R_hand,L_hip,R_hip,L_knee,R_knee,L_ankle,R_ankle,L_foot,R_foot,L_heel,R_heel]
