from settings import *
from gpiozero import Servo, AngularServo, DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from typing import Tuple, List

class ServoMain(AngularServo):
    def __init__(self):
        factory = PiGPIOFactory()
        super().__init__(pin=SERVO_PIN, initial_angle=SERVO_INIT_ANGLE, min_angle=SERVO_MIN_ANGLE, max_angle=SERVO_MAX_ANGLE, min_pulse_width=SERVO_MIN_PULSE_WIDTH, max_pulse_width=SERVO_MAX_PULSE_WIDTH, frame_width=SERVO_FRAME_WIDTH, pin_factory=factory)


class ServoJump(ServoMain):
    def __init__(self):
        super().__init__()
    
    def move_to_angle(self, angle:float) -> None:
        assert -90 <= angle <= 90, "The angle must be between -90 degrees and 90 degrees."
        self.angle = angle


class DistanceSensorMain(DistanceSensor):
    def __init__(self):#, queue_len, threshold_distance, partial):
        factory = PiGPIOFactory()
        #super().__init__(echo=ECHO_PIN, trigger=TRIG_PIN, queue_len=queue_len, max_distance=MAX_DIST, threshold_distance=threshold_distance, partial=partial, pin_factory=factory)
        super().__init__(echo=ECHO_PIN, trigger=TRIG_PIN, max_distance=MAX_DIST, pin_factory=factory)

        
class EnvDetection:
    def __init__(self, servo=None, dist_sensor=None) -> None:
        self.servo = servo if isinstance(servo, Servo) else ServoJump()
        self.dist_sensor = dist_sensor if isinstance(dist_sensor, DistanceSensor) else DistanceSensorMain()
    
    def sweep(
            self,
            start_angle=None, 
            end_angle=None, 
            stops_num=10, 
            period_per_stop = 0.5
    ) -> List[Tuple[float, float]]:
        
        distance_data = []
        
        if start_angle == None:
            start_angle = self.servo.min_angle
        if end_angle == None:
            end_angle = self.servo.max_angle
        
        delta_angle = (end_angle-start_angle)/(stops_num-1)

        for i_stop in range(stops_num):
            self.servo.angle = start_angle + delta_angle*i_stop
            sleep(period_per_stop)
            measured_dist = round(self.dist_sensor.distance*100, 1)
            distance_data.append([self.servo.angle, measured_dist])
        
        return distance_data