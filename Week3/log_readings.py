import csv 


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
        
def save_to_csv(logs, filename="log.csv"):
    
    with open(filename, "w", newline="") as file:
        writer =csv.writer(file)
        
        sensors = list(logs.keys())
        writer.writerow(sensors)
        
        for rows in range(3):
            row = []
            for sensor in sensors:
                row.append(logs[sensor][rows])
            writer.writerow(row)
            
    print(f" Data Saved to {filename}")
    
    
def read_from_csv(filename="log.csv"):
    
    data = []
    
    with open(filename, "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            data.append(row)
        
    return data
    
    
def reconstruct_dict(filename="log.csv"):
    
    final_dict = {}
    
    with open(filename, "r") as file:
        reader = csv.reader(file)
    
        sensors = next(reader)
        
        for sensor in sensors:
            final_dict[sensor] = {}
            
        temp = 0
        
        for row in reader:
            for i, s in enumerate(sensors):
                final_dict[s][temp] = float(row[i])
                
            temp += 1
            
    return final_dict
    

def print_logs(logs):
    print("\n---Loaded Readings ---")
    
    for sensor, readings in logs.items():
        
        min_val = readings[0]
        max_val = readings[0]
        values = []
        
        for i in range(3):
        
            values.append(readings[i])
            
            if readings[i] > max_val:
                max_val = readings[i]
            elif readings[i] < min_val:
                min_val = readings[i]
        
        average = sum(values)/len(values)
        
        print(f"{sensor} - Avg: {average:.2f} cm, Min: {min_val:.2f} cm, Max: {max_val:.2f} cm")
     

if __name__ == "__main__":
    database = robot_log()
    # print(database)
    
    save_to_csv(database)
    
    final_dict = reconstruct_dict()
    print_logs(final_dict)
            
            
    