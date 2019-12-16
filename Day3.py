wire1 = None
wire2 = None


def get_wire_path(wire):
	wire_path = [(0,0)]

	for line in wire:
		direction = line[0]
		distance = int(line[1:])
  
		#print('Direction: {}  Distance: {}'.format(direction, distance))
		
		for step in range(1, distance+1):
			p_x = wire_path[len(wire_path)-1][0]
			p_y = wire_path[len(wire_path)-1][1]
   
			if direction == 'U':    
				wire_path.append((p_x, p_y+1))
			elif direction == 'D':
				wire_path.append((p_x, p_y-1))
			elif direction == 'L':
				wire_path.append((p_x-1, p_y))
			elif direction == 'R':
				wire_path.append((p_x+1, p_y))
	
	return wire_path

def getDistanceOfPath(path):
	distance = 0
	previous_cord = None
	
	for cord in path:
		x = cord[0]
		y = cord[1]
		
		if previous_cord == None:
			previous_cord = cord
		else:
			if x != previous_cord[0]:
				distance += abs(x - (previous_cord[0]))
			if y != previous_cord[1]:
				distance += abs(y - (previous_cord[1]))
				
			previous_cord = cord
	
	return distance

def get_wire_crosses(wirePath1, wirePath2):
    crosses = list(set(wirePath1) & set(wirePath2))
    crosses.remove( (0,0) )
    return crosses

def get_min_cross_distance(wire1_path, wire2_path):
	crosses = get_wire_crosses(wire1_path, wire2_path)
	print(crosses)
 
	distances = []
	for cross in crosses:
		distance = getDistanceOfPath(((0,0), cross))
  
		if distance > 0:
			distances.append(distance)
	
	return min(distances)

def get_steps_to_point(wire_path, point):
    steps = 0
    
    for pos in wire_path:
        if pos == point:
            return steps
        else:
            steps += 1
    
    return None
 
def get_min_cross_steps(wire1_path, wire2_path):
    crosses = get_wire_crosses(wire1_path, wire2_path)
    min_cross_steps = None
    #print('----------------------------------')
    #print('Crosses: ',crosses)
    
    for cross in crosses:
        w1Cross = get_steps_to_point(wire1_path, cross)
        w2Cross = get_steps_to_point(wire2_path, cross)
        if min_cross_steps == None:
            min_cross_steps = w1Cross+w2Cross
        elif min_cross_steps > w1Cross+w2Cross:
            min_cross_steps = w1Cross+w2Cross
        
    #     print('----------------------------------')
    #     print('Wire 1 steps', w1Cross)
    #     print('Wire 2 steps', w2Cross)
    #     print('Combined steps', w1Cross+w2Cross)  
    # print('----------------------------------')      
    
    return min_cross_steps
     

with open('Day3Input.txt') as document: 
	lineCount = 1

	line = document.readline()
	while line:
		wire = line.strip().split(',')
  
		if lineCount == 1:
			wire1 = wire
		elif lineCount == 2:
			wire2 = wire
		lineCount+=1

		line = document.readline()
  
#print("Line 1: ", wire1)
#print("Line 2: ", wire2)
wire1_path = get_wire_path(wire1)
wire2_path = get_wire_path(wire2)
#print('wire 1 path: ', wire1_path)
#print('wire 2 path: ', wire2_path)
#print(get_min_cross_distance(wire1_path, wire2_path)) #part1

print(get_min_cross_steps(wire1_path, wire2_path)) #part2