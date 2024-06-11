from controller import Robot, Motion, Keyboard

robot = Robot()
keyboard = Keyboard()
timestep = 32

keyboard.enable(timestep)

wave = Motion('../../motions/wave.motion')

def startMotion(motion):
    motion.play()
    
def printMessages():
    print("Press UP to WAVE")
    
key = -1
printMessages()

while robot.step(timestep) != -1:
    key = keyboard.getKey()
    if key == Keyboard.UP:
        startMotion(wave)
