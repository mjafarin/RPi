import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11, True)
GPIO.output(11, False)
GPIO.output(11, True)
mah_pwm = GPIO.PWM(11,100)  #(pin,freq[Hz]);100Hz=1/10ms=1/10^-2=10^2=100 :)
#mah_pwm.start(100)
#mah_pwm.ChangeDutyCycle(25)
#mah_pwm.ChangeDutyCycle(10)
#mah_pwm.ChangeDutyCycle(1)
#mah_pwm.ChangeDutyCycle(25)
#mah_pwm.ChangeFrequency(50)
#mah_pwm.ChangeFrequency(100)
#mah_pwm.ChangeFrequency(200)
#mah_pwm.ChangeFrequency(1000)
#mah_pwm.ChangeFrequency(0.5)
#mah_pwm.ChangeFrequency(2)
mah_pwm.start(100)
#mah_pwm.ChangeDutyCycle(18)
#mah_pwm.ChangeDutyCycle(2)
mah_pwm.ChangeDutyCycle(1)
mah_pwm.stop()
GPIO.cleanup()

