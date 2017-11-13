from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = 7.8
y = -1
z = 14.8
blockType = 10
mc.setBlock(x, y, z, blockType)
