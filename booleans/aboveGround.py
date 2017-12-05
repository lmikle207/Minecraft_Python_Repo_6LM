from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(-31.3,1.6)
mc.postToChat(highestBlockY)
"The player is above the ground: True/False"
