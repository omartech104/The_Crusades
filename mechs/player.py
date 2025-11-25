from rich.console import Console

console = Console()

player_hp = 1500
player_dp = 50
player_df = 0
player_ag = 0

def wear_clothes_and_armor(item):
    """
    Equip armor or weapon safely.
    - Armor (Clothing or Armory with 'defense') updates player_df
    - Weapon (Armory with 'damage') updates player_dp
    """
    from mechs import shopping, traveling
    global player_df, player_dp

    city_shop = shopping.shops[traveling.current_city]

    clothes = city_shop.get("Clothing", {})
    armory = city_shop.get("Armory", {})

    if item in clothes:
        if "defense" in clothes[item]:
            player_df = clothes[item]["defense"]
            console.print(f"[bold green]You equipped {item} as armor![/bold green] [cyan]DF = {player_df}[/cyan]")
        else:
            console.print(f"[bold red]{item} cannot be equipped as armor![/bold red]")
        return

    if item in armory:
        if "defense" in armory[item]:
            player_df = armory[item]["defense"]
            console.print(f"[bold green]You equipped {item} as armor![/bold green] [cyan]DF = {player_df}[/cyan]")
        elif "damage" in armory[item]:
            player_dp = armory[item]["damage"]
            console.print(f"[yellow]You equipped {item} as a weapon! Damage = {player_dp}[/yellow]")
        else:
            console.print(f"[bold red]{item} cannot be equipped![/bold red]")
        return

    console.print(f"[bold red]{item} cannot be equipped as armor or weapon![/bold red]")

