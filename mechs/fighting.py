import random
from rich.console import Console
from mechs import traveling, shopping, inventory, badges,player

console = Console()

# player stats

equipped_weapon = None

# enemy spawn points
enemy_spawns = {
    "London": {
        "Crossroad": ["Bandit", "Thief"],
        "Docks": ["Thief", "Bandit"],
        "Castle": ["Templar"]
    },
    "Paris": {
        "Tavern": ["Bandit"],
        "Gatehouse": ["Thief"],
        "Cathedral": ["Templar"]
    },
    "Cairo": {
        "Oasis": ["Bandit"],
        "Citadel": ["Templar"],
        "Bazaar": ["Thief"]
    },
    "Prague": {
        "Powder Gate": ["Bandit"],
        "Hradčany Castle": ["Templar"],
        "Crossroad": ["Thief"]
    },
    "Venice": {
        "Arsenale": ["Thief"],
        "Doge Palace": ["Templar"],
        "Rialto Bridge": ["Bandit"]
    }
}


# enemy class
class Enemy:
    def __init__(self, kind):
        self.kind = kind
        self.dp = random.randint(80, 150)
        self.hp = random.randint(500, 1200)

    def cutscene(self):
        console.print(f"[bold red]⚔ A {self.kind} appears at this location! ⚔[/bold red]")


# equip weapon system
def equip_weapon():
    """
    Equip a weapon from the player's inventory (stored as strings).
    Sets player_dp based on the weapon's damage from Armory.
    """
    global player_dp, equipped_weapon
    from mechs import shopping, player, badges

    inv = shopping.inventory
    shops = shopping.shops

    if not inv:
        console.print("[bold red]You have no weapons in your inventory![/bold red]")
        return

    # Build a list of weapons in inventory by checking Armory
    weapon_list = []
    weapon_data = {}
    printed = set()

    for item in inv:
        if item in printed:
            continue
        # Search for weapon damage in all Armories
        for city in shops.values():
            armory = city.get("Armory", {})
            if item in armory and "damage" in armory[item]:
                dmg = armory[item]["damage"]
                weapon_list.append(item)
                weapon_data[item] = dmg
                printed.add(item)
                console.print(f"[green]{len(weapon_list)}.[/green] {item} ([cyan]{dmg} dmg[/cyan])")
                break  # stop at first match

    if not weapon_list:
        console.print("[bold red]You have no usable weapons in your inventory.[/bold red]")
        return

    # Ask player to choose a weapon
    choice = input("\nChoose a weapon to equip: ")

    if choice.isdigit() and 1 <= int(choice) <= len(weapon_list):
        weapon = weapon_list[int(choice) - 1]
        equipped_weapon = weapon
        player_dp = weapon_data[weapon]

        # Badge bonus if unlocked
        if badges.badges[0]["unlocked"]:
            player_dp += 40
            console.print("[bold green]Badge bonus: +40 damage[/bold green]")

        console.print(f"\n[bold cyan]You equipped the {weapon}![/bold cyan] Damage set to [bold yellow]{player_dp}[/bold yellow]")

        # Start fight (optional)
        # fighting.start(player_dp=player_dp, weapon=weapon)

    else:
        console.print("[bold red]Invalid choice — you fight with your fists.[/bold red]")
        equipped_weapon = None
        player_dp = 50  # default unarmed damage

# player attacks enemy
def player_attack(enemy):
    damage = enemy.dp - (enemy.dp * (player.player_df / 100))
    enemy.hp -= damage
    console.print(f"[bold green]You hit the {enemy.kind} with {equipped_weapon or 'fists'} for {damage} damage![/bold green]")
    if enemy.hp <= 0:
        console.print(f"[bold yellow]The {enemy.kind} has been slain![/bold yellow]")
        if enemy.kind == "Bandit":
            badges.badges[0]["unlocked"] = True
        return True
    return False


def player_heal():
    #global player.player_hp
    inventory.view_inventory()
    player.player_hp = min(player.player_hp, 1500)
    console.print(f"[bold green]Your HP is now {player.player_hp}[/bold green]")


# enemy attacks player
def enemy_attack(enemy):
    #global player.player_hp
    damage = enemy.dp
    player.player_hp -= damage
    console.print(f"[red]The {enemy.kind} attacked you for [bold red]{damage}[/bold red] damage![/red] [bold white]Current HP: {player.player_hp}[/bold white]")
    if player.player_hp <= 0:
        console.print("[bold red]You were slain... Game Over.[/bold red]")
        return True
    return False

def dodge_chance(agility):
    return agility / (agility + 30)  # cap grows naturally


# combat loop
def combat(enemy):
    #global player.player_hp
    enemy.cutscene()
    equip_weapon()

    while player.player_hp > 0 and enemy.hp > 0:
        console.print(f"\n[bold blue]Your HP:[/bold blue] {player.player_hp} | [bold red]Enemy HP:[/bold red] {enemy.hp}")
        console.print("\n[bold red]1. Attack[/bold red] | [bold green]2. Heal[/bold green] | [bold yellow]3. Dodge[/bold yellow]")
        des = input("> ")

        if des == "1":
            killed = player_attack(enemy)
            if killed:
                loot = [f"{enemy.kind} Loot"]
                shopping.inventory.extend(loot)
                console.print(f"[bold magenta]You looted: {loot}[/bold magenta]")
                return enemy.kind, loot
            if random.random() < 0.8:
                if enemy_attack(enemy):
                    return None, []
        elif des == "2":
            player_heal()
        elif des == "3":
            if random.random() > dodge_chance(player.player_ag):
                console.print("[bold green]You dodged successfully![/bold green]")
            else:
                console.print("[bold red]Dodge failed![/bold red]")
                if enemy_attack(enemy):
                    return None, []
        else:
            console.print("[bold red]Invalid choice! The enemy takes the chance to strike...[/bold red]")
            if enemy_attack(enemy):
                return None, []

    return None, []


# check if enemy spawns on current tile
def check_for_enemy():
    city = traveling.current_city
    row, col = traveling.player_pos
    tile = traveling.current_map[row][col]

    if city in enemy_spawns and tile in enemy_spawns[city]:
        possible_enemies = enemy_spawns[city][tile]
        enemy_kind = random.choice(possible_enemies)
        enemy = Enemy(enemy_kind)
        return combat(enemy)
    else:
        console.print("[dim]The area is quiet. No enemies here.[/dim]")

