from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 10
length = 10

buildX = -5
buildY = 31
buildZ = 12

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX <= x <= buildX + width and buildY <= y <= buildY + height and buildZ <= z <= buildZ + length
print(inside)
