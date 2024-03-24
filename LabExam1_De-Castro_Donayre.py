game_library = {
    "Donkey Kong": {"Quantity": 3, "Cost": 2},
    "Super Mario Bros": {"Quantity": 5, "Cost": 3},
    "Tetris": {"Quantity": 2, "Cost": 1},
}

user_inventory = {
    "user_inventory": {
        "Donkey Kong": 0,
        "Super Mario Bros": 0,
        "Tetris": 0
    }
}

users = {}
admin_user = "admin"
admin_pass = "adminpass"
username = ""
password = ""
user_coins = 0
user_points = 0

def sign_up(username, user_coins, user_points):
    print("_" * 100)    
    print("\n> Create a new account")
    
    while True:
        try:
            username = str(input("\n\t> Enter your username: "))
            if username in users:
                print("\n\t\t>> Username already exists. Please enter a different username.")
                continue
            else:
                password = str(input("\t> Enter your password (must have at least 8 characters): "))
                while True:
                    try:
                        if len(password) >= 8:            
                            users[username] = {"password": password, "user_coins": user_coins, "user_points": user_points}
                            print(users)
                            print("\n\t\t>> You have successfully signed up to AA Game Rentals.")
                            main_menu(username, user_coins, user_points)
                            break
                        else:
                            print("\n\t\t>> Your password must have at least 8 characters.")
                            sign_up(username, user_coins, user_points)
                            break
                    except ValueError:
                        print("\n\t\t>> [ValueError] Invalid input. Please try again.")
                        sign_up(username, user_coins, user_points)
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            sign_up(username, user_coins, user_points)

def sign_in(username, user_coins, user_points):
    print("_" * 100)   
    print("\n> Sign in to your account")
    
    while True:
        try:
            username = str(input("\n\t> Enter your username: "))
            password = str(input("\t> Enter your password: "))
        
            if users[username]['password'] == password:
                users[username].update(user_inventory)
                print("\n\t\t>> You have signed in successfully to AA Game Rentals.\n")
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Your log-in details are incorrect. Please try again.")
                sign_in(username, user_coins, user_points)
                break
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            sign_in(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Your log-in details are incorrect. Please try again.")
            sign_in(username, user_coins, user_points)

def sign_admin(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Sign in as Administrator")

    while True:
        try:
            adm_user = str(input("\n\t> Enter your username: "))
            adm_pass = str(input("\t> Enter your password: "))
        
            if admin_user == adm_user and admin_pass == adm_pass:
                print("\n\t\t>> You have signed in successfully.")
                admin_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Your log-in details are incorrect. Please try again.")
                sign_admin(username, user_coins, user_points)
                break
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            sign_admin(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Your log-in details are incorrect. Please try again.")
            sign_admin(username, user_coins, user_points)

def display_games(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Display Games")

    while True:
        i = 1
        for games in game_library:
            print(f"\n{i}. {games}")
            i += 1
            for details in game_library[games]:
                print(f"{details}: {game_library[games][details]}")

        try:
                choice = str(input("\n\t> Would you like to go back to the user menu? (Y/N) "))
                if choice == 'N' or choice == 'n':
                    continue
                elif choice == 'Y' or choice == 'y':
                    user_menu(username, user_coins, user_points)
                    break
                else:
                    print("\n\t\t>> Invalid input. Please try again.")
                    continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            display_games(username, user_coins, user_points)

def rent_game(username, user_coins, user_points):
    mod_points = 0

    print("_" * 100)
    print("\n> Rent Game")

    while True:
        i = 1
        for games in game_library:
            print(f"\n{i}. {games}")
            i += 1
            for details in game_library[games]:
                print(f"{details}: {game_library[games][details]}")
        try:
            game_choice = str(input("\n\t> Kindly refer to the game library and type the name of your selected game: ")).lower().title()

            if game_choice in game_library:
                if game_library[game_choice]['Quantity'] > 0:
                    if users[username]['user_coins'] >= game_library[game_choice]['Cost']:
                        game_library[game_choice]['Quantity'] -= 1
                        users[username]['user_coins'] -= game_library[game_choice]['Cost']
                        users[username]['user_inventory'][f'{game_choice}'] += 1
                        print(f"\n\t\t>> You have rented {game_choice} for {game_library[game_choice]['Cost']} coins! You now have a total of {users[username]['user_coins']} coin/s.")
                        if game_library[game_choice]['Cost'] >= 2:
                            mod_points = int(game_library[game_choice]['Cost'] / 2)
                            users[username]['user_points'] += mod_points
                            print(f"\t\t>> You have earned {mod_points} point/s from your purchase! You now have a total of {users[username]['user_points']} point/s.")
                    else:
                        print("\n\t\t>> You do not have enough coins! Please top-up your account on the user menu.")
                        user_menu(username, user_coins, user_points)
                        break
                elif game_library[game_choice]['Quantity'] <= 0:
                    try:
                        stock_choice = str(input(f"\n\t\t>> {game_choice} is currently out of stock. Would you like to choose another game? (Y/N) "))
                        if stock_choice == 'Y' or stock_choice == 'y':
                            continue
                        elif stock_choice == 'N' or stock_choice == 'n':
                            user_menu(username, user_coins, user_points)
                            break
                        else:
                            print("\n\t\t>> Invalid input. Please try again.")
                            continue
                    except ValueError:
                        print("\n\t\t>> [ValueError] Invalid input. Please try again.")
                        rent_game(username, user_coins, user_points)
            else:
                print("\n\t\t>> Game is not available. Please enter a game within our selection.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            rent_game(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Invalid input. Please try again.")
            rent_game(username, user_coins, user_points)

        try:
            choice = str(input("\n\t> Would you like to (A) rent another game or (B) go back to the user menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                rent_game(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            rent_game(username, user_coins, user_points)

def return_game(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Return Game\n")
    
    while True:
        print("\n> Here is the list of your currently rented games:")

        i = 1
        for rented_games in users[username]['user_inventory']:
            print(f"\n{i}. {rented_games}")
            print(f"Inventory: {users[username]['user_inventory'][rented_games]}")
            i += 1

        try:
            return_item = str(input("\n\t> Kindly refer to the game library and type the name of the game that you want to return: ")).lower().title()
            if return_item in game_library:
                return_qty = int(input("\t> How many copies would you like to return? "))
                if return_qty <= users[username]['user_inventory'][f'{return_item}']:
                    users[username]['user_inventory'][f'{return_item}'] -= return_qty
                    game_library[return_item]['Quantity'] += return_qty
                    print(f"\n\t\t>> You have returned {return_qty} copy/ies of {return_item}. You now have {users[username]['user_inventory'][f'{return_item}']} stock/s of {return_item} in your inventory. Thank you for renting from AA Game Rentals!")
                else:
                    print(f"\n\t\t>> You do not have enough copies of {return_item} to return. Please try again.")
                    return_game(username, user_coins, user_points)
                    break
            else:
                print("\n\t\t>> Game is not available. Please enter a game within our selection.")
                continue       
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            return_game(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Invalid input. Please try again.")
            return_game(username, user_coins, user_points)
        
        try:
            choice = str(input("\n\t> Would you like to (A) return another game or (B) go back to the user menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                return_game(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            return_game(username, user_coins, user_points)

def topup_account(username, user_coins, user_points):
    topup_user_coins = 0

    print("_" * 100)
    print("\n> Top-up Account")

    while True:
        try:
            topup_user_coins = int(input("\n\t> Enter the amount of coins to add to your account: "))
            users[username]['user_coins'] += topup_user_coins
            print(f"\n\t\t>> You have topped up {topup_user_coins} coin/s. You now have a total of {users[username]['user_coins']} coin/s.")
        except ValueError:
            print("\n\t\t>> Invalid input. Please try again.")
            topup_account(username, user_coins, user_points)

        try:
            choice = str(input("\n\t> Would you like to (A) top-up again or (B) go back to the user menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                topup_account(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            topup_account(username, user_coins, user_points)

def check_inventory(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Check Inventory")

    while True:
        print("\n> Here is the list of your currently rented games:")

        i = 1
        for rented_games in users[username]['user_inventory']:
            print(f"\n{i}. {rented_games}")
            print(f"Inventory: {users[username]['user_inventory'][rented_games]}")
            i += 1

        try:
            choice = str(input("\n\t> Would you like to go back to the user menu? (Y/N) "))
            if choice == 'N' or choice == 'n':
                check_inventory(username, user_coins, user_points)
                break
            elif choice == 'Y' or choice == 'y':
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            check_inventory(username, user_coins, user_points)

def redeem_game(username, user_coins, user_points):
    free_games = 0
    mod_redeem = 0

    print("_" * 100)
    print("\n> Redeem a Free Game")
    print("\n> Using your points earned from renting, you can redeem free games!")
    print("> Five (5) points is equivalent to one (1) free game.")
    print(f"\n> You have a total of {users[username]['user_points']} point/s.")

    while True:
        if users[username]['user_points'] < 5:
            print("\n\t\t>> Sorry, you do not have enough points to redeem a free game.")
        else:
            mod_redeem = int(users[username]['user_points'] / 5)
            free_games += mod_redeem

            try:
                choice = str(input(f"\n\t> Congratulations! You can redeem {free_games} free game/s of your choice from AA Game Rentals! Would you like to redeem them now? (Y/N) "))
                if choice == 'N' or choice == 'n':
                    user_menu(username, user_coins, user_points)
                    break
                elif choice == 'Y' or choice == 'y':
                    while True:
                        i = 1
                        game_inventory = []

                        for games in game_library:
                            print(f"\n{i}. {games}")
                            i += 1

                            if 'Quantity' in games:
                                game_inventory.append({'Quantity': games['Quantity']})

                            print(f"Quantity: {game_library[games]['Quantity']}")

                        try:
                            game_choice = str(input("\n\t> Kindly refer to the game library and type the name of your selected game: ")).lower().title()

                            if game_choice in game_library:
                                if game_library[game_choice]['Quantity'] > 0:
                                    game_library[game_choice]['Quantity'] -= 1
                                    users[username]['user_inventory'][f'{game_choice}'] += 1
                                    users[username]['user_points'] -= 5
                                    print(f"\n\t\t>> You have redeemed {game_choice} for 5 points! You now have a total of {users[username]['user_points']} point/s.")
                                    break
                                elif game_library[game_choice]['Quantity'] <= 0:
                                    try:
                                        stock_choice = str(input(f"\n\t\t>> {game_choice} is currently out of stock. Would you like to choose another game? (Y/N) "))
                                        if stock_choice == 'Y' or stock_choice == 'y':
                                            redeem_game(username, user_coins, user_points)
                                            break
                                        elif stock_choice == 'N' or stock_choice == 'n':
                                            user_menu(username, user_coins, user_points)
                                            break
                                        else:
                                            print("\n\t\t>> Invalid input. Please try again.")
                                            continue
                                    except ValueError:
                                        print("\n\t\t>> [ValueError] Invalid input. Please try again.")
                                        redeem_game(username, user_coins, user_points)
                            else:
                                print("\n\t\t>> Game is not available. Please enter a game within our selection.")
                                redeem_game(username, user_coins, user_points)
                                break
                        except ValueError:
                            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
                            redeem_game(username, user_coins, user_points)
                        except KeyError:
                            print("\n\t\t>> [KeyError] Invalid input. Please try again.")
                            redeem_game(username, user_coins, user_points)

                        try:
                            if users[username][user_points] >= 5:
                                choice = str(input("\n\t> Would you like to (A) redeem another game or (B) go back to the user menu? (A/B) "))
                                if choice == 'A' or choice == 'a':
                                    redeem_game(username, user_coins, user_points)
                                    break
                                elif choice == 'B' or choice == 'b':
                                    user_menu(username, user_coins, user_points)
                                    break
                                else:
                                    print("\n\t\t>> Invalid input. Please try again.")
                                    continue
                            else:
                                choice = str(input("\n\t> Would you like to go back to the user menu? (Y/N) "))
                                if choice == 'N' or choice == 'n':
                                    redeem_game(username, user_coins, user_points)
                                    break
                                elif choice == 'Y' or choice == 'y':
                                    user_menu(username, user_coins, user_points)
                                    break
                                else:
                                    print("\n\t\t>> Invalid input. Please try again.")
                                    continue
                        except ValueError:
                            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
                            redeem_game(username, user_coins, user_points)
                else:
                    print("\n\t\t>> Invalid input. Please try again.")
                    redeem_game(username, user_coins, user_points)
                    break
            except ValueError:
                print("\n\t\t>> [ValueError] Invalid input. Please try again.")
                redeem_game(username, user_coins, user_points)

        try:
            choice = str(input("\n\t> Would you like to go back to the user menu? (Y/N) "))
            if choice == 'N' or choice == 'n':
                redeem_game(username, user_coins, user_points)
                break
            elif choice == 'Y' or choice == 'y':
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            redeem_game(username, user_coins, user_points)
                
def check_points(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Check Points")
    while True:
        try:
            points_choice = str(input(f"\n\t> You have a total of {users[username]['user_points']} point/s. Would you like to rent games to earn points? (Y/N) "))
            if points_choice == 'Y' or points_choice == 'y':
                rent_game(username, user_coins, user_points)
            elif points_choice == 'N' or points_choice == 'n':
                user_menu(username, user_coins, user_points)
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                check_points(username, user_coins, user_points)
                break
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            check_points(username, user_coins, user_points)

def add_qty(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Add Quantity")
    while True:
        i = 1
        game_inventory = []

        for games in game_library:
            print(f"\n{i}. {games}")
            i += 1

            if 'Quantity' in games:
                game_inventory.append({'Quantity': games['Quantity']})

            print(f"Quantity: {game_library[games]['Quantity']}")
    
        try:
            game_choice = str(input("\n\t> Kindly refer to the game library and type the game that you want to increase the stocks of: ")).lower().title()
            if game_choice in game_library:
                game_qty = int(input("\t> Kindly enter the number of stocks you wish to add: "))
                game_library[game_choice]['Quantity'] += game_qty
                print(f"\n\t\t>> {game_choice} is now restocked to {game_library[game_choice]['Quantity']} copy/ies.")

                i = 1
                game_inventory = []
                print("\nHere is the game library with the updated stocks:")

                for games in game_library:
                    print(f"\n{i}. {games}")
                    i += 1

                    if 'Quantity' in games:
                        game_inventory.append({'Quantity': games['Quantity']})

                    print(f"Quantity: {game_library[games]['Quantity']}")
            else:
                print("\n\t\t>> Game is not available. Please enter a game within our selection.")
                add_qty(username, user_coins, user_points)
                break
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            add_qty(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Invalid input. Please try again.")
            add_qty(username, user_coins, user_points)

        try:
            choice = str(input("\n\t> Would you like to (A) add more stocks to another game or (B) go back to the admin menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                add_qty(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                admin_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            add_qty(username, user_coins, user_points)

def change_price(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Change Price")

    while True:
        try:
            i = 1
            game_inventory = []
            print("\nHere is the updated game library:")

            for games in game_library:
                print(f"\n{i}. {games}")
                i += 1

                if 'Cost' in games:
                    game_inventory.append({'Cost': games['Cost']})

                print(f"Cost: {game_library[games]['Cost']}")

            print("\n1. Increase the Price")
            print("2. Decrease the Price")

            choice = int(input("\n\t> Kindly enter the numerical input corresponding to your choice: "))
            if choice == 1:
                print("\n> Increase Price")

                game_choice = str(input("\n\t> Kindly refer to the game library and type the game that you want to increase the price of: ")).lower().title()
                if game_choice in game_library:
                    new_price = int(input(f"\t> Kindly enter the amount that you wish to add to the current cost of {game_choice}: "))
                    game_library[game_choice]['Cost'] += new_price
                    print(f"\n\t\t>> The cost of {game_choice} is now {game_library[game_choice]['Cost']} coin/s.")
                else:
                   print("\n\t\t>> Game is not available. Please enter a game within our selection.")
                   change_price(username, user_coins, user_points)
                   break
            elif choice == 2:
                print("\n> Decrease Price")

                game_choice = str(input("\n\t> Kindly refer to the game library and type the game that you want to decrease the price of: ")).lower().title()
                if game_choice in game_library:
                    new_price = int(input(f"\t> Kindly enter the amount that you wish to subtract to the current cost of {game_choice}: "))
                    if new_price <= game_library[game_choice]['Cost']:
                        game_library[game_choice]['Cost'] -= new_price
                        print(f"\n\t\t>> The cost of {game_choice} is now {game_library[game_choice]['Cost']} coin/s.")
                        
                        i = 1
                        game_inventory = []
                        print("\nHere is the game library with the updated costs:")

                        for games in game_library:
                            print(f"\n{i}. {games}")
                            i += 1

                            if 'Cost' in games:
                                game_inventory.append({'Cost': games['Cost']})

                            print(f"Cost: {game_library[games]['Cost']}")
                    else:
                        print("\n\t\t>> Your input cannot be greater than the current cost of the game. Please try again.")
                        continue
                else:
                   print("\n\t\t>> Game is not available. Please enter a game within our selection.")
                   change_price(username, user_coins, user_points)
                   break

        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            change_price(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Invalid input. Please try again.")
            change_price(username, user_coins, user_points)

        try:
            choice = str(input("\n\t> Would you like to (A) adjust the prices once more or (B) go back to the admin menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                change_price(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                admin_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            change_price(username, user_coins, user_points) 

def add_game(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Add Game")

    while True:
        try:
            i = 1
            for games in game_library:
                print(f"\n{i}. {games}")
                i += 1
                for details in game_library[games]:
                    print(f"{details}: {game_library[games][details]}")
            
            new_game_name = str(input("\n\t> Kindly enter the name of your new game (case-sensitive): "))
            if new_game_name in game_library:
                print("\n\t\t>> That game is already in the game library library. Please input a game that is not yet found in our library.")
                add_game(username, user_coins, user_points)
                break
            else:
                new_game_qty = int(input("\t> Kindly enter the number of stocks of your new game: "))
                new_game_cost = int(input("\t> Kindly enter the cost of your new game: "))
                game_library[new_game_name] = {"Quantity": new_game_qty, "Cost": new_game_cost}
                user_inventory['user_inventory'][f'{new_game_name}'] = 0
                print(user_inventory)

                print("\nHere is the updated game library with your new game:")
                i = 1
                for games in game_library:
                    print(f"\n{i}. {games}")
                    i += 1
                    for details in game_library[games]:
                        print(f"{details}: {game_library[games][details]}")
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            add_game(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Invalid input. Please try again.")
            add_game(username, user_coins, user_points)

        try:
            choice = str(input("\n\t> Would you like to (A) add another game or (B) go back to the admin menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                add_game(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                admin_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            add_game(username, user_coins, user_points)

def admin_menu(username, user_coins, user_points):
    print("_" * 100)
    print(f"\n> Logged in as {admin_user}.\n")
    print("1. Add Quantity")
    print("2. Increase Price")
    print("3. Add Game")
    print("4. Log Out")

    try:
        choice = int(input("\n> Kindly enter the numerical input corresponding to your directory selection: "))
        if choice == 1:
            add_qty(username, user_coins, user_points)
            return
        if choice == 2:
            change_price(username, user_coins, user_points)
            return
        elif choice == 3:
            add_game(username, user_coins, user_points)
            return
        elif choice == 4:
            main_menu(username, user_coins, user_points)
            return
        else:
           print("\n\t\t>> Invalid input. Please try again.")
           admin_menu(username, user_coins, user_points)
    except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            admin_menu(username, user_coins, user_points)

def user_menu(username, user_coins, user_points):
    print("_" * 100)
    print(f"\n> Logged in as {username}.")
    print(f"\n> Coins: {users[username]['user_coins']} coin/s")
    print(f"> Points: {users[username]['user_points']} point/s\n")
    print("1. Display Games")
    print("2. Rent a Game")
    print("3. Return a Game")
    print("4. Top-Up Account")
    print("5. Check Inventory")
    print("6. Redeem a Free Game")
    print("7. Check Points")
    print("8. Log Out")

    try:
        choice = int(input("\n> Kindly enter the numerical input corresponding to your directory selection: "))
        if choice == 1:
            display_games(username, user_coins, user_points)
            return
        if choice == 2:
            rent_game(username, user_coins, user_points)
            return
        elif choice == 3:
            return_game(username, user_coins, user_points)
            return
        elif choice == 4:
            topup_account(username, user_coins, user_points)
            return
        elif choice == 5:
            check_inventory(username, user_coins, user_points)
            return
        elif choice == 6:
            redeem_game(username, user_coins, user_points)
            return
        elif choice == 7:
            check_points(username, user_coins, user_points)
            return
        elif choice == 8:
            user_coins = 0
            user_points = 0

            main_menu(username, user_coins, user_points)
            return
        else:
           print("\n\t\t>> Invalid input. Please try again.")
           user_menu(username, user_coins, user_points)
    except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            user_menu(username, user_coins, user_points)

def main_menu(username, user_coins, user_points): 
    print("_" * 100)
    print("\nWelcome to AA Game Rentals!\n")
    print("1. Sign up")
    print("2. Sign in")
    print("3. Sign in as Administrator")
    print("4. Exit")

    try:
        choice = int(input("\n> Kindly enter the numerical input corresponding to your directory selection: "))
        if choice == 1:
            sign_up(username, user_coins, user_points)
            return
        elif choice == 2:
            sign_in(username, user_coins, user_points)
            return
        elif choice == 3:
            sign_admin(username, user_coins, user_points)
            return
        elif choice == 4:
            exit()
        else:
           print("\n\t\t>> Invalid input. Please try again.")
           add_game(username, user_coins, user_points)
    except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            main_menu(username, user_coins, user_points)

main_menu(username, user_coins, user_points)