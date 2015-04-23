
import nuke

def  FreezeFrom():
  for n in nuke.selectedNodes():

    n.knob('from1').fromScript(n.knob('to1').toScript())
    n.knob('from2').fromScript(n.knob('to2').toScript())
    n.knob('from3').fromScript(n.knob('to3').toScript())
    n.knob('from4').fromScript(n.knob('to4').toScript())
    nuke.Knob.clearAnimated(nuke.selectedNode().knob('from1'))
    nuke.Knob.clearAnimated(nuke.selectedNode().knob('from2'))
    nuke.Knob.clearAnimated(nuke.selectedNode().knob('from3'))
    nuke.Knob.clearAnimated(nuke.selectedNode().knob('from4'))

def  FreezeTo():
  for n in nuke.selectedNodes():

    n.knob('to1').fromScript(n.knob('from1').toScript())
    n.knob('to2').fromScript(n.knob('from2').toScript())
    n.knob('to3').fromScript(n.knob('from3').toScript())
    n.knob('to4').fromScript(n.knob('from4').toScript())
    nuke.Knob.clearAnimated(nuke.selectedNode().knob('to1'))
    nuke.Knob.clearAnimated(nuke.selectedNode().knob('to2'))
    nuke.Knob.clearAnimated(nuke.selectedNode().knob('to3'))
    nuke.Knob.clearAnimated(nuke.selectedNode().knob('to4'))