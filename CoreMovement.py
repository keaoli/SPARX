from adafruit_servokit import ServoKit
import time
 #import the servokit library (from circuitpython0 If you are using
 #a raspberry pi you will need additional libraries

kit = ServoKit(channels=16) #set up the kit object for servos plus channels
#channels = to the channels on your controller, this was done with an adafruit
#PCA9685 which has 36 servo channels.

#pick a direction for your quadruped to face before defining these, it will make it easier
RFP = kit.servo[0] #Right Front Pivot (the corner hip servo)
LFP = kit.servo[4] #Left Front Pivot
RBP = kit.servo[12] # Right Back Pivot
LBP = kit.servo[8] # Left Back Pivot

RFL = kit.servo[1] #Right Front Lift servo (the knee servo)
LFL = kit.servo[6] #Left Front :ift
RBL = kit.servo[13] #Right Back Lift
LBL = kit.servo[9] #Left Back Lift

#these designations are fairly arbitrary, the quad is symmetrical but it helps to think of a "front"

RFPCal = -5 #calibration values, servos may be slightly off center, these will allow for that
LFPCal = 0
RBPCal = 5
LBPCal = 5

RFLCal = -5
LFLCal = 20
RBLCal = 5
LBLCal = 0


#find these values by setting the pivot servos to 90 degrees then adding or subtracting single degrees
# until each leg points at a 45 degree angle from the body

#servo positions (calibration allowed for)
RFP90 = (90+RFPCal)
RFP120 = (120+RFPCal)
RFP150 = (150+RFPCal)
RFP180 = (180+RFPCal)

LFP90 = (90+LFPCal)
LFP120 = (120+LFPCal)
LFP150 = (150+LFPCal)
LFP180 = (180+LFPCal)

RBP0 = (0+RBPCal)
RBP30 = (30+RBPCal)
RBP60 = (60+RBPCal)
RBP90 = (90+RBPCal)

LBP0 = (0+LBPCal)
LBP30 = (30+LBPCal)
LBP60 = (60+LBPCal)
LBP90 = (90+LBPCal)

#using these variables should allow repeatable results
#allowed for these variables within the srv function so they arent used, kept them incase

OverallSpeed = 0.003 #speed of motion, defined by a wait between actions.faster speeds can be experimented with

RFPCurr = 90 #holds current position of servos
LFPCurr = 90 #these ignore calibration because they are "imagined" positions, for the purpose of MATHS
RBPCurr = 90
LBPCurr = 90

RFLCurr = 90
LFLCurr = 90
RBLCurr = 90
LBLCurr = 90

def srv(PLFP, PLBP, PRBP, PRFP, PLFL, PLBL, PRBL, PRFL, SP1, SP2, SP3, SP4):
    #PLFP : positionto move Left Front Pivot servo to
    #PLBP : Position for Left Back Pivot
    #PRBP : Position for Right Back Pivot
    #PRFP : Position for Right Front Pivot
    #PLFL : Position for Left Front Lift servo
    #PLBL : Position for Left Back Lift servo
    #PRBL: : Position for Right Back Lift servo
    #PRFL: Position for Right Front Lift servo
    # SP1-SP4 : Speed values, amount of degrees to move each servo by each loop
    global RFPCurr# = 90 #holds current position of servos
    global LFPCurr #= 90 #these ignore calibration because they are "imagined" positions, for the purpose of MATHS
    global RBPCurr #= 90
    global LBPCurr# = 90

    global RFLCurr# = 90
    global LFLCurr# = 90
    global RBLCurr# = 90
    global LBLCurr# = 90
    
    #global SP1
    #global SP2
    #global SP3
    #global SP4
    
    
    while PLFP != LFPCurr or PLBP != LBPCurr or PRBP != RBPCurr or PRFP != RFPCurr or PLFL != LFLCurr or PLBL != LBLCurr or PRBL != RBLCurr or PRFL != RFLCurr :
        
        if LFPCurr < PLFP:
            if (LFPCurr + SP1) <= PLFP:
                LFPCurr = LFPCurr + SP1
            else:
                LFPCurr = PLFP
            
        if (LFPCurr > PLFP): #Left Front Pivot servo
            if (LFPCurr - SP1) >= PLFP:
                LFPCurr = LFPCurr - SP1
            else:
                LFPCurr = PLFP
        #time.sleep(0.002)        
        if (LBPCurr < PLBP) :#Left Front Pivot servo
            if (LBPCurr + SP2) <= PLBP:
                LBPCurr = LBPCurr + SP2
            else:
                LBPCurr = PLBP
                
        if (LBPCurr > PLBP): #Left Front Pivot servo
            if (LBPCurr - SP2) >= PLBP:
                LBPCurr = LBPCurr - SP2
            else:
                LBPCurr = PLBP
        #time.sleep(0.002)           
        if (RBPCurr < PRBP): #Left Front Pivot servo
            if (RBPCurr + SP3) <= PRBP:
                RBPCurr = RBPCurr + SP3
            else:
                RBPCurr = PRBP
                
        if (RBPCurr > PRBP): #Left Front Pivot servo
            if (RBPCurr - SP3) >= PRBP:
                RBPCurr = RBPCurr - SP3
            else:
                RBPCurr = PRBP
        #time.sleep(0.002)           
        if (RFPCurr < PRFP) :#Left Front Pivot servo
            if (RFPCurr + SP4) <= PRFP:
                RFPCurr = RFPCurr + SP4
            else:
                RFPCurr = PRFP
                
                   
        if (RFPCurr > PRFP): #Left Front Pivot servo
            if (RFPCurr - SP4) >= PRFP:
                RFPCurr = RFPCurr - SP4
            else:
                RFPCurr = PRFP
        #time.sleep(0.002)           
        if (LFLCurr < PLFL):#Left Front Pivot servo
            if (LFLCurr + SP1) <= PLFL:
                LFLCurr = LFLCurr + SP1
            else:
                LFLCurr = PLFL
                
                
        if (LFLCurr > PLFL): #Left Front Pivot servo
            if (LFLCurr - SP1) >= PLFL:
                LFLCurr = LFLCurr - SP1
            else:
                LFLCurr = PLFL
        #time.sleep(0.002)           
        if (LBLCurr < PLBL) :#Left Front Pivot servo
            if (LBLCurr + SP2) <= PLBL:
                LBLCurr = LBLCurr + SP2
            else:
                LBLCurr = PLBL
                
        if (LBLCurr > PLBL): #Left Front Pivot servo
            if (LBLCurr - SP2) >= PLBL:
                LBLCurr = LBLCurr - SP2
            else:
                LBLCurr = PLBL
        #time.sleep(0.002)       
        if (RBLCurr < PRBL) :#Left Front Pivot servo
            if (RBLCurr + SP3) <= PRBL:
                RBLCurr = RBLCurr + SP3
            else:
                RBLCurr = PRBL

        if (RBLCurr > PRBL) :#Left Front Pivot servo
            if (RBLCurr - SP3) >= PRBL:
                RBLCurr = RBLCurr - SP3
            else:
                RBLCurr = PRBL
        #time.sleep(0.002)   
        if (RFLCurr < PRFL) :#Left Front Pivot servo
            if (RFLCurr + SP4) <= PRFL:
                RFLCurr = RFLCurr + SP4
            else:
                RFLCurr = PRFL

        if (RFLCurr > PRFL) :#Left Front Pivot servo
            if (RFLCurr - SP4) >= PRFL:
                RFLCurr = RFLCurr - SP4
            else:
                RFLCurr = PRFL
        #time.sleep(0.002)
        
        if (LFLCurr+LFLCal) >= 0 and (LFLCurr+LFLCal) <= 180 :
        
            LFL.angle = LFLCurr + LFLCal
        if (LBLCurr+LBLCal) >= 0 and (LBLCurr+LBLCal) <= 180 :
            LBL.angle = LBLCurr + LBLCal
        if (RBLCurr+RBLCal) >= 0 and (RBLCurr+RBLCal) <= 180 :
            RBL.angle = RBLCurr + RBLCal
        if (RFLCurr+RFLCal) >= 0 and (RFLCurr+RFLCal) <= 180 :
            RFL.angle = RFLCurr + RFLCal
        
        if (LFPCurr+LFPCal) >= 0 and (LFPCurr+LFPCal) <= 180 :
            
            LFP.angle = LFPCurr + LFPCal
        if (LBPCurr+LBPCal) >= 0 and (LBPCurr+LBPCal) <= 180 :
            LBP.angle = LBPCurr + LBPCal
        if (RFPCurr+RFPCal) >= 0 and (RFPCurr+RFPCal) <= 180 :
            RFP.angle = RFPCurr + RFPCal
        if (RBPCurr+RBPCal) >= 0 and (RBPCurr+RBPCal) <= 180 :
            RBP.angle = RBPCurr + RBPCal
     #This ufly block of code makes sure that an angle below 0 or above 180 is sent to each servo
     #this could cause problems , a better option might be to set to exacxtly 0 or 180       
        
            
        time.sleep(OverallSpeed)
        #sleep for the overall speed, not ACTUALLY required for motion
        
def srv2(PLFP, PLBP, PRBP, PRFP, PLFL, PLBL, PRBL, PRFL, SP1, SP2, SP3, SP4):
    #secondary serv function processing each movement in a different order, to possibly
    #improve gait, not used in current code, still a WIP
    #PLFP : positionto move Left Front Pivot servo to
    #PLBP : Position for Left Back Pivot
    #PRBP : Position for Right Back Pivot
    #PRFP : Position for Right Front Pivot
    #PLFL : Position for Left Front Lift servo
    #PLBL : Position for Left Back Lift servo
    #PRBL: : Position for Right Back Lift servo
    #PRFL: Position for Right Front Lift servo
    # SP1-SP4 : Speed values, amount of degrees to move each servo by each loop
    global RFPCurr# = 90 #holds current position of servos
    global LFPCurr #= 90 #these ignore calibration because they are "imagined" positions, for the purpose of MATHS
    global RBPCurr #= 90
    global LBPCurr# = 90

    global RFLCurr# = 90
    global LFLCurr# = 90
    global RBLCurr# = 90
    global LBLCurr# = 90
    
    #global SP1
    #global SP2
    #global SP3
    #global SP4
    
    while PLFL != LFLCurr or PLBL != LBLCurr or PRBL != RBLCurr or PRFL != RFLCurr :
        if (LFLCurr < PLFL):#Left Front Pivot servo
            if (LFLCurr + SP1) <= PLFL:
                LFLCurr = LFLCurr + SP1
            else:
                LFLCurr = PLFL
        if (LFLCurr > PLFL): #Left Front Pivot servo
            if (LFLCurr - SP1) >= PLFL:
                LFLCurr = LFLCurr - SP1
            else:
                LFLCurr = PLFL
        time.sleep(0.002)           
        if (LBLCurr < PLBL) :#Left Front Pivot servo
            if (LBLCurr + SP2) <= PLBL:
                LBLCurr = LBLCurr + SP2
            else:
                LBLCurr = PLBL
                
        if (LBLCurr > PLBL): #Left Front Pivot servo
            if (LBLCurr - SP2) >= PLBL:
                LBLCurr = LBLCurr - SP2
            else:
                LBLCurr = PLBL
        time.sleep(0.002)       
        if (RBLCurr < PRBL) :#Left Front Pivot servo
            if (RBLCurr + SP3) <= PRBL:
                RBLCurr = RBLCurr + SP3
            else:
                RBLCurr = PRBL

        if (RBLCurr > PRBL) :#Left Front Pivot servo
            if (RBLCurr - SP3) >= PRBL:
                RBLCurr = RBLCurr - SP3
            else:
                RBLCurr = PRBL
        time.sleep(0.002)   
        if (RFLCurr < PRFL) :#Left Front Pivot servo
            if (RFLCurr + SP4) <= PRFL:
                RFLCurr = RFLCurr + SP4
            else:
                RFLCurr = PRFL

        if (RFLCurr > PRFL) :#Left Front Pivot servo
            if (RFLCurr - SP4) >= PRFL:
                RFLCurr = RFLCurr - SP4
            else:
                RFLCurr = PRFL
        time.sleep(0.001)
        
        if (LFLCurr+LFLCal) >= 0 and (LFLCurr+LFLCal) <= 180 :
        
            LFL.angle = LFLCurr + LFLCal
        if (LBLCurr+LBLCal) >= 0 and (LBLCurr+LBLCal) <= 180 :
            LBL.angle = LBLCurr + LBLCal
        if (RBLCurr+RBLCal) >= 0 and (RBLCurr+RBLCal) <= 180 :
            RBL.angle = RBLCurr + RBLCal
        if (RFLCurr+RFLCal) >= 0 and (RFLCurr+RFLCal) <= 180 :
            RFL.angle = RFLCurr + RFLCal
    
    while PLFP != LFPCurr or PLBP != LBPCurr or PRBP != RBPCurr or PRFP != RFPCurr : 
        
        if LFPCurr < PLFP:
            if (LFPCurr + SP1) <= PLFP:
                LFPCurr = LFPCurr + SP1
            else:
                LFPCurr = PLFP
            
        if (LFPCurr > PLFP): #Left Front Pivot servo
            if (LFPCurr - SP1) >= PLFP:
                LFPCurr = LFPCurr - SP1
            else:
                LFPCurr = PLFP
        time.sleep(0.002)        
        if (LBPCurr < PLBP) :#Left Front Pivot servo
            if (LBPCurr + SP2) <= PLBP:
                LBPCurr = LBPCurr + SP2
            else:
                LBPCurr = PLBP
                
        if (LBPCurr > PLBP): #Left Front Pivot servo
            if (LBPCurr - SP2) >= PLBP:
                LBPCurr = LBPCurr - SP2
            else:
                LBPCurr = PLBP
        time.sleep(0.002)           
        if (RBPCurr < PRBP): #Left Front Pivot servo
            if (RBPCurr + SP3) <= PRBP:
                RBPCurr = RBPCurr + SP3
            else:
                RBPCurr = PRBP
                
        if (RBPCurr > PRBP): #Left Front Pivot servo
            if (RBPCurr - SP3) >= PRBP:
                RBPCurr = RBPCurr - SP3
            else:
                RBPCurr = PRBP
        time.sleep(0.002)           
        if (RFPCurr < PRFP) :#Left Front Pivot servo
            if (RFPCurr + SP4) <= PRFP:
                RFPCurr = RFPCurr + SP4
            else:
                RFPCurr = PRFP
                
                   
        if (RFPCurr > PRFP): #Left Front Pivot servo
            if (RFPCurr - SP4) >= PRFP:
                RFPCurr = RFPCurr - SP4
            else:
                RFPCurr = PRFP
        time.sleep(0.001)           
        
        if (LFPCurr+LFPCal) >= 0 and (LFPCurr+LFPCal) <= 180 :
            
            LFP.angle = LFPCurr + LFPCal
        if (LBPCurr+LBPCal) >= 0 and (LBPCurr+LBPCal) <= 180 :
            LBP.angle = LBPCurr + LBPCal
        if (RFPCurr+RFPCal) >= 0 and (RFPCurr+RFPCal) <= 180 :
            RFP.angle = RFPCurr + RFPCal
        if (RBPCurr+RBPCal) >= 0 and (RBPCurr+RBPCal) <= 180 :
            RBP.angle = RBPCurr + RBPCal
      
        
            
        time.sleep(0.001)
        
def changespeed(spdchange):
    
    global OverallSpeed
    
    OverallSpeed = OverallSpeed + spdchange
    #command to allow changing the time between motions, using a global like this isnt recommended but it works.
    
                
def forward():
    #work in profress walk gait, not used.
    srv(180, 0 , 120, 60, 82,  73,  73,  82,  2,  6,  2,  2)
    time.sleep(2)
    srv( 90, 30, 90,  30, 36,   73,  73,  82,  6,  2,  2,  2)
    time.sleep(2)
    srv( 90, 30, 90,  30, 82,  73,  73,  82,  6,  2,  2,  2)
    time.sleep(2)
    srv( 90, 60, 90,  30, 82,  73,  73,  82,  6,  2,  2,  2)
    time.sleep(2)
    srv( 90, 60, 90,  30, 82,  73,  36,  82,  6,  2,  2,  2)
    time.sleep(2)
    srv(120, 60, 180, 0,  82,  73,  36,   82,  2,  2,  6,  2)
    time.sleep(2)
    srv(120, 60, 180, 0,  82,  73,  73,  36,  2,  2,  6,  2)
    time.sleep(2)
    srv(150, 90, 150, 90, 82,  73,  100,  36,   2,  2,  2,  6)
    srv(150, 90, 150, 90, 82,  73,  100,  82,   2,  2,  2,  6)
    time.sleep(2)
    srv(150, 90, 150, 90, 82,  36,  100,  82,  2,  2,  2,  6)
    time.sleep(2)
    srv(180, 0,  120, 60, 82,  73,   73,  82,  2,  6,  2,  2)
    
def for2():
    #second work in progress walk gate, not used
    srv2(180, 0 , 90, 90, 90,  90,  90,  90,  3,  3,  3,  3)
    time.sleep(2)
    srv2( 40, 0, 90,  90, 30,   90,  90,  90,  3,  1,  1,  1)
    time.sleep(2)
    srv2( 90, 90, 30,  0, 90,  90,  90,  90,  3,  3,  3,  3)
    time.sleep(2)
    srv2(90, 90, 180, 0,  90,  90,  36,   90,  3,  3,  3,  3)
    time.sleep(2)
    srv2(90, 90, 180, 150,  90,  90,  90,  30,  3,  3,  3,  3)
    time.sleep(2)
    srv2(180, 140, 90, 90, 90,  90,  90, 90,   3,  3,  3,  3)
    time.sleep(2)
    srv2(180, 0, 90, 90, 90,  30, 90,  90,  3, 3,  3,  3)
    
    #srv(180, 0,  120, 60, 82,  36,   73,  82,  1,  3,  1,  1)
def forwardbase():
    #the walk gait we use, simple and taken directly from original code, not perfect.
    srv(180, 0 , 120, 60, 72,  63,  63,  72,  1,  3,  1,  1);
    srv( 90, 30, 90,  30, 36,   63,  63,  72,  3,  1,  1,  1);
    srv( 90, 30, 90,  30, 72,  63,  63,  72,  3,  1,  1,  1);
    srv(120, 60, 180, 0,  72,  63,  36,   72,  1,  1,  3,  1);
    srv(120, 60, 180, 0,  72,  63,  63,  72,  1,  1,  3,  1);
    srv(150, 90, 150, 90, 72,  63,  63,  36,   1,  1,  1,  3);
    srv(150, 90, 150, 90, 72,  63,  63,  72,  1,  1,  1,  3);
    srv(180, 0,  120, 60, 72,  36,   63,  72,  1,  3,  1,  1);

def backbase():
    #basic backwards walk, something isnt perfect with it as of writing this
    srv(180, 0,  120, 60, 72, 63, 63, 72, 3,  1, 1, 1);
    srv(150, 90, 150, 90, 72, 48, 63, 72, 1,  3, 1, 1);
    srv(150, 90, 150, 90, 72, 63, 63, 72, 1,  3, 1, 1);
    srv(120, 60, 180, 0,  72, 63, 63, 36,  1,  1, 1, 3);
    srv(120, 60, 180, 0,  72, 63, 63, 72, 1,  1, 1, 3);
    srv(90,  30, 90,  30, 72, 63, 48, 72, 1,  1, 3, 1);
    srv(90,  30, 90,  30, 72, 63, 63, 72, 1,  1, 3, 1);
    srv(180, 0,  120, 60, 36,  63, 63, 72, 3,  1, 1, 1);

def baseleft():
    #turn left, drifts slightly
    srv(150,  90, 90,  30, 72, 36,  63, 72, 1, 3, 1, 1);
    srv(150,  90, 90,  30, 72, 63, 63, 72, 1, 3, 1, 1);
    srv(120,  60, 180, 0,  72, 63, 36,  72, 1, 1, 3, 1);
    srv(120,  60, 180, 0,  72, 63, 63, 54, 1, 1, 3, 1);
    srv(90,   30, 150, 90, 72, 63, 63, 36,  1, 1, 1, 3);
    srv(90,   30, 150, 90, 72, 63, 63, 72, 1, 1, 1, 3);
    srv(180,  0,  120, 60, 36,  63, 63, 72, 3, 1, 1, 1);
    srv(180,  0,  120, 60, 72, 63, 63, 63, 3, 1, 1, 1);
def baseright():
    #turn right, drifts slightly
    srv( 90, 30, 150, 90, 36,  63, 63, 72, 3, 1, 1, 1);
    srv( 90, 30, 150, 90, 72, 63, 63, 72, 3, 1, 1, 1);
    srv(120, 60, 180, 0,  72, 63, 63, 36,  1, 1, 1, 3);
    srv(120, 60, 180, 0,  72, 63, 63, 72, 1, 1, 1, 3);
    srv(150, 90, 90,  30, 72, 63, 36,  72, 1, 1, 3, 1);
    srv(150, 90, 90,  30, 72, 63, 63, 72, 1, 1, 3, 1);
    srv(180, 0,  120, 60, 72, 36,  63, 72, 1, 3, 1, 1);
    srv(180, 0,  120, 60, 72, 63, 63, 72, 1, 3, 1, 1);
def center_servos():
    #center the servos, self explanatory.
    RFP.angle = RFP90
    time.sleep(0.001)
    RFL.angle = 90 + RFLCal
    time.sleep(0.001)
    LFP.angle = LFP90
    time.sleep(0.001)
    LFL.angle = 90 + LFLCal
    time.sleep(0.001)
    RBP.angle = RBP90
    time.sleep(0.001)
    RBL.angle = 90 + RBLCal
    time.sleep(0.001)
    LBP.angle = LBP90
    time.sleep(0.001)
    LBL.angle = 90 + LBLCal

    
   
    RFPCurr = 90 #holds current position of servos
    LFPCurr = 90
    RBPCurr = 90
    LBPCurr = 90

    RFLCurr = 90
    LFLCurr = 90
    RBLCurr = 90
    LBLCurr = 90

def lean_left():
    # lean to the left, used for the Dance function
    LFL.angle = 150 + LFLCal
    LBL.angle = 150 + LBLCal
    RFL.angle = 15 + RFLCal
    RBL.angle = 15 + RBLCal
    
def lean_right():
    #lean to the right, used for the dance function
    LFL.angle = 15 + LFLCal
    LBL.angle = 15 + LBLCal
    RFL.angle = 150 + RFLCal
    RBL.angle = 150 + RBLCal

def bow():
    #a little bow, used for the dance
    center_servos()
    time.sleep(0.2)
    LFL.angle = 15 + LFLCal
    RFL.angle = 15 + RFLCal
    time.sleep(0.7)
    LFL.angle = 90 + LFLCal
    RFL.angle = 90 + RFLCal
    
def dance():
    #a cute but jerky dance
    center_servos()
    time.sleep(0.1)
    lean_left()
    time.sleep(0.3)
    lean_right()
    time.sleep(0.3)
    lean_left()
    time.sleep(0.3)
    lean_right()
    time.sleep(0.3)
    lean_left()
    time.sleep(0.3)
    lean_right()
    time.sleep(0.3)
    lean_left()
    time.sleep(0.3)
    lean_right()
    time.sleep(0.8)
    center_servos()
    time.sleep(0.3)
    bow()
    time.sleep(0.1)
    center_servos()

def twerk(): # dont ask
    center_servos()
    RFL.angle = 15 + RBLCal
    LFL.angle = 15 + LBLCal
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    RBL.angle = 360 + RBLCal
    LBL.angle = 360 + LBLCal
    time.sleep(0.1)
    RBL.angle = 100 + RBLCal
    LBL.angle = 100 + LBLCal
    time.sleep(0.1)
    center_servos()

#everything below this is for testing, it will change and should be ignored.
center_servos()
time.sleep(5)
while True:
    baseright()
    




