#dw_CamProjSetup.py  v1.1
#
#Written by:  Dave Windhorst    09/05/2012
#								09/04/2012  v1.0
#
#Setup camera projections quickly in Nuke. Script contains 2 main functions to call:
#
#	camProjSingle()
#	camProjMultiple()
#
#
#camProjSingle() - Creates a 'ProjCamS' node using the current frame amd selected source 
#camera for values. Camera is automatically connected to a 'Project3D' node for use.
#
#camProjMultiple() - Creates a 'ProjCamM' node that initially uses the current frame and 
#selected source camera values; however, unlike 'ProjCamS' nodes, an extra Tab 'Frame_Settings' 
#is available to tweak the frame the projection is based on. The source camera is expression 
#linked to the 'ProjCamM' node and allows for the user to set the current frame, lock/unlock the 
#frame setting temporarily (keeping source camera linked - good for source cameras that are to be 
#updated/modified in some way), and finally bake the frame values as expressions in order to break 
#connection with source camera
#
#


#BEGIN SCRIPT



#Required modules imported
import nuke


#Create camera projection based on current camera selection and single frame
def camProjSingle():
	#Retrieve selected 'Camera' node and 'img' input node
	camSelect = nuke.selectedNodes( "Camera2" )
	imgSelect = nuke.selectedNodes()
	
	#Retrieve current frame in Viewer
	curFrame = nuke.frame()
	
	#Specify 'ProjCam' type
	camType = "S"
	
	#Specify node and GL color ( Hexadecimal Value )
	camColor = 4283190527L
	
	#Create 'ProjCamS' node
	projCam = camProjCreate( camSelect, imgSelect, curFrame, camType, camColor )
	
	if projCam !="":
		#Show properties panel for node
		projCam.showControlPanel()
	
	return


#Create camera projection based on current camera selection and expression link them
def camProjMultiple():
	#Retrieve selected 'Camera' node and 'img' input node
	camSelect = nuke.selectedNodes( "Camera2" )
	imgSelect = nuke.selectedNodes()
	
	#Retrieve current frame in Viewer
	curFrame = nuke.frame()
	
	#Specify 'ProjCam' type
	camType = "M"
	
	#Specify node and GL color ( Hexadecimal Value )
	camColor = 3796845823L
	
	#Create 'ProjCamM' node
	projCam = camProjCreate( camSelect, imgSelect, curFrame, camType, camColor )
	
	if projCam != "":
		#If 'ProjCamM' node is not empty, create knobs and add them
		
		#Frame Settings Tab
		projCamTab = nuke.Tab_Knob( "Frame_Settings" )
		
		#Projected Frame (Integer Knob)
		projCamFrame = nuke.Int_Knob( "projCamFrame", "projected frame " )
		projCamFrame.setTooltip( "Specifies the frame the projection camera is currently using to obtain values from source camera." )
		
		#Set Current Frame Button
		curFrameBttn = nuke.PyScript_Knob( "curFrameBttn", "SET CURRENT FRAME", "nuke.thisNode()['projCamFrame'].setValue( nuke.frame() )" )
		curFrameBttn.setTooltip( "Sets the current Viewer Frame to be the projection camera frame to obtain values for." )
		
		#Lock/Unlock Projected Frame Knob
		lockFrameBttn = nuke.PyScript_Knob( "lockFrameBttn", "LOCK/UNLOCK FRAME", "dw_camProjSet_v1_1.lockUnlockFrame( nuke.thisNode() )" )
		lockFrameBttn.setTooltip( "Locks and unlocks projection frame being modified. This allows expressions to source camera to still exist, but not be able to change the frame being referenced. This is a good option for temporary setups where the source camera is expected to be changed/modified." )
		
		#Bake Projected Frame Values
		bakeFrameBttn = nuke.PyScript_Knob( "bakeBttn", "BAKE FRAME", "dw_camProjSet_v1_1.bakeCamFrame( nuke.thisNode() )" )
		bakeFrameBttn.setTooltip( "Bakes the current frame values, thus severing expressions to the source camera. Values are baked down as expressions rather than keyed values to ensure settings aren't changed easily." )
		
		#Create Divider Knobs
		projDivKnob = nuke.Text_Knob( "", "", "" )
		
		#Create 'Written by' Knob
		projByName = "FRAME_SETTINGS (CAMERA PROJECTION CTRLS) TAB"
		projByVer = "v1.1"
		projByAut = "Dave Windhorst"
		projByDate = "09/05/2012"
		projByText = projByName + " : " + projByVer + "\n\nWritten by: " + projByAut + "    " + projByDate
		projByKnob = nuke.Text_Knob( "","", projByText )
		projByKnob.setFlag( nuke.STARTLINE )
		
		#Knobs Array
		projCamKnobs = [projCamTab, projCamFrame, curFrameBttn, lockFrameBttn, bakeFrameBttn, projDivKnob, projByKnob]
		
		#Add Knobs to 'ProjCamM' node
		for i in projCamKnobs:
			projCam.addKnob(i)
		
		#Set the Projection Frame to the current frame
		projCam['projCamFrame'].setValue( curFrame )
		
		#Retrieve the source camera name
		camExpName = camSelect[0]['name'].value()
		
		#Update the 'ProjCam' properties to expression link to the source camera
		projCam['label'].setValue( "frame: [value projCamFrame]" + "\nsource: " + camExpName )
		
		projCam['focal'].setExpression( camExpName + ".focal" )
		projCam['haperture'].setExpression( camExpName + ".haperture" )
		projCam['vaperture'].setExpression( camExpName + ".vaperture" )
		projCam['near'].setExpression( camExpName + ".near" )
		projCam['far'].setExpression( camExpName + ".far" )
			
		projCam['translate'].setExpression( camExpName + ".translate.x( projCamFrame )", 0)
		projCam['translate'].setExpression( camExpName + ".translate.y( projCamFrame )", 1)
		projCam['translate'].setExpression( camExpName + ".translate.z( projCamFrame )", 2)
		
		projCam['rotate'].setExpression( camExpName + ".rotate.x( projCamFrame )", 0)
		projCam['rotate'].setExpression( camExpName + ".rotate.y( projCamFrame )", 1)
		projCam['rotate'].setExpression( camExpName + ".rotate.z( projCamFrame )", 2)
		
		projCam['scaling'].setExpression( camExpName + ".scaling.x( projCamFrame )", 0)
		projCam['scaling'].setExpression( camExpName + ".scaling.y( projCamFrame )", 1)
		projCam['scaling'].setExpression( camExpName + ".scaling.z( projCamFrame )", 2)
	
		#Show properties panel for node
		projCam.showControlPanel()
	
	return


#Lock/Unlock frame knob and frame button
def lockUnlockFrame( nodeBttn ):
	#Lock/Unlock Knob Array
	lockKnobs = ['projCamFrame', 'curFrameBttn']
	
	for i in lockKnobs:
		#Lock/Unlock each item of the array
		if nodeBttn[i].enabled() == True:
			#If the knobs are enabled, disable them
			nodeBttn[i].setEnabled( False )
		else:
			#If the knobs are disabled, enable them
			nodeBttn[i].setEnabled( True )

	return


#Bake current frame values and break expression link to source camera
def bakeCamFrame( bakeNode ):
	#Get frame range to bake
	getRange = nuke.getFramesAndViews( "Bake projection curves?", "%s-%s" % ( nuke.root().firstFrame(), nuke.root().lastFrame() ) )
	if not getRange:
		return
	fRange = nuke.FrameRange( getRange[0] )
	views = getRange[1]
	bakeCamExpressions( bakeNode, fRange.first(), fRange.last(), fRange.increment(), views )

	
#Get all camera curves	
def getCamCurves( knob, views ):
	curves = []
	for i in views:
		curves.extend( knob.animations(i) )
	return curves


#Bake all camera curves and remove expressions
def bakeCamCurve( curve, first, last, inc ):
	for i in xrange( first, last, inc ):
		curve.setKey( i, curve.evaluate(i) )
	curve.setExpression( 'curve' )


#Bake camera values
def bakeCamExpressions( node, first, last, inc, views ):
	expKnobs = [i for i in node.knobs().values() if i.hasExpression() ]
	
	allCurves = []
	for i in expKnobs:
		allCurves += getCamCurves( i, views )
	
	for i in allCurves:
		bakeCamCurve( i, first, last, inc )
	
	
#Create 'ProjCam' node
def camProjCreate( camSelect, imgSelect, frame, camType, camColor ):
	#Retrieve all other selected nodes that are not 'Camera' nodes
	imgArray = []
	for i in imgSelect:
		if i not in camSelect:
			imgArray.append(i)
	
	if len(camSelect) != 1:
		#If more than one camera or no cameras are selected, error message, return no node
		nuke.message( "Must select a source 'Camera' to create projection camera from!" )
		projCam = ""
		
	elif len(imgArray) > 1:
		#If more than one other node is selected as an 'img' for projection, error message, return no node
		nuke.message( "Please select no more than one texture node to project besides source camera node!" )
		projCam = ""
		
	else:
		#Retrieve selected camera properties
		camNode = camSelect[0]
		
		camName = camNode['name'].value()
		
		camFocal = camNode['focal'].value()
		camAprtH = camNode['haperture'].value()
		camAprtV = camNode['vaperture'].value()
		camNear = camNode['near'].value()
		camFar = camNode['far'].value()
		
		camTrans = camNode['translate'].value()
		camRot = camNode['rotate'].value()
		camScale = camNode['scaling'].value()
		
		#Store camera properties for use
		camVal = { 'name': camName, 'focal': camFocal, 'haperture': camAprtH, 'vaperture': camAprtV, 'camNear': camNear, 'camFar': camFar, 'tx': camTrans[0], 'ty': camTrans[1], 'tz': camTrans[2], 'rx': camRot[0], 'ry': camRot[1], 'rz': camRot[2], 'sx': camScale[0], 'sy': camScale[1], 'sz': camScale[2]}
		
		#Create and set 'projCam' node and properties
		projCam = nuke.nodes.Camera2()
		
		#Retrieve existing 'projCam' nodes to find next node number for name ( 'projCam#' )
		projCamName = "ProjCam" + camType
		selCam = nuke.allNodes("Camera2")
		finNum = 0
		for i in selCam:
			if projCamName in i['name'].value():
				tempNum = int ( i['name'].value().split( projCamName )[-1] )
				if tempNum > finNum:
					finNum = tempNum
		finNum = finNum + 1
		
		#Set 'ProjCam' properties based on source camera and specified type
		projCam['name'].setValue( projCamName + str( finNum ) )	
		projCam['label'].setValue( "frame: " + str( frame ) + "\nsource: " + camVal['name'] )
		
		projCam['tile_color'].setValue( camColor )
		projCam['gl_color'].setValue( camColor )
		
		projCam['focal'].setValue( camVal['focal'] )
		projCam['haperture'].setValue( camVal['haperture'] )
		projCam['vaperture'].setValue( camVal['vaperture'] )
		projCam['near'].setValue( camVal['camNear'] )
		projCam['far'].setValue( camVal['camFar'] )
		
		projCam['translate'].setValue( camVal['tx'], 0 )
		projCam['translate'].setValue( camVal['ty'], 1 )
		projCam['translate'].setValue( camVal['tz'], 2 )
		
		projCam['rotate'].setValue( camVal['rx'], 0 )
		projCam['rotate'].setValue( camVal['ry'], 1 )
		projCam['rotate'].setValue( camVal['rz'], 2 )
		
		projCam['scaling'].setValue( camVal['sx'], 0 )
		projCam['scaling'].setValue( camVal['sy'], 1 )
		projCam['scaling'].setValue( camVal['sz'], 2 )
		
		#Create 'Project3D' node and connect the 'ProjCam' node to it
		projNode = nuke.nodes.Project3D()
		projNode.setInput(1, projCam)
		
		
		if len(imgArray) != 0:
			#If an 'img' node has been selected for input, connect it to the 'Project3D' node
			imgNode = imgArray[0]
			projNode.setInput(0, imgNode)
			
			#Use 'img' node position to position 'Project3D' node in DAG
			imgPosX = imgNode.xpos()
			imgPosY = imgNode.ypos()
			
			projNode['xpos'].setValue( imgPosX )
			projNode['ypos'].setValue( imgPosY + 105 )
			
		else:
			#If no 'img' node has been selected, autoplace 'Project3D' node in DAG
			projNode.autoplace()
		
		#Use 'Project3D' node position to position 'ProjCam' node in DAG
		projPosX = projNode.xpos()
		projPosY = projNode.ypos()
		
		projCam['xpos'].setValue( projPosX + 161 )
		projCam['ypos'].setValue( projPosY - 21 )
		
	return projCam

