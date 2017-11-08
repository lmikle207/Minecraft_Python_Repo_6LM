from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -1.34
y = 100
z = -17
mc.player.setTilePos(x, y, z)
import time
x = 100.5
y = 12.0
z = 101.5
mc.player.setTilePos(x, y, z)
time.sleep(10)
x = 23
y =56
z = 78
mc.player.setTilePos(x, y, z)

