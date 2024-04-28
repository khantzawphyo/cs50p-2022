def calculate(mass):
    # Speed of light in meters per second
    speed_of_light = 300000000
    
    # Calculate energy using the famous equation E=mc^2
    energy = mass * speed_of_light**2
    
    return energy

def main():
    m = int(input("m: "))
    print("E: ", calculate(m))

if __name__ == "__main__":
    main()