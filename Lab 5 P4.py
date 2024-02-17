for x in range(1, 51):
    
    print(x)

    if x % 3 == 0 and x % 5 == 0: #First checks if divisible by both
        print("Divisible by both")

    elif x % 5 == 0: #Checks if divisible by 5 
        print("Divisible by 5")

    elif x % 3 == 0: #Checks if divisible by 3
        print("Divisible by 3")
    

#Victor Moreno
#2/16/24
#Program iterates integers 1-50. If integer is divisible by 3, it will state. If integer is divisible by 5, it will state. If integer is divisible by both, it will state.
