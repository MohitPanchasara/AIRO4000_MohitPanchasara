def decide_action():

    total = int(input("Enter total number of distances you want to add: "))
    distance = input(f"Enter {total} Distances (space seperated):> \n").split()

    # HANDLING TOTAL INPUT NUMBER 
    while True:
        if len(distance) != total:
            distance = input(f"Please Enter Only Exact {total} Values \n").split()
        else:
            break
        
        
    # HANDLING Ccount summary

    execution = [0]*4

    for i in range(total):
        if distance[i].lstrip('-').isdigit():
            distance[i] = int(distance[i])
            
            if distance[i] < 20:
                print(f"Reading {i+1}: {distance[i]} cm -> STOP\n")
                execution[0] += 1
            elif distance[i] <50 and distance[i] >= 20:
                print(f"Reading {i+1}: {distance[i]} cm -> SLOWING DOWN\n")
                execution[1] += 1
            elif distance[i] >= 50:
                print(f"Reading {i+1}: {distance[i]} cm -> MOVE FORWARD\n")
                execution[2] += 1
        
        else:
            print(f"Reading {i+1}: Invalid -> skipped \n")
            execution[3] += 1
            
            
    print("")

    return f"### SUMMARY ### \nSTOP: {execution[0]}, SLOW DOWN: {execution[1]}, MOVE FORWARD: {execution[2]}, INVALID ITERATIONS: {execution[3]} "   

if __name__ == "__main__":
    action = decide_action()
    print(action)