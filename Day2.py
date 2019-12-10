# list of int[1, 0, 0, 3, 99]
# 1, 2, 99 are key numbers# 99: stop
# # 1: add number from array positions from next 2 values and store sum in array position of 3 rd value
# # i.e.[0, 1, 3, 2, 0]
# # hit 1
# # add array[3](2) and array[2](3) and store in array[2](3)
# #[0, 1, 5, 2, 0]
# #
# #
# # 2: multiply 2 inputs store sum in 3 rd
# # after hitting a 1 or 2 do the operation and then skip the next 3 numbers
from copy import deepcopy

def run_Intcode(intcode): 
	index = 0
	intcode_Length = len(intcode)
 
	while(index < intcode_Length-3):
		num = intcode[index]
  
		if num == 1 or num == 2:
			int1 = intcode[(index+1)]
			int2 = intcode[(index+2)]
			result = intcode[(index+3)]
   
			if num == 1:
				intcode[result] = intcode[int1] + intcode[int2]
			elif num == 2:
				intcode[result] = intcode[int1] * intcode[int2]
    
			index += 4
		elif num == 99:
			return intcode
		else:
			index += 1

	return intcode


# print(run_Intcode('1,9,10,3,2,3,11,0,99,30,40,50'))
# print(run_Intcode('2,3,0,3,99'))
# print(run_Intcode('2,4,4,5,99,0'))
# print(run_Intcode('1,1,1,4,99,5,6,0,99'))

# assert run_Intcode([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
# assert run_Intcode([2,3,0,3,99]) == [2,3,0,6,99]
# assert run_Intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
# assert run_Intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]                

with open('Day2Input.txt') as document: 
	line = document.readline()
	while line: 
		og_intcode =  [int(x) for x in line.strip().split(',') if x]
		answer = None
		for noun in range(100):
			if answer != None:
				break
			for verb in range(100):
				intcode = deepcopy(og_intcode)
    
				intcode[1] = noun
				intcode[2] = verb
				output = run_Intcode(intcode)[0]
    
				if output == 19690720:
					answer = (100 * noun) + verb
					break

		print("Answer: ", answer)

		line = document.readline()