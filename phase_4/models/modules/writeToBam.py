import direct.directbase.DirectStart
from pandac.PandaModules import *

# Write a scene to bam



object1 = loader.loadModel('gagShop_TT.egg')
object1.reparentTo(render)
object1.find('**/sign').removeNode()

object1.writeBamFile('gagShop_TT.bam')

# dp.writeBamFile("hqTT_ost.bam")


run()
