#Assignment_2
import random
import time
while(True):
    temperature = round(random.uniform(30,40),1)
    print("\tTemperature : "+str(temperature))
    humidity = random.randint(10,80)
    print("\tHumidity : "+str(humidity)+"\n")
    
    if(temperature > 36.5 and temperature < 37.5):
        print("\tNormal Body Temperature")
    else:
        print("\tAbnormal Body Temperature")

    if(humidity > 30 and humidity < 60):
        print("\tNormal Humidity")
    else:
        print("\tAbnormal Humidity")
    if((temperature > 36.5 and temperature < 37.5) and (humidity > 30 and humidity < 60)):
        print("\tAll is good, Stay Healthy !!")
        
    time.sleep(1)
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
