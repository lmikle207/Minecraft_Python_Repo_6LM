from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10.0
y = 110.0
z = 12.0
mc.player.setPos(x, y, z)
import time
time.sleep(10)

x = 100
y = 125
z = 10
mc.player.setPos(x, y, z)
