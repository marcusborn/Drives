import matplotlib.pyplot as plt

#This is the drives system ex 1 torque and power
##'''A brochure of a passenger car contains the following data:
##Maximum torque of the internal combustion engine:
##150 Nm at 3000 rpm
##Torque range of the internal combustion engine:
##90% of the maximum torque from 2000 rpm to 5000 rpm
##Please draw the torque and power diagrams for this internal combustion
##engine!'''

max_torque = 150 #Nm
max_torque_rpm = 3000
pi = 3.14215

n = list(range(0,5001))
#90% of max torque from 2000rpm to 5000rpm

#IMPORTANT FORMULA P[W] = Torque[Nm] x n[1/s]
print("Important formula --> Power = 2*pi * n[1/s] * torque[Nm]")

print("\n\nPower @ 2000rpm = 2*pi * ( 2000[1/min] / 60[s] )* 0.9*150[Nm] ")
p_2000 = 2*pi * ( n[2000] / 60 )* 0.9*max_torque
print("Power @2000rpm = " + str(round(p_2000,2)) + " W")



print("\n\nPower @ 3000rpm = 2*pi * ( 3000[1/min] / 60[s] )* 150[Nm] ")
p_3000 = 2*pi * ( n[3000] / 60 )* max_torque
print("Power @3000rpm = " + str(round(p_3000,2)) + " W")


print("\n\nPower @ 5000rpm = 2*pi * ( 5000[1/min] / 60[s] )* 150[Nm] ")
p_5000 = 2*pi * ( n[5000] / 60 )* 0.9*max_torque
print("Power @5000rpm = " + str(round(p_5000,2)) + " W")


#Graph this with matplot lib

print("\n\n\n T @2000rpm = 150 * 0.9 = 135 [Nm],\n T @ 3000rpm = 150[Nm],\n T @ 5000rpm = 150 * 0.9 = 135[Nm]")

power = [p_2000/1000, p_3000/1000, p_5000/1000] #for y2 ax
torque = [135, 150, 135] #for y1 ax
rpm = [2000,3000,5000] #for x ax


fig, ax1 = plt.subplots()
fig.suptitle('Torque, Power, RPM diagram')
ax1.set_xlabel('n(rpm)')
ax1.set_xlim([0,6000])
ax1.set_xticks([0,1000,2000,3000,4000,5000])
ax1.set_ylim([0,176])
ax1.set_yticks(list(range(0, 176,25)))
ax1.set_ylabel('Torque(Nm)', color='r')
ax1.tick_params(axis='y', labelcolor='r')
ax1.plot(rpm, torque, color='r', label='Torque')
ax1.scatter(rpm, torque, color='r')

ax2 = ax1.twinx() #instantiate 2nd axis
ax2.set_ylabel('Power(kW)', color='b')
ax2.set_ylim([0,80])
ax2.set_yticks([0,20,40,60,80])
ax2.tick_params(axis='y', labelcolor='b')
ax2.plot(rpm, power, color='b', label='Power')
ax2.scatter(rpm, power, color='b')

#plt.legend()
plt.show()








