width = 2.40
height = 1.13
parts = 3
debug = 1
SashNum = 2

# Sum all 4 sides of Frames
FrameSum = ((width*2)+(height*2))*35000
if(debug==1): print("Frame:",FrameSum )
# Mullions
Mullions = ((parts-1)*(height))*30000
if(debug==1): print("Mullions:",Mullions )
# Sash
Sashes = SashNum*(((width/parts)*2)+(height*2))*30000
if(debug==1): print("Sashes:",Sashes )
# Interlock
Interlock = SashNum*((height)*7000)
if(debug==1): print("InterLock:",Interlock )
# Overlapping Cover
OCover = SashNum*((((width/parts)*2)+(height*2))*7000)
if(debug==1): print("Overlapping Cover:",OCover)
# Alminuim Rail
Arail = width * 5000
if(debug==1): print("Alminuim Rail:",Arail )
# Tape
Tape = (SashNum*(((width/parts)*2)+height))*700
if(debug==1): print("Tape:",Tape )
# Equipment
Equipment = SashNum*75000
if(debug==1): print("Equipment:",Equipment )
# Glass
Glass = ((width*height)*0.7)*50000
if(debug==1): print("Glass:",Glass)
# Installation Equipment
Iequip = SashNum*20000
if(debug==1): print("Installation Material:",Iequip )

FinalPrice = FrameSum+Mullions+Sashes+Interlock+OCover+Arail+Tape+Tape+Equipment+Glass+Iequip
FinalPrice += (FinalPrice*10)/100
if(debug==1): print("Installation Price: 10 Percent",(FinalPrice*10)/100)
print("Total price of Sliding Door and window:",FinalPrice)