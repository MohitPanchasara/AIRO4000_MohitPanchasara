def input_num_robots():    

    check = int(input("How many robots you want to check? Enter a value (min 1, max 5): "))

    while True:
        if check < 1 or check > 5:
            print("Please enter amount between 1 and 5")
            check = int(input())
        else:
            break
        
    return check

def input_robots_speed(num):    
    speed = []
    for i in range(1, num+1):
        print(f"Please enter the speed for Robot {i}")
        temp = float(input())
        speed.append(temp)
    return speed
    
def check_speed(speed):
    speed_check = []
    
    for i in range(len(speed)):
        if speed[i] < 10:
            speed_check.append("Too Slow")
            
        if speed[i] > 50:
            speed_check.append("Too Fast")
            
        else:
            speed_check.append("Speed OK!")
            
    return speed_check


if __name__ == "__main__":
    total_robots = input_num_robots()
    speed = input_robots_speed(total_robots)
    speed_check = check_speed(speed)
    
    for i in range(total_robots):
        print(f"Robot {i}: {speed_check[i]} (Speed: {speed[i]})")
    
    
    
    
    