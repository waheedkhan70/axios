def printIncreasingPower(x):
    
    base = 1
    current_power=base*base
   
    while(current_power <= x):
       
        
        print ( current_power, end = " ")
        
        base = base + 1
        
        current_power = base * base
       
