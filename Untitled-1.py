def raindrops(number):
    result = ""

    if number % 3 == 0:
        result += "Pling"

    if number % 5 == 0:
        result += "Plang"

    if number % 7 == 0:
        result += "Plong"

    if not result:
        result = str(number)

    return result

# Example usage
number = int(input("Enter a number: "))
print(raindrops(number))
