import maya.cmds as cmds    #Python ,open maya 2 ,pymel (speed down)
import maya.mel as mel #   maya spesfic commands
import maya.OpenMaya as om #much faster than cmds   
cube=cmds.polyCube(n="Hello_Cube")  
controller=cmds.circle(n="Hello_Cube_Controller")  
cmds.group(controller[0],n="Hello_Cube_Controller_Group")  
cmds.parent(cube,controller)



                #I first starting with printing each linea a
                # nd see what is the type of grp and try to make as 
                # list so i create list and appened each grp created
                #  and all grop are pened i loop based on the location intdex 

 
	