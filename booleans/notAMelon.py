from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -1.9
y = -27
z = 2.6
melon = 103
block = mc.getBlock(x, y, z)

noMelon = block != melon

mc.postToChat("You need to get some food: " + str(noMelon))
