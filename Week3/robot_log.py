def robot_log():
    
    robot_db = {}
    sensors = ["Front", "Left", "Right"]
    
    for i in range(3):
        print(f"\nEnter three readings for the {sensors[i]} sensor (cm):")
                
        robot_inner_db = {}
        
        for j in range(3):
            
            while True:
                try:
                    reading = float(input(f"   Reading {j+1}: "))
                    robot_inner_db[j] = reading
                    break
                except ValueError:
                    print("Invalid Input - please enter a numeric number")
            
        robot_db[sensors[i]] = robot_inner_db
        
    return robot_db

def print_report(logs):
    
    print("\n--- SEnsor Change Report ---")
    
    for sensor, readings in logs.items():
        change = readings[2] - readings[0]
        
        if change > 0:
            flag = ['+', 'increase']
        elif change == 0:
            flag = ['', 'constant']
        else:
            flag = ['-', 'decreases'] 
            
        
        print(f"{sensor}: {readings[0]} -> {readings[2]}  (change {flag[0]}{change} cm, {flag[1]})")
    
    print("\nAll Readings: ")
    
    for S, R in logs.items():
        
        all_readings = [0]*3
        for i,j in R.items():
            all_readings[i] = j
        
        print(f"{S}: {all_readings}")
            
            
    

if __name__ == "__main__":
    database = robot_log()
    # print(database)
    
    print_report(database)
            
            
        
            