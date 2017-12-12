from mcpi.minecraft import Minecraft
mc = Minecraft.create()


pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y, z)
mc.postToChat(blockType == 0)
leaves = 18
wood = 11
y = y - 1
print("Is player in tree True/False")
print("Is block under player leaves True/False")

