from Robot import Robot
import os 
from pynput import mouse, keyboard


#global
robot = None


def on_press(key): 
    #    print(f"{key} pressed, typ: {type(key)}")
    if str(key) == "Key.down":
         robot.wheels.forward()
    if str(key) == "Key.up":
        robot.wheels.backward()
    if str(key) == "Key.left":
        robot.wheels.turn_right()
    if str(key) == "Key.right":
        robot.wheels.turn_left()
    if str(key) == "Key.space":
        print(robot.env_detection.sweep(stops_num = 30, period_per_stop = 0.3))
    

def main():
    global robot
    robot = Robot()
    
    with keyboard.Listener(on_press=on_press) as k_listener:
        k_listener.join()
    
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program stopped by User")
    finally:
        robot.env_detection.servo.mid() 