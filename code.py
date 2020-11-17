d=int(input())
r=int(input())
c=int(input())
speed_dif=c-r
meter_dif=50-d
if speed_dif==0:
 print("Meep Meep")
elif r==0 and c>r:
 print("Yum")
elif d/r<meter_dif/speed_dif:
 print("Meep Meep")
else:
 print("Yum")
