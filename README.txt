README////////////////////////////////////////////////////////////////////////////////////////////////////////

dw_camProjSet_v1_1

Written by:  Dave Windhorst    09/05/2012


Python script pack including 2 new commands/nodes: 'Camera Project Current Frame' and 'Camera Project Source'. 
A new 'ProjCam' node is created based off of the selected source Camera at the current Viewer frame. A 
'Project3D' node is automatically created and connected if an image input is also selected besides the 
source camera.

The 'Camera project Current Frame' command allows the user creates a 'ProjCamS' node, which only contains 
the values originating from the selected source camera at the current Viewer frame.  

The 'Camera Project Source' command creates a 'ProjCamM' node, which contains an expression link back to 
the source camera and initially sets the projected camera values at the current Viewer frame.  The 
'ProjCamM' node also contains a 'Frame_Settings' Tab which allows the user to update the projection frame, 
lock/unlock the frame from accidental changes, and finally bake the values at the current frame, breaking 
the expression links to the source camera.


NOTE: Current limitations are:
		
		-User must specify only one source 'Camera' node to obtains values from
		-User can specify up to one image input to auto connect to the 'Project3D' node or connect manually 
		later
		-Only nodes that can actually connect to the 'Project3D' input will be connected automatically/Any 
		node class that connects manually to the 'Project3D' node will work!
		
		(i.e. If a 'Viewer1' and 'Camera1' node are selected, the 'ProjCam' and 'Project3D' nodes will be 
		created; however, the 'Viewer' node class cannot input as a texture into the 'Project3D', thus the 
		'Viewer1' and 'Project3D1' will not be connected.  On the other hand, if a 'Blur1' or 'Roto1' is 
		selected, the connection will work.) 
		

NOTE: Created in Nuke 6.3v8.


Contained Files///////////////////////////////////////////////////////////////////////////////////////////////

- 'icons' folder
	- dw_camProjCurFrame.png
	- dw_camProjSource.png
	- dw_menu.png
	
- 'python' folder
	- dw_camProjSet_v1_1.py

- init.py
- menu.py
- README.TXT


Steps/////////////////////////////////////////////////////////////////////////////////////////////////////

1. Import/Install Python Scripts into Nuke. To install, copy files (except README.TXT) to '.nuke' folder
	found on workstation. To learn why/how, please watch this tutorial:

	http://www.davewindhorst.com/resources.php?type=tutorials#dw_tut001


	
	To import commands/run them from the script editor are as follows:
	
	
		Camera Project Current Frame:	dw_camProjSet_v1_1.camProjSingle()
		
		Camera Project Source:			dw_camProjSet_v1_1.camProjMultiple()
		
		
		
2. Use Imported or 'DW Tools' menu created on Nuke 'Nodes' Menu Toolbar



Camera Project Current Frame  (Hotkey: Shift+C )//////////////////////////////////////////////////////////////

Creates a 'ProjCamS' node based on the currently selected source 'Camera' node (required) and a texture input 
node to project (optional).  The 'ProjCamS' node is automatically connected to a 'Project3D' node. If a texture 
input is in the current selection and is of a type of node class with the ability to connect with the 
'Project3D' node, then they will be automatically.  If no texture input is specified upon runtime, the 
'Project3D' node will be created and can be connected manually later. The projection frame and source camera 
can be seen on the node in the DAG panel. 

Use this command when the current frame in the Viewer is the desired projection frame and no modifications to 
the source camera are to be expected. This command is a barebones/lightweight and efficient version to use.



	1.  Select the source 'Camera' node (required) and/or one texture input node (optional - i.e. 'Blur1' or 
		'Roto1').
		
		For example:
		
			Selected Nodes:			Camera1, Roto1
			
			
			After Command Runtime:
			
							
									Roto1 ----> Project3D1 <---- ProjCamS1
													|
													v
			
			
	2.  The projection is now ready to be created - specify an input texture if not already, and connect 
		'Project3D' node output to desired Geo for use.


		

Camera Project Source  (Hotkey:  Shift+Ctrl+C )///////////////////////////////////////////////////////////////

Like the 'Camera Project Current Frame' command, the 'Camera Project Source' command creates a camera 
projection setup based on the currently selected source 'Camera' (required) and a texture input node to project 
(optional). However, unlike the previous command, the 'Camera Project Source' creates expression links to the 
original source camera, allowing the user to modify the source camera values while automatically updating the 
camera projection.

Besides creating a projection camera, the 'ProjCamM' node contains an extra tab ('Frame_Settings') allowing the 
user to change the frame on which the projection camera is obtaining values from the source camera. The user also 
has a 'SET CURRENT FRAME' button, allowing the user to change the projection frame to the current one in the 
Viewer panel.  The 'LOCK/UNLOCK FRAME' button allows the user to disable the projection frame and 
'SET CURRENT FRAME' from being used. This feature is designed to keep users from accidentally changing the frame 
once the desired one is found.  The 'BAKE FRAME' button breaks the connection to the source camera and stores the 
current projection frame values as animated keys for the frame range specified.  This option mimics the 
lightweight command 'Camera Project Current Frame' and cleans up the DAG window of unecessary expression links.


NOTE:  Here are some interesting results to try (only works when expression links to source camera still exist!):


		1.  By setting the 'projCamFrame' to this expression:	
		
		
		
				frame
		
		
		
			-This will recreate the camera movement for every frame (as though the projection camera was the 
			source camera all along.)

			
			
		2.	By setting the 'projCamFrame' to this expression:	
		
		
		
				frame > # & frame < ## ? frame: 0
		
		
		
			Where # and ## are two different numbers of a range(#,##)
			
			-This will recreate the source camera movement only for the frames that are within the range of # and ##
				-If the current frame is outside the range, the camera defaults to frame 0 in this case
					- NOTE:  Number 3 below is better for a frame range limit by holding the camera at the range frames 
					when the current frame is outside the range
			
			
			
		3.	By setting the 'projCamFrame' to this expression:	
		
		
		
				frame > # & frame < ## ? frame: frame <= # ? # : ##
		
		
		
			Where # and ## are two different numbers of a range(#,##)
			
			-This will recreate the source camera movement only for the frame that are within the range of # and ##
				-If the current frame is outside the range, the camera will sit still on either # or ## depending on
				 the current frame