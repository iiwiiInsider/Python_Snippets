game_level = 3
enemies = ["Skeletons", "Zombies", "Witches", "Vampires", "Werewolves"]

def create_enemy():
    new_enemy = ""
    if game_level < 10:
        new_enemy = enemies[0]

    print(new_enemy)