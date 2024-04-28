def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the leading $
    amount = d[1:]
    # Convert to float
    return float(amount)


def percent_to_float(p):
    # Remove the trailing %
    percentage = p[:-1]
    # Convert to float and divide by 100 to get the decimal representation
    return float(percentage) / 100


if __name__ == "__main__":
    main()
