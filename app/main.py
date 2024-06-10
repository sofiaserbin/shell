import sys
import os


def main():
    builtins = ["echo", "type", "exit"]
    PATH = os.environ.get("PATH")
    paths = PATH.split(":")
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
        elif user_input.startswith("echo"):
            print(user_input[5:])
        elif user_input.startswith("type"):
            found = false
            for path in paths:
                if os.path.isfile(f"{path}/{user_input[5:]}"):
                    print(f"{user_input[5:]} is {path}/{user_input[5:]}")
                    found = true
                    sys.stdout.write("$ ")
                    sys.stdout.flush()
                    break
            if found = true:
                continue
            elif user_input[5:] in builtins:
                print(f"{user_input[5:]} is a shell builtin")
            else:
                print(f"{user_input[5:]} not found")
        else:
            print(f"{user_input}: command not found")
        sys.stdout.write("$ ")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
