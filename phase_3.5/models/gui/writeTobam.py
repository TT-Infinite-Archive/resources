import direct.directbase.DirectStart
from pandac.PandaModules import *

object1 = loader.loadModel('chat_input_gui.bam')
object1.reparentTo(render)
object1.ls()

run()