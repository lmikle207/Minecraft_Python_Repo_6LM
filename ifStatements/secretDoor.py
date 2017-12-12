from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x = 7.7
y = 1.0
z = -46.4
gift = mc.getBlock(x, y, z)
if gift != 0:
    print("Gift detected")
    if gift == 57:
        print("Diamond detected!")
        mc.setBlock(-0.03, 2.0, 1.6, 0)
    else:
        mc.setBlocks(6.8, 0.0, -45.7, 10)
        
        
            
else:
    print("No gift detected")
    mc.postToChat("Place an offering on the pedestal.")
    mc.setBlock(10)
    mc.player.setPos
    x = 6.8
    y = 0.0
    z = -45.7
    

