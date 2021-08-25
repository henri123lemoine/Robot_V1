from dataclasses import dataclass
from gpiozero import Motor
from settings import *
import time
from dataclasses import dataclass
from gpiozero import Motor
from time import sleep

@dataclass
class Wheels:
    left_motor: Motor = Motor(forward=LEFT_MOTOR_FORWARD_PIN, backward=LEFT_MOTOR_BACKWARD_PIN)
    right_motor: Motor = Motor(forward=RIGHT_MOTOR_FORWARD_PIN, backward=RIGHT_MOTOR_BACKWARD_PIN)

    def forward(self, speed: float = 1, period_s: float = 0.3):
        self.left_motor.forward(speed=speed)
        self.right_motor.forward(speed=speed)
        sleep(period_s)
        self.stop()

    def backward(self, speed: int = 1, period_s: int = 0.3):
        self.left_motor.backward(speed=speed)
        self.right_motor.backward(speed=speed)
        sleep(period_s)
        self.stop()

    def turn_right(self, speed: int = 1, period_s: int = 0.3):
        self.left_motor.forward(speed=speed)
        self.right_motor.backward(speed=speed)
        sleep(period_s)
        self.stop()

    def turn_left(self, speed: int = 1, period_s: int = 0.3):
        self.left_motor.backward(speed=speed)
        self.right_motor.forward(speed=speed)
        sleep(period_s)
        self.stop()

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()


