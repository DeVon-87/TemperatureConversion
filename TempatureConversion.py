def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 +32 
    return fahrenheit

# the main function is used to test the other functions

def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp), 2), "Celsius")

    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp), 2), "Fahrenheit")

if __name__ == "__main__":
    main()
