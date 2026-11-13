import random

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

while True:
    print(CYAN + "\n=== TALHA KA ULTIMATE TOOL ===" + RESET)
    print(GREEN + "1. Calculator" + RESET)
    print(YELLOW + "2. Password Checker" + RESET)
    print(BLUE + "3. Guessing Game" + RESET)
    print(CYAN + "4. Quiz Game" + RESET)
    print(RED + "5. Exit" + RESET)
    choice = input("Apni Choice Likho (1-5): ")

    if choice == "1":
        print(GREEN + "\n--- CALCULATOR ---" + RESET)
        a = int(input("Pehla Number: "))
        b = int(input("Dusra Number: "))
        print("Jama:", a+b)
        print("Minus:", a-b)
        print("Zarb:", a*b)

    elif choice == "2":
        print(YELLOW + "\n--- PASSWORD CHECKER ---" + RESET)
        pw = input("Password Likho: ")
        if len(pw) < 6:
            print(RED + "Weak! 6 se bara likho" + RESET)
        elif pw.isdigit():
            print(YELLOW + "Medium! Numbers + Letters milao" + RESET)
        else:
            print(GREEN + "Strong! MashAllah!" + RESET)

    elif choice == "3":
        print(BLUE + "\n--- GUESSING GAME ---" + RESET)
        secret = random.randint(1, 10)
        guess = int(input("1 se 10 tak guess karo: "))
        if guess == secret:
            print(GREEN + "Jeet Gaye! Secret tha" + str(secret) + RESET)
        else:
            print(RED + "Haar Gaye! Secret tha" + str(secret) + RESET)

    elif choice == "4":
        print(CYAN + "\n--- QUIZ GAME ---" + RESET)
        score = 0
        ans = input("Pakistan ka capital? ")
        if ans.lower() == "islamabad":
            print(GREEN + "Sahi! +1" + RESET)
            score += 1
        ans2 = input("2 + 2 = ? ")
        if ans2 == "4":
            print(GREEN + "Sahi! +1" + RESET)
            score += 1
        print(YELLOW + "Tumhara Score:" + str(score) + "/ 2" + RESET)

    elif choice == "5":
        print(RED + "Allah Hafiz Talha Bhai! Phir Milenge!" + RESET)
        break
    else:
        print(RED + "Ghalat Choice! 1 se 5 tak likho" + RESET)
0
