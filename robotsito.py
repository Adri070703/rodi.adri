import rodi
import time

robot_wally = rodi.RoDI() #crar un objeto con la clase RoDI de nuestra libreria/archivo rodi.py y guardarlo en la variable robot_wally
# while True:
#     veo = robot_wally.sense()

#     '''
#     ojos = robot_wally.see()
    
#     for i in range(4):
#         robot_wally.led(1)
#        robot_wally.move_stop()   robot_wally.move(100,100)
#         time.sleep(3)
#         robot_wally.move_stop()

#         print(robot_wally.see())
        
#         robot_wally.led(0)
#         robot_wally.move_left()
#         time.sleep(0.5)
#         robot_wally.move_stop()
    
#     if ojos <= 10:
#         print(robot_wally.see())
#         robot_wally.move_stop()
#     else:
#         robot_wally.move_forward()
#     '''
#     if veo > [100,100]:
#         robot_wally.move_backward()
#         robot_wally.move_stop()
#     elif veo < [100,100]:
#         robot_wally.move_forward()
#         robot_wally.move_stop()

        

while True:


        sensor = robot_wally.sense()
        distancia = robot_wally.see()
        print(sensor)

        if distancia <= 40:
            robot_wally.move(100,100)
        else:
            robot_wally.move(-100,50)
            time.sleep(1)
            robot_wally.move_stop()
            time.sleep(1)
            print(robot_wally.see())


        if sensor[0] >= 100 or sensor[1] >= 100:
            robot_wally.move_stop()
            time.sleep(1)
            robot_wally.move_backward()
            time.sleep(1)
            robot_wally.move_left()
            time.sleep(0.5)

       

                        