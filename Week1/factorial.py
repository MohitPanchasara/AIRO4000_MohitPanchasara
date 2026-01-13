def factorial(num):
    
    temp = 1
    
    for i in range(1, num+1):
        temp = temp * i
        
    return temp
    
if __name__ == "__main__":    

    Entry = int(input("Enter an integer for its factorial: "))
    result = factorial(Entry)
    print(result)