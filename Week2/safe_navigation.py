def checkpoints():
    
    while True:
        try:
            checkpoint = int(input("How many checkpoints? "))
            if checkpoint <= 0:
                print("Error! Please enter a number that is at least 1")
            else:
                break
        except ValueError:
            print("Error! Please enter a whole number")
            
    array = []
    
    for i in range(checkpoint):
        
        while True:
            try:
                array.append(float(input(f"Enter distance for checkpoint {i+1} in cm: ")))
                break
            except ValueError:
                print("Invalid Input - please enter a numeric number")
            
    return array


if __name__ == "__main__":
    print(f"Distances Recorded: {checkpoints()}")