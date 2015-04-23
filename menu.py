import dw_camProjSet_v1_1
import mari_bridge
import RandomTile
import animatedSnap3D
import CornerPinFreeze
import MultiChannelCombine
import MultiChannelCombineSgtk
import MultiChannelSplit
import MultiChannelSplitSgtk

toolbar = nuke.menu('Nodes')
toolbar.addCommand( 'Random Tile', 'RandomTile.randomTile()','',icon='RandomTile.png')



##################### Andy's Custom Toolbar

usersToolbar = nuke.toolbar('CustomTools')
usersToolbar.addMenu('AndysTools', 'Crazy_Harry.jpg')
myMenu = usersToolbar.addMenu('AndysTools', 'Crazy_Harry.jpg')



######### Andy's Shuffle Solid Alpha

def ShuffleSolidAlpha():

    sh = nuke.createNode('Shuffle')
    sh.knob('alpha').setValue("white")
    sh.knob('label').setValue("Shuffle_Solid_Alpha")
    # enter your red, green, blue values here:
    r = 1
    g = 1
    b = 1 
    # close your eyes and just do it:
    hexColour = int('%02x%02x%02x%02x' % (r*255,g*255,b*255,1),16) 
    # now use is:
    sh['tile_color'].setValue( hexColour ) 


myMenu.addCommand('Shuffle_Solid_Alpha', 'ShuffleSolidAlpha()', 'shift+a')




######### Andy's Toggle Hide Input

def ToggleHideInput():

    for n in nuke.selectedNodes():
      if n["hide_input"].value()==1:
	  n["hide_input"].setValue(0)
      else:
	  n["hide_input"].setValue(1)



myMenu.addCommand('ToggleHideInput', 'ToggleHideInput()', 'shift+h')

######### Andy's Custom OCIO node with shortcut

def customOCIO():

    n = nuke.createNode('OCIOCDLTransform')
    # enter your red, green, blue values here:
    r = 0
    g = .75
    b = 1
    # close your eyes and just do it:
    hexColour = int('%02x%02x%02x%02x' % (r*255,g*255,b*255,1),16) 
    # now use is:
    n['tile_color'].setValue( hexColour ) 

######## Andy's Custom CornerPin animation helpers

myMenu.addCommand('CornerPin/Freeze_To', 'CornerPinFreeze.FreezeTo()')
myMenu.addCommand('CornerPin/Freeze_From', 'CornerPinFreeze.FreezeFrom()')
myMenu.addCommand('Colour/OCIOtx','customOCIO()', 'shift+o')

######## MultiChannel Combine and Split scripts

myMenu.addCommand('Scripts/MultiChannelCombine', 'MultiChannelCombine.MultiChannelCombine()')
myMenu.addCommand('Scripts/MultiChannelCombineSgtk', 'MultiChannelCombineSgtk.MultiChannelCombine()')

myMenu.addCommand('Scripts/MultiChannelSplit', 'MultiChannelSplit.MultiChannelSplit()')
myMenu.addCommand('Scripts/MultiChannelSplitSgtk', 'MultiChannelSplitSgtk.MultiChannelSplitSgtk()')

toolbar = nuke.menu("Nodes")

dwMenu = toolbar.addMenu("DW Tools", "dw_menu.png")

dwMenu.addCommand("Cameras/Camera Project Current Frame", "dw_camProjSet_v1_1.camProjSingle()", "shift+c", "dw_camProjCurFrame.png")
dwMenu.addCommand("Cameras/Camera Project Source", "dw_camProjSet_v1_1.camProjMultiple()", "ctrl+shift+c", "dw_camProjSource.png")


#####################


def clear_properties():
 
    for n in nuke.allNodes() + [nuke.root(), ]:
        n.hideControlPanel()
 
def autoBackdrop():


    
    i = 0
    for n in nuke.selectedNodes():
	i = i + 1
    if i == 0:
	bdName = nuke.getInput("Backdrop Name")
	bd = nuke.createNode("BackdropNode")
	bd.knob("name").setValue(bdName)
	bd.knob("tile_color").setValue(0x88888800)

    else:

	#create lists
	xposList = []
	yposList = []
    
	#add each node position to respective list
	for n in nuke.selectedNodes():
	    xposList.append(n.xpos())
	    yposList.append(n.ypos())

	#sort lists numerically
	xposList.sort()
	yposList.sort()

	#grab the min
	leftX = xposList[0]
	topY = yposList[0]

	#calculate difference between smallest and largest values
	if i == 1:
	    theWidth = 105
	    theHeight = 110
	else:
	    theWidth = (xposList[(len(xposList) - 1)] - xposList[0]) + 105
	    theHeight = (yposList[(len(yposList) - 1)] - yposList [0]) + 110

	#get Backdrop name
	bdName = nuke.getInput("Backdrop Name")

	#create Backdrop Node
	bd = nuke.createNode("BackdropNode")
	bd.knob("label").setValue(bdName)
	bd.knob("note_font_size").setValue(50)
	bd.knob("xpos").setValue(leftX - 50)
	bd.knob("ypos").setValue(topY - 90)
	bd.knob("bdwidth").setValue(theWidth + 90) #padding
	bd.knob("bdheight").setValue(theHeight + 90) #padding
	bd.knob("name").setValue(bdName)
	bd.knob("tile_color").setValue(0x88888800)




    
 
nuke.menu("Nuke").addCommand("Edit/Node/Close all properties",
clear_properties, "ctrl+shift+a")
nuke.menu("Nuke").addCommand("Edit/Node/autoBackdrop", autoBackdrop, "shift+b")


######################


import extractFrame 

n = nuke.toolbar('Nodes') 
n.addCommand('Edit/extractFrame', 'extractFrame.extractFrame()', "shift+f")



######################






######################

#  menu.py
#  J_Ops
#
#  Created by Jack Binks on 07/01/2010.
#  Copyright (c) 2010 Jack Binks. All rights reserved.
import nuke
import os.path
import J_Ops

toolbar = nuke.menu("Nodes")
n = toolbar.addMenu("J_Ops", "J_Ops.png")
n.addCommand("J_3Way", "J_Ops.createNode(\"J_3Way\")", "", "J_3Way.png")
n.addCommand("J_GeoManager", "J_Ops.createNode(\"J_GeoManager\")", "", "J_GeoManager.png")
n.addCommand("J_GotSomeID", "J_Ops.createNode(\"J_GotSomeID\")", "", "J_GotSomeID.png")
n.addCommand("J_MergeHDR", "J_Ops.createNode(\"J_MergeHDR\")", "", "J_MergeHDR.png")
m = n.addMenu("J_Mullet", "J_Mullet.png")
m.addCommand("J_MulletBody", "J_Ops.createNode(\"J_MulletBody\")", "", "J_MulletBody.png")
m.addCommand("J_MulletCompound", "J_Ops.createNode(\"J_MulletCompound\")", "", "J_MulletCompound.png")
m.addCommand("J_MulletConstraint", "J_Ops.createNode(\"J_MulletConstraint\")", "", "J_MulletConstraint.png")
m.addCommand("J_MulletForce", "J_Ops.createNode(\"J_MulletForce\")", "", "J_MulletForce.png")
m.addCommand("J_MulletSolver", "J_Ops.createNode(\"J_MulletSolver\")", "", "J_MulletSolver.png")
n.addCommand("J_Scopes", "J_Ops.createNode(\"J_Scopes\")", "", "J_Scopes.png")
n.addCommand("J_ZKeyer", "J_Ops.createNode(\"J_ZKeyer\")", "", "J_ZKeyer.png")
n.addCommand("J_ZMaths", "J_Ops.createNode(\"J_ZMaths\")", "", "J_Zmaths.png")
n.addCommand("J_Ops Help", "J_Ops.launchHelp()", "", "J_Ops_Help.png")


###################################################################################
#Customised drag and drop, adding support for geos, luts and chans.

import nukescripts, nuke, os

def jopsFileHandler(dropdata):
    filePath=dropdata
    fileRange= ''
    
    if not os.path.isfile(filePath):
        filePath, sep, fileRange = filePath.rpartition(' ')

    fileName, fileExt = os.path.splitext(filePath)

    if fileExt == '.obj':
        r = nuke.createNode("ReadGeo2", inpanel=False)
        r["file"].fromUserText(dropdata)
        r["selected"].setValue(0)
        return True

    if fileExt == '.fbx':
        r = nuke.createNode("ReadGeo2", inpanel=False)
        r["file"].fromUserText(dropdata)
        r["selected"].setValue(0) 
        nuke.tprint(dropdata)
        r = nuke.createNode("Camera2", 'read_from_file 1 file '+dropdata, inpanel=False)
        r["selected"].setValue(0)
        r = nuke.createNode("Light2", 'read_from_file 1 file '+dropdata, inpanel=False)
        r["selected"].setValue(0)        
        return True
    
    if fileExt == '.3dl' or fileExt == '.blur' or fileExt == '.csp' or fileExt == '.cub' or fileExt == '.cube' or fileExt == '.vf' or fileExt == '.vfz':
        r = nuke.createNode("Vectorfield", inpanel=False)
        r["vfield_file"].setValue(dropdata)
        r["selected"].setValue(0)
        return True

    if fileExt == '.chan':
        r = nuke.createNode("Camera2", inpanel=False)
        nuke.tcl('in %s {import_chan_file %s }' %(r.name(), dropdata))
        r["selected"].setValue(0)
        return True

    r = nuke.createNode("Read", inpanel=False)
    r["file"].fromUserText(dropdata)
    return True

def jopsPathHandler(dropdata):
    if os.path.isdir(dropdata):

        recurse = False

        try:
            recurse = nuke.toNode('preferences')["j_ops_drop_recurse"].getValue()
        except (SyntaxError, NameError):
            pass
        
        for each in nuke.getFileNameList(dropdata, False, False, bool(recurse), False):
            jopsPathHandler(os.path.join(dropdata,each))
        return True
    else:
        return jopsFileHandler(dropdata)

def jopsDropHandler(droptype, dropdata):
    #Fix filename for linux drops
    if dropdata.startswith("file://"):
        dropdata = dropdata[7:]
    if os.path.isfile(dropdata) or os.path.isdir(dropdata):
        return jopsPathHandler(dropdata)
    return False

###################################################################################
#Dag bookmarking.

def jopsBookmarkAddMenus():
    toolbar = nuke.menu("Nodes")
    toolbar = toolbar.findItem("J_Ops")
    toolbar = toolbar.addMenu("Python")
    m = toolbar.addMenu("DAG Bookmarks")
    m.addCommand('JB1 (Restore Bookmark 1)', 'jopsBookmarkRestore(1)', 'shift+F7')
    m.addCommand('JB2 (Restore Bookmark 2)', 'jopsBookmarkRestore(2)', 'shift+F8')
    m.addCommand('JB3 (Restore Bookmark 3)', 'jopsBookmarkRestore(3)', 'shift+F9')
    m.addCommand('JB4 (Restore Bookmark 4)', 'jopsBookmarkRestore(4)', 'shift+F10')
    m.addCommand('JB5 (Restore Bookmark 5)', 'jopsBookmarkRestore(5)')
    m.addCommand('JB6 (Restore Bookmark 6)', 'jopsBookmarkRestore(6)')
    m.addCommand('JB7 (Restore Bookmark 7)', 'jopsBookmarkRestore(7)')
    m.addCommand('JB8 (Restore Bookmark 8)', 'jopsBookmarkRestore(8)')
    m.addCommand('JB9 (Restore Bookmark 9)', 'jopsBookmarkRestore(9)')
    m.addCommand('JSB1 (Store Bookmark 1)',  'jopsBookmarkSave(1)', 'alt+F7')
    m.addCommand('JSB2 (Store Bookmark 2)',  'jopsBookmarkSave(2)', 'alt+F8')
    m.addCommand('JSB3 (Store Bookmark 3)',  'jopsBookmarkSave(3)', 'alt+F9')
    m.addCommand('JSB4 (Store Bookmark 4)',  'jopsBookmarkSave(4)', 'alt+F10')
    m.addCommand('JSB5 (Store Bookmark 5)',  'jopsBookmarkSave(5)')
    m.addCommand('JSB6 (Store Bookmark 6)',  'jopsBookmarkSave(6)')
    m.addCommand('JSB7 (Store Bookmark 7)',  'jopsBookmarkSave(7)')
    m.addCommand('JSB8 (Store Bookmark 8)',  'jopsBookmarkSave(8)')
    m.addCommand('JSB9 (Store Bookmark 9)',  'jopsBookmarkSave(9)')
    m.addCommand('JSNB1 (Store Node Bookmark 1)',  'jopsBookmarkSave(1, "node")', 'alt+shift+F7')
    m.addCommand('JSNB2 (Store Node Bookmark 2)',  'jopsBookmarkSave(2, "node")', 'alt+shift+F8')
    m.addCommand('JSNB3 (Store Node Bookmark 3)',  'jopsBookmarkSave(3, "node")', 'alt+shift+F9')
    m.addCommand('JSNB4 (Store Node Bookmark 4)',  'jopsBookmarkSave(4, "node")', 'alt+shift+F10')
    m.addCommand('JSNB5 (Store Node Bookmark 5)',  'jopsBookmarkSave(5, "node")')
    m.addCommand('JSNB6 (Store Node Bookmark 6)',  'jopsBookmarkSave(6, "node")')
    m.addCommand('JSNB7 (Store Node Bookmark 7)',  'jopsBookmarkSave(7, "node")')
    m.addCommand('JSNB8 (Store Node Bookmark 8)',  'jopsBookmarkSave(8, "node")')
    m.addCommand('JSNB9 (Store Node Bookmark 9)',  'jopsBookmarkSave(9, "node")')

def jopsBookmarkSave(index, mode='dag'):
    tabNameString   = "DAG_Bookmarks"
    try:
        nuke.root()[tabNameString]
    except (SyntaxError, NameError):
        nuke.root().addKnob(nuke.Tab_Knob(tabNameString))
        for ind in range(1,10):
            zoomNameString  = "jops_bookmark_"+str(ind)+"_zoom"
            posNameString   = "jops_bookmark_"+str(ind)+"_pos"
            xyKnob   = nuke.XY_Knob(posNameString, str(ind))
            zoomKnob = nuke.Double_Knob(zoomNameString, "")
            zoomKnob.setFlag(nuke.NO_ANIMATION)
            zoomKnob.setFlag(nuke.DISABLED)
            xyKnob.setFlag(nuke.NO_ANIMATION)
            xyKnob.setFlag(nuke.DISABLED)
            zoomKnob.clearFlag(nuke.STARTLINE)
            nuke.root().addKnob(xyKnob)
            nuke.root().addKnob(zoomKnob)
        nuke.root().addKnob(nuke.Text_Knob("j_ops_bookmarks_note", "", "<i>DAG bookmarks are part of the J_Ops toolset available on Nukepedia</i>"))
    
    xpos = 0.0
    ypos = 0.0
    zoom = 0.0
    selectedList = []

    if mode == 'node':
        if nuke.selectedNodes():
            xposList = []
            yposList = []
            for anode in nuke.selectedNodes():
                xposList.append(anode["xpos"].getValue())
                yposList.append(anode["ypos"].getValue())
            xpos = sum(xposList, 0.0) / len(xposList)
            ypos = sum(yposList, 0.0) / len(yposList)
        else:
            return
    else:
        if nuke.selectedNodes():
            for anode in nuke.selectedNodes():
                selectedList.append(anode)
                anode["selected"].setValue(0.0)

        tempNode = nuke.createNode("Dot", inpanel=False)
        xpos = tempNode["xpos"].getValue()
        ypos = tempNode["ypos"].getValue()
        nuke.delete(tempNode)
    
    zoom = nuke.zoom()
    
    zoomNameString  = "jops_bookmark_"+str(index)+"_zoom"
    posNameString   = "jops_bookmark_"+str(index)+"_pos"
        
    nuke.root()[zoomNameString].clearFlag(nuke.DISABLED)
    nuke.root()[zoomNameString].setValue(zoom)
    nuke.root()[posNameString].clearFlag(nuke.DISABLED)
    nuke.root()[posNameString].setValue(xpos,0)
    nuke.root()[posNameString].setValue(ypos,1)
    
    if selectedList:
        for anode in selectedList:
            anode["selected"].setValue(1.0)

def jopsBookmarkRestore(index):
    zoomNameString  = "jops_bookmark_"+str(index)+"_zoom"
    posNameString   = "jops_bookmark_"+str(index)+"_pos"
 
    try:
        z = nuke.root()[zoomNameString]
        p = nuke.root()[posNameString]
        if z.enabled():
            zoom = z.getValue()
            xpos = p.x()
            ypos = p.y()
            pos = [xpos, ypos]
            nuke.zoom(zoom, pos)
    except (SyntaxError, NameError):
        pass




###################################################################################
#Preferences

def preferencesCreatedCallback():
    p = nuke.toNode('preferences')
    
    #Setup J_Ops prefs knobs if they don't exist.
    try:
        jopsKnobsPresent = p["J_Ops"]
    except (SyntaxError, NameError):
        k = nuke.Tab_Knob("J_Ops")
        k.setFlag(nuke.ALWAYS_SAVE)
        p.addKnob(k)

        v = nuke.Double_Knob("j_ops_ver", "j_ops_ver")
        v.setFlag(nuke.ALWAYS_SAVE)
        v.setFlag(nuke.INVISIBLE)
        v.setValue(2.0101)
        p.addKnob(v)
        
        k = nuke.Boolean_Knob("j_ops_enable_drop", "Improved drag and drop")
        k.setFlag(nuke.ALWAYS_SAVE)
        k.setFlag(nuke.STARTLINE)
        k.setValue(1.0)
        k.setTooltip("Enable/disable a somewhat improved drag and drop behaviour. Requires Nuke restart to take effect. Adds creation of geo, camera, light and vectorfield nodes based on incoming file extensions, as well as support for sequences when dropping folders onto DAG.")
        p.addKnob(k)

        k = nuke.Boolean_Knob("j_ops_enable_bookmark", "DAG bookmarks")
        k.setFlag(nuke.ALWAYS_SAVE)
        k.setFlag(nuke.STARTLINE)
        k.setValue(1.0)
        k.setTooltip("Enable/disable DAG bookmarks, allowing storing and recalling of particular DAG locations and zoom settings, for easy navigation around a script. Requires Nuke restart to take effect. Adds Python-DAG Bookmarks menu to J_Ops toolbar, offering access via mouse, tab menu, or hotkeys.")
        p.addKnob(k)

        k = nuke.Text_Knob("j_ops_dropdivider_label", "Drag And Drop")
        k.setFlag(nuke.ALWAYS_SAVE)
        p.addKnob(k)

        k = nuke.Boolean_Knob("j_ops_drop_recurse", "Recurse directories")
        k.setFlag(nuke.ALWAYS_SAVE)
        k.setValue(1.0)
        k.setTooltip("Enable/disable recursion into directories dropped on DAG. When enabled will result in entire directory structure being imported into DAG, when disabled only the directory dropped will be imported (ie none of its sub directories)")
        p.addKnob(k)
        
    #Check for preference setting, and if drop enabled add its callback/
    dropEnabled = False
    try:
        dropEnabled = nuke.toNode('preferences')["j_ops_enable_drop"].getValue()
    except (SyntaxError, NameError):
        pass

    if dropEnabled == True:
        nukescripts.drop.addDropDataCallback(jopsDropHandler)

    #Check for preference setting, and if drop enabled add its callback/
    bookmarkEnabled = False
    try:
        bookmarkEnabled = nuke.toNode('preferences')["j_ops_enable_bookmark"].getValue()
    except (SyntaxError, NameError):
        pass

    if bookmarkEnabled == True:
        jopsBookmarkAddMenus()

#Adding callbacks to ensure knobs added if needed, and interpreted. 
#Root is done to catch the case where there are no custom prefs,
#so no creation callback for it.
nuke.addOnCreate(preferencesCreatedCallback, nodeClass='Preferences')
nuke.addOnCreate(preferencesCreatedCallback, nodeClass='Root')



import sys
    
import nuke


print 'Loading Lab Tools...'
menubar = nuke.menu("Nuke")

# Custom Lab Tools
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Lab Tools", "")

n = m.addMenu("Draw", "draw.png")
n = m.addMenu("Draw/Utility", "utility.png")
m.addCommand("Draw/FlareFactory Plus", "nuke.createNode(\"FlareFactory_Plus\")", icon="FlareFactoryPlus.png")
