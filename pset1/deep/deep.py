valid_answers = ["42", "fourty-two", "fourty two"]
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if answer.lower() in valid_answers:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()