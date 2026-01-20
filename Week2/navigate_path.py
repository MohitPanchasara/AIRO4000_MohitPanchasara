def handle_total_inputs(distances):
    while True:
        if len(distances) != 5:
            distances = input(f"Please Enter Only Exact 5 Values \n").split()
        else:
            break
    return distances
    
    
def decide_action(distance):
    
    if distance.lstrip('-').isdigit():
        distance = int(distance)
        
        if distance < 20:
            return f" {distance} cm -> STOP\n"
        elif distance <50 and distance >= 20:
            return f" {distance} cm -> SLOWING DOWN\n"
        elif distance >= 50:
            return f" {distance} cm -> MOVE FORWARD\n"
        
    else:
        return f"Reading Invalid -> skipped \n"
            
    
    
    
def user_input_func():
    # take 5 inputs
    distance = input(f"Enter 5 Distances (space seperated):> \n").split()
    
    five_distances = handle_total_inputs(distance)

    return five_distances
    
    

if __name__ == "__main__":
    user_input = user_input_func()
    
    for i in range(len(user_input)):
        print(f"Action: {i+1} | {decide_action(user_input[i])}")