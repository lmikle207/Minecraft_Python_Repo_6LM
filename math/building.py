from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 5
length = 6
blockType = 4
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
trees = 4
trees = trees * 2
skeletons = 8
skeletons = skeletons /2
