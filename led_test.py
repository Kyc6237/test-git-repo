# boolean 변수 설정
light_on = False
# button_callback 함수를 정의

def button_callback(channel):
  global light_on           # Global 변수 선언
  if light_on = False:      # LED 불이 꺼져 있을 때
    GPIO.output(led_pin,1)  # LED ON
    print("LED ON!")
    
  else:                     # LED 불이 켜져 있을 때
    GPIO.output(led_pin,0)  # LED OFF
    print("LED OFF!")
  light_on = not light_on   # False <=> True
