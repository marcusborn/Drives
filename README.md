# Drives
A repository to help me learn about drives and also help others studying drive systems :)

This is a method to analyse the relationship between torque, power and rpm and ultimately figure out the most efficient rpm to do gear changes in a car with just some basic data. 

1.0 I have written a program that does some basic calculations and creates a graph of rpm-torque and rpm-power for a specific engine. 

In the example I am analysing some basic data from the 2019 Mazda MX-5 RF manual transmission with 6 gears. (https://www.mazda.com.au/cars/mx-5/specifications/)

With data taken from a car catalogue we know the maximum torque of the internal combustion engine is 205 Nm at 4000 rpm. (available at https://www.automobile-catalog.com/curve/2019/2771225/mazda_mx-5_miata_rf_club_6-speed.html)

If For a 'quick and dirty' calculation that can be easily done by hand we can get a good estimation of engine charactarstics with just 3 data points. we can take 85% of the max torque = 174.5 and find the closest data points that match this. 
leaving us with 174.8Nm @2300rpm and 176.2Nm @7200rpm

From here we can graph the curve of power and Torque. 

Solution for important values:

![Alt Text](https://github.com/marcusborn/Drives/blob/master/1.0%20solutions%20mx5%203-points.png)

Graphs of power and torque:

![Alt Text](https://github.com/marcusborn/Drives/blob/master/1.0%20graph%20mx5%203-points.png)


This graph shows us the torque charactaristics for this engine. It should be clear that the most efficient operational speed of this engine is at 4000rpm. This will later help us determine the optimal time to change gears.

Using more data points supplied by the manufacturer and obtained from the previous catalogue. We can use the same program which uses cubic spline interpolation to get better torque and power curves of the MX-5 engine seen below.

Graph:

![Alt Text](https://github.com/marcusborn/Drives/blob/master/1.0%20Torque%2C%20Power%2C%20rpm%20Graph%20mx-5%20engine%20.png)


