import sys
import subprocess
import os
import time
import shutil

def main():
    builtins = ["echo", "type", "exit", "cd", "pwd", "date", "ls", "mkdir"]
    PATH = os.environ.get("PATH")
    paths = PATH.split(":") if PATH else []

    sys.stdout.write(f"$ ")
    sys.stdout.flush()

    while True:
        user_input = input().strip()
        if user_input == "exit 0":
            break
        elif user_input.startswith("grep"):
            arguments = user_input[5:].split(" ")
            file = open(arguments[1], "r")
            content = file.read()
            print(content)
            file.close()
            i = 0
            if arguments[0][0] == "[":
                    for char in arguments[0][1:-1]:
                        for character in content:
                            if char == character:
                                i = i + 1
                               
                                
                        
            else:   
                for char in content:
                    if char == arguments[0]:
                        i = i + 1
                       
                       
            print(i)
                        
        elif user_input.startswith("rd"):
            dirs = user_input[3:].split(" ")
            if dirs[0] == "-r":
                if len(dirs) == 2:
                    try:
                        shutil.rmtree(dirs[1])
                    except FileNotFoundError:
                        print(f"Directory {dirs[1]} not found")
                else:
                    for item in dirs[1:]:
                        try:
                            shutil.rmtree(item)
                        except FileNotFoundError:
                            print(f"Directory {item} not found")
            if len(dirs) == 1:
                try:
                    os.rmdir(dirs[0])
                except FileNotFoundError:
                    print(f"Directory {dirs[0]} not found")
            else:
                for item in dirs:
                    try:
                        os.rmdir(item)
                    except FileNotFoundError:
                        print(f"Directory {item} not found")
        elif user_input.startswith("date"):
            now = time.time()
            date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(now))
            print(date)
        elif user_input.startswith("cd"):
            try:
                if user_input[3:]=="~":
                    os.chdir(os.environ.get("HOME"))
                else:
                    os.chdir(os.path.abspath(user_input[3:]))
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
                        found = True
                        break
                if not found:
                    print(f"{command_name}: not found")
        elif user_input.startswith("mkdir"):
            dirs = user_input[6:].split(" ")
            if len(dirs) == 1:
                os.mkdir(dirs[0])
            else:
                for item in dirs:
                    os.mkdir(item)
        elif user_input.startswith("ls"):
            print(os.listdir(os.getcwd()))
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
