import os
import csv

os.path.join("K4446","Users","philllippierce","Documents")

with open("challengeLists.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])
               

