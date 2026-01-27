import random

def noisy_reading(base):
    noise = random.uniform(-0.5, 0.5)
    if random.random() < 0.1:  # 10% chance of glitch
        return 0
    return base + noise

def generate_ramdom_log():
    print("=========== 10 Checkpoints Data with Noise and Glitches ============")
    sensors = ["Front", "Left", "Right"]
    sensor_data = {}
    
    for sensor in sensors:
        readings = {}
        for i in range(10):
            readings[i] = noisy_reading(random.uniform(5, 25))
        sensor_data[sensor] = readings
        
    return sensor_data


def robot_log():
    print("=========== 10 Checkpoints Data with Noise and Glitches ============")
    
    robot_db = {}
    sensors = ["Front", "Left", "Right"]
    
    for i in range(3):
        print(f"\nEnter 10 readings for the {sensors[i]} sensor (cm):")
                
        robot_inner_db = {}
        
        for j in range(10):
            
            while True:
                try:
                    reading = float(input(f"   Reading {j+1}: "))
                    
                    robot_inner_db[j] = noisy_reading(reading)
                    break
                except ValueError:
                    print("Invalid Input - please enter a numeric number")
            
        robot_db[sensors[i]] = robot_inner_db
        
    return robot_db

def print_report(logs):
    
    print("\n------ SEnsor Noisy Reading Report ------\n")
    flag = ["MOVE FORWARD", "SLOW DOWN", "STOP", "SENSOR GLITCH - RETRY"]
    
    for i in range(10):
        
        print(f"\nCheckpoint {i+1}: ")
        for sensor, readings in logs.items():
            temp = 0
            if readings[i] < 15 and readings[i] >= 10:
                temp = 1
            elif readings[i] < 10 and readings[i] != 0:
                temp = 2
            elif readings[i] == 0:
                temp = 3
            
            print(f"   {sensor} sensor: {readings[i]:.2f} cm -> {flag[temp]}")
            
            
    

if __name__ == "__main__":
    
    # database = robot_log()
    # OR
    database = generate_ramdom_log()
    # print(database)
    
    print_report(database)
            
            
        
            