# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, 
# 	take its mass, 
# 	divide by three, 
# 	round down,
# 	subtract 2.
#
# For example:
#
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. 
# To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

import math

def calulate_launch_fuel_for_mass(mass):
	fuel = math.floor(int(mass) / 3) - 2
	new_fuel = calulate_fuel_needed_to_launch_fuel(fuel)

	return fuel + new_fuel

def calulate_fuel_needed_to_launch_fuel(fuel):
	additional_fuel = 0
	 
	while fuel > 0:
		fuel = math.floor(int(fuel) / 3) - 2
		if fuel > 0:
			additional_fuel += fuel

	return additional_fuel


total_fuel = 0

with open('massList.txt') as document:
   line = document.readline()
   while line:
	   fuel = calulate_launch_fuel_for_mass(line.strip())
	   total_fuel += fuel
		# print("Mass of {} needs {} fuel.".format(line.strip(), fuel))
	   line = document.readline()


print('Total fuel: ', total_fuel)