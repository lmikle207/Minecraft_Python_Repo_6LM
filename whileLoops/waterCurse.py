import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y, pos.z, 8)
count = 30
while count < 30:
    mc.player.getPos(pos.x, pos.y, pos.z, 8)
    count += 30
    time.sleep(30)
