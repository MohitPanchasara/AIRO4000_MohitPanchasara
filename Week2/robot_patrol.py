# PATROL SIMULATION OF A ROBOT

def how_many_patrols():
    while True:
        try:
            patrols = int(input("How many checkpoints? "))
            if patrols < 1 or patrols > 10:
                print("Error! Please enter a number between 1-10")
            else:
                break
        except ValueError:
            print("Error! Please enter a whole number")            
    return patrols

def input_each_patrol(patrols):
    array = []
    for i in range(patrols):
        while True:
            try:
                array.append(float(input(f"Enter a sensor reading (cm) for checkpoint {i+1}: ")))
                break
            except ValueError:
                print("Invalid Input - please enter a numeric number")
    return array


def decide_robot_actions(length, checkpoints):
    
    execution = [0]*3
    
    for i in range(length):
    
        if checkpoints[i] < 10:
            print(f"Reading {i+1}: {checkpoints[i]} cm -> STOP\n")
            execution[0] += 1
        elif checkpoints[i] <14 and checkpoints[i] >= 10:
            print(f"Reading {i+1}: {checkpoints[i]} cm -> SLOWING DOWN\n")
            execution[1] += 1
        elif checkpoints[i] >= 15:
            print(f"Reading {i+1}: {checkpoints[i]} cm -> MOVE FORWARD\n")
            execution[2] += 1
            
    return execution
    


if __name__ == "__main__":
    
    no_of_patrols = how_many_patrols()
    checkpoints = input_each_patrol(no_of_patrols)
    
    execution = decide_robot_actions(no_of_patrols, checkpoints)
    
    summary = f"### SUMMARY ### \nSTOP: {execution[0]}, SLOW DOWN: {execution[1]}, MOVE FORWARD: {execution[2]} "
    
    
    