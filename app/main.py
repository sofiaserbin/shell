import sys


def main():
    builtins = ["echo", "type", "exit"]
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    while True:
        user_input=input()
        if user_input=="exit 0":
            break
        if "echo" in user_input:
            print(user_input[5:])
        if user_input[0:3]=="type":
            if user_input[5:] in builtins:
                print(f"{user_input[5:]} is a shell builtin")
            else:
                print(f"{user_input[5:]} not found")
        else:
            print(f"{user_input}: command not found")
        sys.stdout.write("$ ")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
