from mcpi.minecraft import Minecraft
mc = Minecraft.create()
valid = True
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if not -127 < x < 127:
    valid = False

if valid:
    mc.player.setPos(0.5, 1.0, 0.5)
else:
    mc.postToChat("Please enter a valid location")
    
             
