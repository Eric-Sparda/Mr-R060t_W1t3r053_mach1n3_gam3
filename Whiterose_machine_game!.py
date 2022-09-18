start = "y"

def he_decided_to_leave():
    question = input("You're trapped in a dungeon with your friend. You see a barrel. What do you do ? ")
    while question.lower().strip() not in ("move the barrel", "sit down next to my friend"):
        question = input("You're trapped in a dungeon with your friend. You see a barrel. What do you do ? ")
    if question.lower().strip() == "move the barrel":
        question = input("The barrel rolls aside revealing a secret tunnel. What do you do ? ")
        while question.lower().strip() != "enter tunnel":
            question = input("The barrel rolls aside revealing a secret tunnel. What do you do ? ")
        if question.lower().strip() == "enter tunnel":
            question = input("You start to escape but your friend is too weak to go with you. He hands you a note. What do you do ? ")
            while question.lower().strip() != "read the note":
                question = input("You start to escape but your friend is too weak to go with you. He hands you a note. What do you do ? ")
            if question.lower().strip() == "read the note":
                question = input("It's too dark to read the note. What do you do ? ")
                while question.lower().strip() != "leave":
                    question = input("It's too dark to read the note. What do you do ? ")
                if question.lower().strip() == "leave":
                    question = input("You crawl through the tunnel and the tunnel leads you to a beach. What do you do ? ")
                    while question.lower().strip() != "look":
                        question = input("You crawl through the tunnel and the tunnel leads you to a beach. What do you do ? ")
                    if question.lower().strip() == "look":
                        question = input("In the water you see a boat. What do you do ? ")
                        while question.lower().strip() != "get on the boat":
                            question = input("In the water you see a boat. What do you do ? ")
                        if question.lower().strip() == "get on the boat":
                            print("Congratulations, you're heading to a new world!")
    elif question.lower().strip() == "sit down next to my friend":
        question = input("Your friend hands you a note. What do you do ? ")
        while question.lower().strip() != "read the note":
            question = input("Your friend hands you a note. What do you do ? ")
        if question.lower().strip() == "read the note":
            question = input("The note says, <<Don't leave me here.>> Do you leave your friend or stay ? ")
            if question.lower().strip() == "stay":
                print("Hello, Friend")
            elif question.lower().strip() == "leave":
                he_decided_to_leave()


while start == "y":
    input("Press Enter to start")
    question = input("You're trapped in a dungeon with your friend. You see a barrel. What do you do ? ")
    while question.lower().strip() not in ("move the barrel", "sit down next to my friend"):
        question = input("You're trapped in a dungeon with your friend. You see a barrel. What do you do ? ")
    if question.lower().strip() == "move the barrel":
        question = input("The barrel rolls aside revealing a secret tunnel. What do you do ? ")
        while question.lower().strip() != "enter tunnel":
            question = input("The barrel rolls aside revealing a secret tunnel. What do you do ? ")
        if question.lower().strip() == "enter tunnel":
            question = input("You start to escape but your friend is too weak to go with you. He hands you a note. What do you do ? ")
            while question.lower().strip() != "read the note":
                question = input("You start to escape but your friend is too weak to go with you. He hands you a note. What do you do ? ")
            if question.lower().strip() == "read the note":
                question = input("It's too dark to read the note. What do you do ? ")
                while question.lower().strip() != "leave":
                    question = input("It's too dark to read the note. What do you do ? ")
                if question.lower().strip() == "leave":
                    question = input("You crawl through the tunnel and the tunnel leads you to a beach. What do you do ? ")
                    while question.lower().strip() != "look":
                        question = input("You crawl through the tunnel and the tunnel leads you to a beach. What do you do ? ")
                    if question.lower().strip() == "look":
                        question = input("In the water you see a boat. What do you do ? ")
                        while question.lower().strip() != "get on the boat":
                            question = input("In the water you see a boat. What do you do ? ")
                        if question.lower().strip() == "get on the boat":
                            print("Congratulations, you're heading to a new world!")
    elif question.lower().strip() == "sit down next to my friend":
        question = input("Your friend hands you a note. What do you do ? ")
        while question.lower().strip() != "read the note":
            question = input("Your friend hands you a note. What do you do ? ")
        if question.lower().strip() == "read the note":
            question = input("The note says, <<Don't leave me here.>> Do you leave your friend or stay ? ")
            if question.lower().strip() == "stay":
                print("Hello, Friend")
            elif question.lower().strip() == "leave":
                he_decided_to_leave()

    start = input("Do you want to play again ? y/n ")
