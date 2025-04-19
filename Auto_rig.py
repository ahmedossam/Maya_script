import maya.cmds as cmds    #Python ,open maya 2 ,pymel (speed down)
def Auto_rig():
    """
    This function creates a circle controller for each joint in the scene, 
    groups the circle, and parents it to the joint.
    """
    # Get all joints in the scene
    all_jnts = cmds.ls(type="joint")
    Group = []

    for jnt in all_jnts:
        loc = cmds.xform(jnt, q=True, t=True, ws=True)
        circ = cmds.circle(n=f"{jnt}_Cntr", nr=[0, 1, 0])[0]
        grp = cmds.group(circ, n=circ + "_grp")
        cmds.setAttr(f"{grp}.t", *loc)
        cmds.parentConstraint(circ, jnt, mo=True)
        Group.append(grp)

    # Reverse the list so parenting goes from top to bottom
    #Group.reverse()

    # Chain-parent each group
    for i in range(len(Group) - 1):
        cmds.parent(Group[i + 1], Group[i])

    # Parent the top-most group to world
    cmds.parent(Group[0], world=True)
    
windows=cmds.window('Auto Rig',w=300,h=300)
cmds.columnLayout(adjustableColumn=True)
cmds.text(label='Auto Rig')
cmds.button(label='Auto Rig',c='Auto_rig()')
cmds.showWindow(windows)