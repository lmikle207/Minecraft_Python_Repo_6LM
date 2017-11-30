from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 11
z = 12
gift = mc.getBlock(x, y, z)


if gift == 57:


elif gift == 6:

else:
    mc.postToChat("Bring a gift to " + str(x) + ", " +str(y) + ", " + str(z))
    
