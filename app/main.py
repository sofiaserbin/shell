import sys
import subprocess
import os

def main():
    builtins = ["echo", "type", "exit"]
    PATH = os.environ.get("PATH")
    paths = PATH.split(":") if PATH else []

    sys.stdout.write("$ ")
    sys.stdout.flush()

    while True:
        user_input = input().strip()
        if user_input == "exit 0":
            break
        elif user_input.startswith("cd"):
            try:
                os.chdir(user_input[3:])
            except FileNotFoundError:
                print(f"cd: {user_input[3:]}: No such file or directory")
                
        elif user_input.startswith("pwd"):
                print(os.getcwd())
        elif user_input.startswith("echo "):
            print(user_input[5:])
        elif user_input.startswith("type "):
            command_name = user_input[5:].strip()
            if command_name in builtins:
                print(f"{command_name} is a shell builtin")
            else:
                found = False
                for path in paths:
                    executable_path = os.path.join(path, command_name)
                    if os.path.isfile(executable_path):
                        print(f"{command_name} is {executable_path}")
                        # os.command(command_name)
                        found = True
                        break
                if not found:
                    print(f"{command_name}: not found")
        else:
            cmd_parts = user_input.split()
            cmd = cmd_parts[0]
            args = cmd_parts[1:]
            found = False
            for path in paths:
                executable_path = os.path.join(path, cmd)
                if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                    subprocess.run([executable_path] + args)
                    found = True
                    break
            if not found:
                print(f"{user_input}: command not found")
        
        sys.stdout.write("$ ")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
