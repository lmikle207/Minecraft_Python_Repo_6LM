from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -1.34
y = 100
z = -17
mc.player.setTilePos(x, y, z)
import time
time.sleep(10)
x = 100
y = 100
z = 101
mc.player.setTilePos(x, y , z)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 110
z = -12
mc.player.setPos(x, z, y)
