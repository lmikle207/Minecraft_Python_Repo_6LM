from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x = -0.9
y = 4.0
z = 0.5
gift = mc.getBlock(x, y, z)
if gift != 0:
    print("Gift detected")
    if gift == 57:
        print("Diamond detected!")
        mc.setBlock(-0.03, 2.0, 1.6, 0)
        
        
            
else:
    print("No gift detected")
    mc.postToChat("Place an offering on the pedestal.")
    
