import rodi
import time

robot_wally = rodi.RoDI() #crar un objeto con la clase RoDI de nuestra libreria/archivo rodi.py y guardarlo en la variable robot_wally
while True:
    ojos = robot_wally.see()
    '''
    for i in range(4):
        robot_wally.led(1)
        robot_wally.move(100,100)
        time.sleep(3)
        robot_wally.move_stop()

        print(robot_wally.see())
        
        robot_wally.led(0)
        robot_wally.move_left()
        time.sleep(0.5)
        robot_wally.move_stop()
    '''
    if ojos <= 10:
        print(robot_wally.see())
        robot_wally.move_stop()
    else:
        robot_wally.move_forward()