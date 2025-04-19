import maya.cmds as cmds    #Python ,open maya 2 ,pymel (speed down)
import maya.mel as mel #   maya spesfic commands
import maya.OpenMaya as om #much faster than cmds   
cube=cmds.polyCube(n="Hello_Cube")  
controller=cmds.circle(n="Hello_Cube_Controller")  
cmds.group(controller[0],n="Hello_Cube_Controller_Group")  
cmds.parent(cube,controller)


all_jnts = cmds.ls(type="joint")
Group = []
for jnt in all_jnts:
	loc = cmds.xform(jnt,q=1,t=1,ws=1)
	circ = cmds.circle(n=f"{jnt}_Cntr",nr = [0,1,0])[0]
	grp = cmds.group(circ,n=circ+"_grp")
	Group.append(grp)
    Group.reverse()
	cmds.setAttr(f"{grp}.t",*loc)
	cmds.parentConstraint(circ,jnt,mo=1)
	parent = cmds.listRelatives(jnt,ap=1)
for i in Group:
    if i ==Group[0]:
        cmds.parent(i,None)
    else:
        cmds.parent(i,Group[0])
                #I first starting with printing each linea a
                # nd see what is the type of grp and try to make as 
                # list so i create list and appened each grp created
                #  and all grop are pened i loop based on the location intdex 

 
	