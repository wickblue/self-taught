'''
Training program for Rock Climbing
'''
import os
import datetime

def workout():
    boulder = ["v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8"]
    routes = ["5.7", "5.8", "5.9", "5.10a", "5.10b", "5.10c", "5.10d",
              "5.11a", "5.11b", "5.11c", "5.11d", "5.12a", "5.12b", "5.12c",
              "5.12d", "5.13a"]
    completed = []
    print("Welcome to program, press (q) anytime to quit")
    while True:
        log = input("\nRecord a route: ")
        print(type(log))
        if log in boulder or log in routes:
            print("in boulder")
            completed.append(log)
        elif log == 'q':
            break
        else:
            print("Invalid input.")
    return completed

today = workout()

os.path.join("K4446","Users","philllippierce","Documents")

with open("climbing.txt", "a+") as f:
    if str(datetime.date.today) not in f:
        f.write("\n"+str(datetime.date.today()))
    for item in today:
        f.write("\n{0}".format(item))

