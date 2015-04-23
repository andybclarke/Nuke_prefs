'''
Created on 01-Mar-2012

updated on 16-apr-2013

@author: satheesh.R
contact: satheesrev@gmail.com 
'''
import nuke
## creating panel
def  extractFrame():
    curFrame = nuke.frame()
    ef = nuke.Panel("extractFrame.....   by satheesh-R", 50)
    ef.addSingleLineInput("feed frame no to Hold:\n (this is your current frame)",curFrame)
    ef.addButton("cancel")
    ef.addButton("ok")
    window = ef.show()
    if window == 0:
        return

    result=ef.value("feed frame no to Hold:\n (this is your current frame)")
    frame = nuke.frame()
    if result =="":
        result=frame

## create framehold and assign user value
    fh = nuke.createNode("FrameHold")
    fh.setName("HeldFrame")
    fh['first_frame'].setValue(int(result))