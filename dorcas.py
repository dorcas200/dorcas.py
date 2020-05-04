#finding the area of a square.
def calcarea(side):
    area = side*side
    return area
side= int(input("Enter length: "))
area = calcarea(side)
print(area).

#finding the area of rectangle
def calcArea(length,breadth):
	rectangle= length*breadth
	return rectangle
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
rectangle= calcArea(length,breadth)
print(rectangle)

#finding the area of a triangle
def calcArea(breadth,height):
	triangle = 1/2*breadth*height
	return triangle
breadth = int(input("Enter the breadth: "))
height = int(input("Enter the height: "))
triangle = calcArea(breadth,height)
print(triangle)

#finding the area of a circle
def calcArea(pi,radius):
	circle = pi*radius*radius
	return circle
pi = 3.142
radius = int(input("Enter radius: "))
circle = calcArea(pi,radius)
print(circle)

#finding the circumference of a circle
def calcCircumference(pi,radius):
	circum = 2*pi*radius
	return circum
pi = 3.142
radius = int(input("Enter radius: "))
circum = calcCircumference(pi,radius)
print(circum)

#finding the surface area of a cube
def calcSAC(length):
	surf_area = 6*length*length
	return surf_area
length = int(input("Enter length: "))
surf_area  = calcSAC(length)
print(surf_area)

#finding the curved surface areaof a cylinder
def calcCSC(pi,radius,height):
	curve_area = 2*pi*radius*height
	return curve_area
pi = 3.142
radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))
curve_area = calcCSC(pi,radius,height)
print(curve_area)

#finding the total surface area of a cylinder
def calcTSC(pi,radius,height):
	total_area = 2*pi*radius*(radius+height)
	return total_area
pi = 3.142
radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))
total_area = calcTSC(pi,radius,height)
print(total_area)

#finding the volume of a cylinder
def calcVolume(pi,radius,height):
	volume = pi*radius*radius*height
	return volume
pi = 3.142
radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))
volume = calcVolume(pi,radius,height)
print(volume)

#finding acceleration
def calcAcceleration(initial,final,time):
	accel = (initial-final)/time
	return accel
initial = float(input("Enter the initial velocity: "))
final = float(input("Enter the final velocity: "))
time = float(input("Time taken: "))
accel = calcAcceleration(initial,final,time)
print(accel)

#finding density
def calcDensity(mass,volume):
	dens = mass/volume
	return dens
mass = float(input("Enter the mass given: "))
volume = float(input("Enter the volume given: "))
dens = calcDensity(mass,volume)
print(dens)

#finding pressure
def calcPressure(force,area):
	pressure = force/area
	return pressure
force = int(input("Enter the force given: "))
area = int(input("Enter the area given: "))
pressure = calcPressure(force,area)
print(pressure)

#finding Kinetic Energy 
def calcKineticEnergy(mass,volume):
	K_E = 1/2*mass*volume
	return K_E
mass = int(input("Enter the mass: "))
volume = int(input("Enter the volume: ")
K_E = calcKineticEnergy(mass,volume)
print(k_E)

#finding voltage
def calcVoltage(current,resistance):
	vol = current*resistance
	return vol
current = int(input("Enter the current given: "))
resistance = int(input("Enter the resistance given: "))
vol = calcVoltage(current,resistance)
print(vol)




	