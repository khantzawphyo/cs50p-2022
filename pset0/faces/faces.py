def convert(msg):
    return msg.replace(":)", "🙂").replace(":(", "🙁")

def main():
    msg = input()
    print(convert(msg))

if __name__ == "__main__":
    main()
