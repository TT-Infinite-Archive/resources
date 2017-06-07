import direct.directbase.DirectStart
from pandac.PandaModules import *

# Write a scene to bam

'''
scene = render.attachNewNode('sceneParent')

object1 = loader.loadModel('phase_6/models/props/outdoor_zone_tree.bam')
object1.reparentTo(scene)

object2 = loader.loadModel('phase_6/models/props/outdoor_zone_tree.bam')
object2.reparentTo(scene)

scene.flattenStrong() # Optional
scene.writeBamFile('objects.bam')
'''

# Find a node within a model and write it to bam


dp = loader.loadModel('minnies_melody_land.bam')
dp.reparentTo(render)

node = dp.find('**/midkey_floor')
node2 = dp.find('**/MMsz_water')
nod3 = dp.find('**/pond_floor')
dp.writeBamFile("mmPiano.bam")



run()

