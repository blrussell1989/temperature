def to_fahrenheit (temperature):
	fahrenheit = (temperature * (9 / 5)) + 32 
	return fahrenheit 
    
def to_celsius (temperature):
	celsius = (temperature - 32) * (5 / 9)
	return celsius
    
def to_kelvin (temperature):
	#print("tc")
	#print(to_celsius(212))
	kelvin = temperature + 273.15
	return kelvin
    
f = to_fahrenheit(100)
c = to_celsius(32)
k = to_kelvin(-273.15)
m = to_fahrenheit(to_celsius(98.6))

print("fahrenheit: " + str(f))
print("celsius: " + str(c))
print("kelvin: " + str(k)) 
print("multiconvert: " + str(m)) 

 
