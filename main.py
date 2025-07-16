from controller import Robot
from controller import LED
# create the Robot instance.
robot = Robot()
c=0
wall_left=0
wall_right=0
m=0
j=0
p=1
last=0
junction=0
track=0
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

led=[]
led_names=["led_middle","led_right","led_left"]

for name in led_names:
    led.append(robot.getDevice(name))
    led[-1].set(0)
    
    
ds=[]
ds_names=["ir_ext_right","ir_ext_left","ir_right","ir_left","ds_front","ds_right","ds_left","ds_left_rear","ds_right_rear","ds_rear"]
ds_val=[0]*len(ds_names)

for name in ds_names:
    ds.append(robot.getDevice(name))
    ds[-1].enable(timestep)
         
wheels=[]
wheel_names=['front_right_wheel','front_left_wheel','rear_right_wheel','rear_left_wheel']

for name in wheel_names:
         wheels.append(robot.getDevice(name))
         wheels[-1].setPosition(float('inf'))
         wheels[-1].setVelocity(0.0)
         
last_error=intg=diff=prop=waitCounter=0
kp = 0.005
ki = 0
kd = 0.015

def pid(error):
    global last_error, intg, diff , prop, kp, ki, kd
    prop= error
    intg= error+intg
    diff= error - last_error
    balance= (kp*prop)+(ki*intg)+(kd*diff)
    last_error= error
    return balance
    
def setSpeed(base_speed,balance):
     if base_speed+balance>10: base_speed+balance==10
     if base_speed-balance>10: base_speed-balance==10
     if base_speed+balance<-10: base_speed+balance==-10
     if base_speed-balance<=-10: base_speed+balance==-10
     wheels[0].setVelocity(base_speed+balance)
     wheels[1].setVelocity(base_speed-balance)
     wheels[2].setVelocity(base_speed+balance)
     wheels[3].setVelocity(base_speed-balance)
     
     

while robot.step(timestep) != -1:
      for i in range (len(ds)):
            ds_val[i]=ds[i].getValue()
            print(f"{ds_names[i]}:{ds_val[i]}\n"+"*"*40)
            
      if 1000 in ds_val[0:2] and ds_val[4]==1000:
        if ds_val[0]==1000 and ds_val[1]==1000 and ds_val[2]!=1000 and ds_val[3]!=1000:
             setSpeed(4,0)
             track=1
             print("case 0")
             if ds_val[6]<1000:
                wall_left=1
                led[2].set(2)
                print("wall on left")
             elif wall_left==1:
               c=c+1
               led[2].set(0)
               print("wall on left",c)
               wall_left=0
              
         
         
             if ds_val[5]<1000:
               wall_right=1
               led[1].set(2)
               print("wall on right")
             elif wall_right==1:
                m=m+1
                led[1].set(0)
                print("wall on right",m)
                wall_right=0
                        
        elif ds_val[0]==1000 and ds_val[1]==1000 and ds_val[2]==1000 and ds_val[3]!=1000:
             setSpeed(4,5)
             print("case 1")
        elif ds_val[0]==1000 and ds_val[1]==1000 and ds_val[2]!=1000 and ds_val[3]==1000: 
             setSpeed(4,-5)
             print("case 2")
        elif ds_val[0]!=1000 and ds_val[1]==1000 and ds_val[2]!=1000 and ds_val[3]==1000:#lane following 
             setSpeed(4,0)
             track=0#changed now
             print("case 3")
        elif ds_val[0]!=1000 and ds_val[1]==1000 and ds_val[2]!=1000 and ds_val[3]!=1000:#lane following 
             setSpeed(4, 5)
             print("case 4")
        elif ds_val[0]!=1000 and ds_val[1]==1000 and ds_val[2]==1000 and ds_val[3]==1000:#lane following 
             setSpeed(4, -5)
             print("case 5")
       
                  
        elif ds_val[0]==1000 and ds_val[1]!=1000 and ds_val[2]==1000 and ds_val[3]!=1000:#lane following 
             setSpeed(4, 0)
             track=0#changed now
             print("case 6")
        elif ds_val[0]==1000 and ds_val[1]!=1000 and ds_val[2]==1000 and ds_val[3]==1000:#lane following 
             setSpeed(4, 5)
             print("case 7")
        elif ds_val[0]==1000 and ds_val[1]!=1000 and ds_val[2]!=1000 and ds_val[3]!=1000:#lane following 
             setSpeed(4,-5)
             print("case 8")
        elif ds_val[0]==1000 and ds_val[1]==1000 and ds_val[2]==1000 and ds_val[3]==1000:
             setSpeed(4, 0)
             d=c+m+j
             print("NUMBER OF JUNCTION + OBSTACLES =",d)
             led[2].set(d%2)
             d=d//2
             print("d=",d)
             led[0].set(d%2)
             d=d//2
             print("d=",d)
             led[1].set(d%2)
             
      else:
           
              #changed 
             if ds_val[4]!=1000  and ds_val[5]!=1000:
                
                print("turn left")
                setSpeed(0,8)
                
             elif ds_val[4]!=1000  and ds_val[6]!=1000:
          
                print("turn right")
                setSpeed(0,-8)   
             elif ds_val[5]!=1000 and ds_val[6]==1000:
                last=1
                
                error=((ds_val[5]+ds_val[8])/2-500)
                print(error)
                print(ds_val[5])
                rectify = pid(error)
                print(-rectify)
                setSpeed(2,-rectify) 
                
             elif ds_val[6]!=1000 and ds_val[5]==1000:
                last=1
                led[0].set(0) 
                led[1].set(0)
                led[2].set(0)
                
                avg=(ds_val[6]+ds_val[7])/2
                error=(avg-500)
                print(error)
                print(ds_val[6])
                rectify = pid(error)
                print(-rectify)
                setSpeed(2,-rectify) 
                
             
            
             elif ds_val[6]!=1000 and ds_val[5]!=1000 and ds_val[4]==1000:
             
                led[0].set(0) 
                led[1].set(0)
                led[2].set(0)
               
                error=((ds_val[6]-ds_val[5])-0)
                print(error)
                print(ds_val[6])
                print(ds_val[5])
                rectify = pid(error)
                print(rectify)
                setSpeed(2,rectify)  
                
            
             
             elif ds_val[4]==1000 and ds_val[5]==1000 and ds_val[6]==1000 and ds_val[7]!=1000:
                 setSpeed(2,5)
                 
             elif ds_val[4]==1000 and ds_val[5]==1000 and ds_val[6]==1000 and ds_val[8]!=1000:
                 setSpeed(2,-5)      
                   
            
             
                
 #junction counting +led
      if ds_val[0]!=1000 and ds_val[1]!=1000 and ds_val[2]!=1000 and ds_val[3]!=1000 and ds_val[4]==1000 and ds_val[5]==1000 and ds_val[6]==1000 and ds_val[7]==1000 and ds_val[8]==1000 and track==1:
            setSpeed(4,0)
            junction=1
            print("junction detected")
            led[0].set(2)
            led[1].set(2)
            led[2].set(2)
         
      elif junction==1:
            j=j+1
            led[0].set(0) 
            led[1].set(0)
            led[2].set(0)
         
            print("junction count = ",j)
            junction=0    
     
      if last==1 :
         
         if ds_val[1]==1000 and ds_val[3]==1000 and ds_val[2]==1000 and ds_val[0]==1000:
            #setSpeed(2,0)
            led[0].set(2)
            led[1].set(2)
            led[2].set(2)
            
         if ds_val[1]!=1000 and ds_val[3]!=1000 and ds_val[2]!=1000 and ds_val[0]!=1000 and ds_val[4]==1000 and ds_val[5]==1000 and ds_val[6]==1000 and ds_val[7]==1000 and ds_val[8]==1000 and ds_val[9]!=1000:
            setSpeed(0,0)
            
            led[0].set(0)
            led[1].set(0)
            led[2].set(0)
            
         if ds_val[1]!=1000 and ds_val[3]!=1000 and ds_val[2]!=1000 and ds_val[0]!=1000 and ds_val[4]==1000 and ds_val[5]==1000 and ds_val[6]==1000 and ds_val[7]==1000 and ds_val[8]==1000 and ds_val[9]==1000:
            setSpeed(2,0)
            
            
                
                   
