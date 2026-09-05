import time
import sys
import random
import webbrowser

# Stats karakter
role = None
killdragon = False
result = None
player_stats = {     # ini disebut dictionary (menyimpan data yang banyak dan bisa berbagai jenis)
    'health': 100,   # Kesehatan pemain
    'strength': 15,  # Kekuatan pemain
    'intelligence': 8,  # Kecerdasan pemain
    'stamina': 15,  # Daya tahan pemain
    'charisma': 7,  # Karisma atau kemampuan berinteraksi
    'inventory': [],  # Barang-barang yang dimiliki pemain
    'level': 1,  # Level karakter
    'gold':10 #mata uang
}

def cashout(number):
    player_stats['gold']  + number
    type_writer(f"you claimed {number} gold")

def teammate():
    Mark = {'name': 'Mark', 'health': 80, 'attack': 75}
    Albert = {'name': 'Albert', 'health': 100, 'attack': 15}
    Paul = {'name': 'Paul', 'health': 400, 'attack': 5}
    return Mark, Albert, Paul

def show_team():
    team = teammate()
    for member in team:
        print(f"Name: {member['name']}, Health: {member['health']}, Attack: {member['attack']}")



    


def use_item(item):
    # Cek apakah item ada di inventori
    if item in player_stats['inventory']:
        # Definisikan efek dari setiap item
        item_effects = {
            "Health Potion": {"health": 20},
            "Stamina Elixir": {"stamina": 15},
            "Strength Amulet": {"strength": 10},
            "Magic Tome": {"intelligence": 15}
        }

        # Jika item memiliki efek, terapkan efeknya
        if item in item_effects:
            for stat, value in item_effects[item].items():
                player_stats[stat] += value
                type_writer(f"You used {item} and gained {value} {stat}!")
            
            # Hapus item dari inventori
            player_stats['inventory'].remove(item)
        else:
            type_writer(f"{item} has no effect or is not usable.")
    else:
        type_writer(f"You don't have {item} in your inventory.")

owned_cities = ["sterling"]



def capture_city(city_name):
    """Mengembalikan kota ke kendali pemain."""
    if city_name not in owned_cities:
        owned_cities.append(city_name)
        type_writer(f"{city_name} is now under your control!")
    else:
        type_writer(f"{city_name} is already under your control.")

cities_warmoth = [
    "Blackreach",      # Kota utama yang dikelilingi kabut hitam
    "Gloomspire",      # Kota menara tinggi tempat penyihir gelap berkumpul
    "Ravenmoor",       # Kota di tengah rawa penuh burung gagak
    "Duskhaven",       # Kota pelabuhan yang selalu diselimuti senja
    "Ironhold",        # Kota benteng bekas pertempuran besar
    "Wraithfall",      # Kota hantu yang muncul saat bulan purnama
    "Bloodstone",      # Kota tambang batu darah yang terkutuk
    "Ashenvale",       # Kota mati di tengah hutan terbakar
    "Necroth",         # Kota necromancer yang tersembunyi di lembah
    "Shadowfen",       # Kota rawa penuh racun dan makhluk kegelapan
    "Embergrave",      # Kota bekas peradaban yang sekarang jadi puing
    "Grimkeep",        # Kota benteng tempat para kesatria kegelapan
    "Frostbound",      # Kota es yang ditinggalkan setelah perang besar
    "Mournhold",       # Kota berkabung yang selalu turun hujan
    "Vilebrook",       # Kota sungai beracun tempat klan pencuri bersembunyi
    "Thorncrest",      # Kota berduri di pegunungan terjal
    "Soulhaven",       # Kota pengasingan bagi jiwa-jiwa tersesat
    "Darkveil",        # Kota tersembunyi di balik kabut tebal
    "Cryptwatch",      # Kota pemakaman besar yang dijaga undead
    "Voidspire",       # Kota menara iblis yang muncul di tengah padang pasir
]

# Fungsi untuk menampilkan stats pemain
def show_stats():
    print("\n--- Player Stats ---")
    print(f"Health: {player_stats['health']}")
    print(f"Health: {player_stats['gold']}")
    print(f"Strength: {player_stats['strength']}")
    print(f"Intelligence: {player_stats['intelligence']}")
    print(f"Stamina: {player_stats['stamina']}")
    print(f"Charisma: {player_stats['charisma']}")
    print(f"Level: {player_stats['level']}")
    print(f"Inventory: {', '.join(player_stats['inventory']) if player_stats['inventory'] else 'Empty'}")
    print("---------------------\n")

def recover_health():
    type_writer("you just got healed/revive")
    player_stats['health'] = 100

# Fungsi untuk mengetikkan teks secara perlahan
def type_writer(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Permainan dimulai
print("Welcome to my game")
video_url = "https://www.youtube.com/watch?v=2qBlE2-WL60"
developer = "developer: ujang"
if developer != "developer: Agape":
    type_writer("this game is hacked the real developer is Agape")
    webbrowser.open(video_url)
    exit()
print(developer)
type_writer("This is a dark fantasy genre game.")
name = input("Input your name: ")
type_writer("are you ready to go to battle field and fight all the enemy?.")
ask = input("Type 'yes' to start: ")

if ask.lower() == "yes":
    game_start = True
    type_writer(f"Good luck, {name}!")
    game()
    


    def game():
        type_writer("It's a long day since the King of Warmoth attacked the country...")
        time.sleep(1)
        type_writer("People are suffering and the world is full of darkness.")
        time.sleep(1)
        type_writer("You are here to save the world.")
        time.sleep(1)
        type_writer("Story starts in a house of Sterling Village.")
        time.sleep(1)
        type_writer("You just came from the woods to play with your friends.")
        time.sleep(1)
        type_writer("Your grandma is sick right now.")
        time.sleep(1)
        type_writer("Grandma: 'Son, where have you been?'")
        time.sleep(2)

        choices()

    def choices():
        type_writer("Do you want to say:")
        time.sleep(1)
        type_writer("1. Tell her you were playing in the woods with your friends.")
        type_writer("2. Lie and say you were out looking for herbs to help her.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            tell_truth()
        elif choice == "2":
            lie_to_grandma()
        else:
            type_writer("Invalid choice. Try again!")
            choices()

    def tell_truth():
        type_writer(f"{name}: I just came from the woods playing with my friends.")
        time.sleep(2)
        type_writer("Grandma was disappointed but also grateful for having an honest child.")
        time.sleep(2)
        player_stats['charisma'] += 2
        type_writer(f"Your charisma increased by 2! Current charisma: {player_stats['charisma']}")
        time.sleep(2)
        type_writer(f"{name}:ma i want to go outside see you")
        time.sleep(2)
        continue_story()

    def lie_to_grandma():
        type_writer(f"{name}: I just came from hunting in the woods.")
        time.sleep(2)
        type_writer("Grandma: 'Thank you, my good boy.'")
        time.sleep(2)
        type_writer("Grandma: 'Where is the food?'")
        time.sleep(2)
        type_writer(f"{name}: Uhh... uhh?")
        time.sleep(1)
        type_writer("Grandma: 'Are you lying to me again?'")
        time.sleep(2)
        type_writer(f"{name}:im sorry grandma")
        time.sleep(2)
        type_writer("grandma:getout of here!")
        continue_story()

    def continue_story():
        type_writer("You are outside the house right now.")
        time.sleep(2)
        type_writer("A soldier comes up to you.")
        time.sleep(2)
        type_writer("Soldier: 'Hey young man, you are 12 years old. You are old enough to be a man. Come with us to be a soldier!'")
        time.sleep(2)
        choices2()

    def choices2():
        type_writer("Do you want to:")
        time.sleep(1)
        type_writer("1. Try to escape from them.")
        type_writer("2. Cooperate with them.")
        choice2 = input("Enter the number of your choice: ")

        if choice2 == "1":
            arrested()
        elif choice2 == "2":
            cooperate()
        else:
            type_writer("Invalid choice! Try again.")
            choices2()

    def arrested():
        type_writer("You try to escape, but the soldiers catch you and arrest you.")
        time.sleep(2)
        type_writer("Soldier: 'Gotcha! You can't escape now.'")
        player_stats['charisma'] -= 2
        type_writer(f"Your charisma decreased by 2! Current charisma: {player_stats['charisma']}")
        time.sleep(2)
        barrack()

    def cooperate():
        type_writer("You decide to cooperate with the soldiers. They take you to the barracks.")
        time.sleep(2)
        barrack()

    def barrack():
        type_writer(f"{name}: 'Where am I?'")
        time.sleep(2)
        type_writer("Raider: 'Welcome to the barracks. You will learn how to fight against mages, witches, dragons, soldiers, kings, etc.'")
        time.sleep(2)
        type_writer(f"{name}: 'Wow, I will learn how to fight like a real man?'")
        time.sleep(1)
        type_writer("Raider: 'Say it politely!'")
        time.sleep(1)
        type_writer("Raider: 'In the barracks, the proper response is \"Yes, sir!\" and \"No, sir!\"'")
        time.sleep(2)
        type_writer(f"{name}: 'Sir, yes sir!'")
        time.sleep(2)
        type_writer("Raider: 'Let's start the practice.'")
        training()

    def training():
        type_writer("A training dummy appears in front of you. Let's practice!")
        time.sleep(1)

        # Status musuh (dummy)
        dummy = {'name': 'Training Dummy', 'health': 30, 'attack': 5}

        # Multiplier untuk strength
        strength_multiplier = 0.5

        # Mulai mini-game bertarung
        while dummy['health'] > 0 and player_stats['health'] > 0:
            type_writer(f"{dummy['name']} health: {dummy['health']}")
            type_writer(f"Your health: {player_stats['health']}")
            type_writer(f"Your strength: {player_stats['strength']}")
            type_writer("What will you do?")
            type_writer("1. Attack")
            type_writer("2. Defend")
            choice = input("Choose an action (1/2): ")

            if choice == "1":
                # Hitung damage berdasarkan strength
                base_damage = random.randint(5, 10)
                damage = base_damage + int(player_stats['strength'] * strength_multiplier)
                dummy['health'] -= damage
                type_writer(f"You dealt {damage} damage to {dummy['name']}!")
            
            elif choice == "2":
             # Pertahanan
                defense = random.randint(2, 5)
                reduced_damage = max(dummy['attack'] - defense, 0)
                player_stats['health'] -= reduced_damage
                type_writer(f"You blocked the attack, reducing damage by {defense}.")
            else:
                type_writer("Invalid choice! Try again.")

            # Dummy menyerang
            if dummy['health'] > 0:
                player_stats['health'] -= dummy['attack']
                type_writer(f"{dummy['name']} attacks! You lost {dummy['attack']} health.")

            # Cek jika pemain kalah
            if player_stats['health'] <= 0:
                type_writer("You have been defeated! Training failed.")
                break

        # Jika dummy kalah
        if dummy['health'] <= 0:
            type_writer(f"You defeated the {dummy['name']}! Well done, soldier!")
            player_stats['level'] += 1
            type_writer(f"Your level increased to {player_stats['level']}!")
            recover_health()
            question()

    
    def question():
        type_writer("Raider:'are you ready to fight the enemy?'")
        time.sleep(1)
        type_writer("1.'sir,yes sir'")
        type_writer("2. 'no sir'")
        choice3 = input("Enter the number of your choice: ")        

        
        if choice3 == "1":
            war()
        elif choice3 == "2":
            war2()
        else:
            type_writer("Invalid choice! Try again.")
            choices2()

    
    def add_to_inventory(item):
        player_stats['inventory'].append(item)
        print(f"{item} has been added to your inventory.")

    def increase_strength(amount):
        player_stats['strength'] += amount
        print(f"Strength increased by {amount}. Current strength: {player_stats['strength']}")


    def increase_Intelligence(amount):
        player_stats['Intelligence'] += amount
        print(f"Intelligence increased by {amount}. Current Intelligence: {player_stats['Intelligence']}")

    def war():
        type_writer("raider:'Take this sword!'")
        sword = "Mighty Sword"
        add_to_inventory(sword)
        increase_strength(20)  # Menambahkan 20 strength
        choose_role()


    def war2():
        type_writer("raider:'I'm sorry son, life is too hard for you.'")
        type_writer("The war is too intense... You decide to give up.")
        type_writer("Game Over.")
        sys.exit()  # Menghentikan program sepenuhnya




    def change_role(new_role):
        global role
        role = new_role
        type_writer(f"Your role has been changed to {role}.")




    def choose_role():
        type_writer("raider: 'Choose your path, young soldier. Your destiny awaits.'")
        time.sleep(1)
        type_writer("1. Knight - Balanced Strength and Defense")
        type_writer("2. Cavalry - High Speed and Charge Attack")
        type_writer("3. Mage - Powerful Magic, Low Defense")
        type_writer("4. Berserker - High Strength, Low Defense")
        role = input("Enter the number of your chosen role (1/2/3/4): ")

        if role == "1":
            player_stats['strength'] += 15
            player_stats['health'] += 20
            player_stats['stamina'] += 10
            type_writer("You chose the Knight. A balanced warrior with strong defense.")
            type_writer(f"Strength: {player_stats['strength']}, Health: {player_stats['health']}, Stamina: {player_stats['stamina']}")
            change_role("Knight")
            gowar()


        elif role == "2":
            player_stats['strength'] += 20
            player_stats['stamina'] += 15
            player_stats['intelligence'] += 5
            type_writer("You chose the Cavalry. A swift and powerful mounted warrior.")
            type_writer(f"Strength: {player_stats['strength']}, Stamina: {player_stats['stamina']}, Intelligence: {player_stats['intelligence']}")
            change_role("Cavalry")
            cavalry_training() 

        elif role == "3":
            player_stats['intelligence'] += 25
            player_stats['health'] += 10
            player_stats['stamina'] += 5
            type_writer("You chose the Mage. Master of destructive magic.")
            type_writer(f"Intelligence: {player_stats['intelligence']}, Health: {player_stats['health']}, Stamina: {player_stats['stamina']}")
            change_role("Mage")
            mage()

        elif role == "4":
            player_stats['strength'] += 30
            player_stats['health'] += 5
            player_stats['stamina'] += 5
            type_writer("You chose the Berserker. A raging powerhouse with little defense.")
            type_writer(f"Strength: {player_stats['strength']}, Health: {player_stats['health']}, Stamina: {player_stats['stamina']}")
            change_role("Berseker")
            gowar()

        else:
            type_writer("Invalid choice. Choose again.")
            return choose_role()


    def mage():
        type_writer("Mage:welcome to our society")
        time.sleep(2)
        type_writer("Mage:today you will learn how to be great mage")
        time.sleep(2)
        type_writer("Mage:take this wand")
        wand = "magical staff"
        add_to_inventory(wand)
        increase_Intelligence(100) 
        study() 
    
    def study():
        type_writer("Mage: 'Now that you have the magical staff, let's practice your spells.'")
        time.sleep(2)
        type_writer("Mage: 'I will give you a simple spell to cast. Focus and unleash your power!'")
        time.sleep(2)

        # Mini game untuk Mage
        spells = ["Fireball", "Ice Blast", "Thunder Strike"]
        chosen_spell = random.choice(spells)

        type_writer(f"Mage: 'Try to cast the spell {chosen_spell} correctly.'")
        time.sleep(1)
        user_spell = input("Enter the spell: ").strip()

        if user_spell.lower() == chosen_spell.lower():
            type_writer(f"You successfully cast {chosen_spell}! Your intelligence increases.")
            increase_Intelligence(50)
        else:
            type_writer(f"You failed to cast {chosen_spell}. Your stamina decreases.")
            player_stats['stamina'] -= 10
            type_writer(f"Stamina: {player_stats['stamina']}")

        # Kembali ke latihan
        type_writer("Mage: 'Good job. youre ready enough to go to frontline.'")
        player_stats['stamina'] == 20
        player_stats['stamina'] += 60
        time.sleep(2)
        gowar()

    def cavalry_training():
        global role, result
        type_writer("Cavalry Trainer: 'Welcome to the cavalry training ground!'")
        time.sleep(2)
        type_writer("Cavalry Trainer: 'Today, you'll learn how to charge effectively and strike with precision.'")
        time.sleep(2)
        type_writer("Cavalry Trainer: 'Take this spear and mount your horse!'")
    
        # Menambahkan spear ke inventory dan meningkatkan strength
        spear = "Cavalry Spear"
        add_to_inventory(spear)
        increase_strength(65)

        time.sleep(2)
        type_writer("You are now on your horse, facing a line of training dummies.")
        time.sleep(2)
        type_writer("Cavalry Trainer: 'Prepare to charge! Aim for the dummies and strike at the right moment!'")
        time.sleep(2)

        # Mini game
        targets = ["Left", "Center", "Right"]
        hit_count = 0

        for i in range(3):
            target = random.choice(targets)
            type_writer(f"The target appears on the {target}!")
            time.sleep(1)
            user_choice = input("Choose your strike direction (Left/Center/Right): ").strip().capitalize()

            if user_choice == target:
                type_writer("You hit the target! Your strength increases!")
                increase_strength(20)
                hit_count += 1
            else:
                type_writer("You missed the target. Stay focused!")

    # Menentukan hasil latihan
        if hit_count >= 2:
            type_writer(f"You successfully hit {hit_count} targets! Your cavalry skills are improving.")
            player_stats['level'] += 1
            type_writer(f"Your level increased to {player_stats['level']}!")
        else:
            type_writer(f"You only hit {hit_count} targets. You need more practice.")

        type_writer("Cavalry Trainer: 'Good job! Keep practicing to become a true cavalry warrior!'")
        gowar()
        


    def gowar():
        global role, player_stats
        type_writer(f"you cam inside the field by using {role}")

        type_writer("You step into the battlefield. The air is thick with the scent of blood and steel.")
        time.sleep(2)

        
        enemy = {"name": "Enemy Soldier", "health": 100, "attack": 15}

        enemycount = 5





                
        type_writer(f"You are fighting as a {role}!")

        while enemycount > 0:

            while enemy["health"] > 0 and player_stats["health"] > 0:
                type_writer(f"Enemy health: {enemy['health']}")
                type_writer(f"Your health: {player_stats['health']}")
                type_writer("1. Attack")
                type_writer("2. Special Ability")
                action = input("Choose your action (1/2): ").strip()

            # Sistem serangan dan kemampuan khusus berdasarkan role
                if action == "1":
                    if role == "Knight":
                        damage == player_stats['strength'] + random.randint(10, 20)
                    elif role == "Cavalry":
                        damage = player_stats['strength'] + random.randint(20, 30)
                    elif role == "Mage":
                        damage = player_stats['intelligence'] + random.randint(30, 40)
                    elif role == "Berserker":
                        damage = player_stats['strength'] + random.randint(30, 50)

                    enemy["health"] -= damage
                    type_writer(f"You dealt {damage} damage to the {enemy['name']}!")

                elif action == "2":
                    if role == "Knight":
                        type_writer("You raise your shield, blocking the next attack completely!")
                        player_stats["stamina"] -= 5
                        enemy["attack"] = 0

                    elif role == "Cavalry":
                        type_writer("You charge with your spear, delivering a devastating blow!")
                        damage = player_stats['strength'] * 2
                        enemy["health"] -= damage
                        player_stats["stamina"] -= 10
                        type_writer(f"You dealt {damage} damage but lost 10 stamina!")

                    elif role == "Mage":
                        type_writer("You cast a powerful spell, burning the enemy!")
                        damage = player_stats['intelligence'] * 1.5
                        enemy["health"] -= damage
                        player_stats["stamina"] -= 5
                        type_writer(f"You dealt {damage} magic damage but lost 5 stamina!")

                    elif role == "Berserker":
                        type_writer("You enter a frenzied state, striking wildly!")
                        damage = player_stats['strength'] * 1.8
                        enemy["health"] -= damage
                        player_stats["health"] -= 10
                        type_writer(f"You dealt {damage} damage but also hurt yourself!")

                else:
                    type_writer("Invalid choice. Try again.")
                    continue

                # Musuh menyerang
                if enemy["health"] > 0:
                    player_stats["health"] -= enemy["attack"]
                    type_writer(f"The {enemy['name']} attacks! You lost {enemy['attack']} health.")

                elif enemy["health"] <= 0 and enemycount > 0:
                    enemy['health'] = 100
                    enemycount -= 1
                    type_writer(f"new enemy attack you. there is {enemycount} enemy left")
                    continue


                elif enemy["health"] <= 0 and enemycount <= 0:
                    recover_health()
                    break


    # Hasil pertempuran
        if player_stats["health"] > 0:
            type_writer(f"Victory! You defeated the {enemy['name']}!")
            player_stats["level"] += 3
            type_writer(f"Your level increased to {player_stats['level']}!")
            time.sleep(2)
            type_writer("you have defeated the last enemy in Voidspire")
            capture_city("Voidspire")
            cashout(80)
            town()
        else:
            type_writer("You have been defeated... The battlefield grows silent.")


    def town():
        if killdragon == False:
            type_writer("kill the dragon reward: lots of gold")
        elif killdragon == True:
            choosetown()
            
    def choosetown():
        type_writer("what do you want to do?")
        print("1.shop")
        print("2.hunt goblin")
        print("3.mount a dragon")
        print("4.check stats")
        print("5.do mission")

        towner = input("choose the number you want")

        if towner == "1":
            shop()
        
        elif towner == "2":
            hunt()

        elif towner == "3":
            dragon_fight()

        elif towner == "4":
            show_stats()
            town()
        
        elif towner == "5":
            continue2()

        else:
            print("invalid input")
            return town()


    def shop():
        type_writer("Welcome to the shop! Here, you can buy items to aid you in battle.")
        time.sleep(1)

        # Daftar barang di shop
        items = {
           '1': {'name': 'Health Potion', 'price': 50, 'effect': {'health': 20}},
            '2': {'name': 'Stamina Elixir', 'price': 30, 'effect': {'stamina': 15}},
            '3': {'name': 'Strength Amulet', 'price': 100, 'effect': {'strength': 10}},
            '4': {'name': 'Magic Tome', 'price': 120, 'effect': {'intelligence': 15}},
            '5': {'name': 'Exit Shop', 'price': 0, 'effect': {}}
        }

        while True:
            # Menampilkan barang di shop
            type_writer("Available items:")
            for key, item in items.items():
                type_writer(f"{key}. {item['name']} - {item['price']} gold")

            # Memilih barang
            choice = input("Choose an item to buy (1-5): ")

            if choice in items:
                item = items[choice]

                if choice == '5':
                    type_writer("You exited the shop.")
                    town()

                if player_stats['gold'] >= item['price']:
                    player_stats['gold'] -= item['price']
                    for stat, value in item['effect'].items():
                        player_stats[stat] += value
                    add_to_inventory(item['name'])
                    type_writer(f"You bought {item['name']}!")
                    type_writer(f"Your current stats: {player_stats}")
                else:
                    type_writer("Not enough gold!")
            else:
                type_writer("Invalid choice. Try again.")

    def hunt():
        hunter = random.randint(20, 30)
        type_writer("A goblin appears in front of you.")
        time.sleep(1)

        goblin = {'name': 'Goblin', 'health': 30, 'attack': 5}

        # Multiplier untuk strength
        strength_multiplier = 0.5

        # Mulai mini-game bertarung
        while goblin['health'] > 0 and player_stats['health'] > 0:
            type_writer(f"{goblin['name']} health: {goblin['health']}")
            type_writer(f"Your health: {player_stats['health']}")
            type_writer(f"Your strength: {player_stats['strength']}")
            type_writer("What will you do?")
            type_writer("1. Attack")
            type_writer("2. Defend")
            choice = input("Choose an action (1/2): ")

            if choice == "1":
                # Hitung damage berdasarkan strength
                base_damage = random.randint(5, 10)
                damage = base_damage + int(player_stats['strength'] * strength_multiplier)
                goblin['health'] -= damage
                type_writer(f"You dealt {damage} damage to {goblin['name']}!")
            
            elif choice == "2":
             # Pertahanan
                defense = random.randint(2, 5)
                reduced_damage = max(goblin['attack'] - defense, 0)
                player_stats['health'] -= reduced_damage
                type_writer(f"You blocked the attack, reducing damage by {defense}.")
            else:
                type_writer("Invalid choice! Try again.")

            # Dummy menyerang
            if goblin['health'] > 0:
                player_stats['health'] -= goblin['attack']
                type_writer(f"{goblin['name']} attacks! You lost {goblin['attack']} health.")

            # Cek jika pemain kalah
            if player_stats['health'] <= 0:
                type_writer("You have been defeated!.")
                hospital()

        # Jika dummy kalah
        if goblin['health'] <= 0:
            type_writer(f"You defeated the {goblin['name']}! Well done, soldier!")
            player_stats['level'] += 1
            type_writer(f"Your level increased to {player_stats['level']}!")
            recover_health()
            cashout(hunter)
            town()

    def hospital():
        type_writer("doctor plague:ahh litle cut and make stitches there and...")
        time.sleep(2)
        type_writer("doctor plague:done")
        recover_health()
        type_writer("doctor plague:you can go back to the town")
        time.sleep(1)
        type_writer(f"{name}: thankyou doc")
        town()

    def dragon_fight():
        global killdragon
        type_writer("You hear a thunderous roar as a massive dragon descends before you!")
        time.sleep(2)

        # Dragon Stats
        dragon = {
            'name': 'Fire Dragon',
            'health': 10000,
            'attack': 25,
            'burn_chance': 0.3  # 30% chance to inflict burn
        }

        # Burn effect state
        burn_effect = 0

        while dragon['health'] > 0 and player_stats['health'] > 0:
            type_writer(f"Dragon Health: {dragon['health']}")
            type_writer(f"Your Health: {player_stats['health']}")
            type_writer("1. Attack")
            type_writer("2. Defend")
            type_writer("3. Use Item")

            choice = input("Choose your action (1/2/3): ").strip()

            # Player's turn
            if choice == "1":
                # Regular Attack
                damage = player_stats['strength'] + random.randint(10, 20)
                dragon['health'] -= damage
                type_writer(f"You strike the dragon for {damage} damage!")

            elif choice == "2":
                # Defend
                type_writer("You brace yourself, reducing incoming damage by half.")
                player_stats['stamina'] -= 5

            elif choice == "3":
            # Use Item
                if player_stats['inventory']:
                    item = input("Enter the name of the item to use: ").strip()
                    if item in player_stats['inventory']:
                        use_item(item)
                    else:
                        type_writer("You don't have that item!")
                else:
                    type_writer("Your inventory is empty!")
            else:
                type_writer("Invalid choice. Try again.")
                continue

            # Dragon's turn
            if dragon['health'] > 0:
                if choice == "2":
                    damage = dragon['attack'] // 2
                else:
                    damage = dragon['attack']

                player_stats['health'] -= damage
                type_writer(f"The dragon breathes fire at you, dealing {damage} damage!")

                # Burn effect
                if random.random() < dragon['burn_chance']:
                    burn_effect = 3  # Burn lasts for 3 turns
                    type_writer("You are burned by the dragon's flames! You will take 5 damage each turn.")

            # Apply burn damage
            if burn_effect > 0:
                player_stats['health'] -= 5
                type_writer("The burn sears your flesh, dealing 5 damage!")
                burn_effect -= 1

        # End of battle
        if player_stats['health'] > 0:
            type_writer("Victory! You have slain the Fire Dragon!")
            reward_gold = random.randint(1000, 2000)
            player_stats['gold'] += reward_gold
            type_writer(f"You receive {reward_gold} gold as loot!")
            add_to_inventory("Dragon Scale")
            player_stats['level'] += 10
            type_writer(f"Your level has increased to {player_stats['level']}!")
            killdragon = True
            town()
        else:
            type_writer("You have been defeated by the Fire Dragon...")
            hospital()

    def continue2():
        locals 
        type_writer(f"raider:hey {name} i have a mission for you to save the prince on Gloomspire")
        time.sleep(2)
        type_writer("you cant deny this operation beacuse this command is from the mighty king")
        time.sleep(2)
        type_writer("here take this armor")


            
            






        









        

        

        




 



    
    










