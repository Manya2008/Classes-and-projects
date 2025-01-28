import random

roll = "y"

while roll.lower() == "y":
    no = random.randint(1,6)
    if no == 1 :
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif no == 2 :
        print("[0    ]")
        print("[     ]")
        print("[    0]")
    elif no == 3 :
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
    elif no == 4 :
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    elif no == 5 :
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    elif no == 6 :
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
    roll = input("Wanna roll a dice y/n? ")