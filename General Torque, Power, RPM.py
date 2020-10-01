import matplotlib.pyplot as plt

pi = 3.14215
powers = []




##Enter the torque values in this array
torques = [174.8, 205, 176.2]  #original values from MX-5 3-point example

##Enter the RPM values for the torques
critical_rpms = [2300, 4000, 7200] #original values from MX-5 3-point example

##MX-5 additional data example comment out previous variables..
##critical_rpms = list(range(1500, 7301, 100)) 
##torques = [141.9, 147.8, 153, 157.6, 161.8, 165.5, 168.9, 172, 174.8, 177.4, 179.7, 181.9, 183.9, 185.8, 187.5, 189.2, 190.7, 192.1, 193.5, 194.7, 195.9, 197.1, 198.1, 199.1, 200.1, 201, 201, 200.9, 200.8, 200.7, 200.5, 200.3, 200.1, 199.8, 199.5, 199.1, 198.7, 198.3, 197.8, 197.3, 196.8, 196.2, 195.6, 194.9, 194.2, 193.5, 192.7, 191.9, 191.1, 190.2,189.3, 188.4, 187.4, 186.3, 185.3, 184.2, 180.8,176.2, 170.2]

print(len(critical_rpms))
print(len(torques))


##Calculating power
print("Using the following equation to find the Power at a specific rpm:") 
print("\n   Power = 2*pi*rpm[1/min] / 60[s] * Torque")


for i in range(len(critical_rpms)):
     powers.append((2*pi * critical_rpms[i] / 60 * torques[i])/1000)
     print("\n--> @%d,  Power = %.1fkW & Torque = %.1fNm" %(critical_rpms[i], powers[i], torques[i]))



#Graph this with matplot lib


fig, ax1 = plt.subplots()
fig.suptitle('Torque, Power, RPM diagram')
ax1.set_xlabel('n(rpm)')
ax1.set_xlim([0,max(critical_rpms)+500])
ax1.set_ylim([0,max(torques) + 15])
ax1.set_ylabel('Torque(Nm)', color='r')
ax1.tick_params(axis='y', labelcolor='r')

ax2 = ax1.twinx() #instantiate 2nd axis
ax2.set_ylabel('Power(kW)', color='b')
ax2.set_ylim([0,max(powers)+15])
ax2.tick_params(axis='y', labelcolor='b')

if len(torques) < 10:  #if there are many data points no need for scatter.
     ax1.scatter(critical_rpms, torques, color='r')
     ax2.scatter(critical_rpms, powers, color='b')

##cubic spline interpolation for smooth graph (only works for more than 3 data points...)
if len(torques) > 3:
     
     import numpy as np
     import scipy
     from scipy.interpolate import make_interp_spline, BSpline

     torques = np.array(torques)
     critical_rpms = np.array(critical_rpms)
     powers = np.array(powers)

     critical_rpms_new = np.linspace(critical_rpms.min(), critical_rpms.max(), 300)
     sp1 = make_interp_spline(critical_rpms, powers, k=2)
     sp2 = make_interp_spline(critical_rpms, torques, k=2)

     powers = sp1(critical_rpms_new)#smoothed
     torques = sp2(critical_rpms_new) #smoothed
     critical_rpms = critical_rpms_new 

ax2.plot(critical_rpms, powers, color='b', label='Power')
ax1.plot(critical_rpms, torques, color='r', label='Torque')



#plt.legend()
plt.show()








