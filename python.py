import time;
time2=time.time()
time1=time2+30
while time1>time2:
      time.sleep(5)	
      time1=time1+5
      print(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime()))
   