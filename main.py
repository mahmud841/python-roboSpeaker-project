import os
# print(dir(os))

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.3. Created by Mahmud")
    while True:
        x = input("Enter a what you want me to speak: ")
        if x == "j":
            os.system("say 'bye bye friend'")
            break
            command = f"say {x}"
            os.system(command)




