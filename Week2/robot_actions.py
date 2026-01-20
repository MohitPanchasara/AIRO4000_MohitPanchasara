def robot_actions(name, turns, direction):
    print(f"Initializing the Robot :> {name}")
    
    for i in range(turns):
        print(f"Turning the {name} to {direction}")
        if direction == 'left':
            print(f" ^ \n < \n v \n > \n ^")
            print(f"Turn {i} Complete: {name} turned fully anti-clockwise\n")
        else:
            print(f" ^ \n > \n v \n < \n ^")
            print(f"Turn {i+1} Complete: {name} turned fully clockwise\n")
            
if __name__ == "__main__":
    name = input("Give a name to Robot: ")
    direction = input("Enter direction of the turn (left or right): ")
    turns = int(input("Enter number of turns: "))
    robot_actions(name, turns, direction)