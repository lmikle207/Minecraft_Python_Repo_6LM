from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = -5
y = 32
z = 12
width = 10
height = 10
length = 10
blockType = 4
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x+1, y+1, z+1, x + width-1, y + height-1, z + length-1, 0)

