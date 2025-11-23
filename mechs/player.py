from rich.console import Console

console = Console()

player_hp = 1500
player_dp = 50
player_df = 0

def wear_armor(item):
    global player_hp, player_df
    import mechs.shopping

    # Check if player has the armor in inventory
    if item not in mechs.shopping.inventory:
        console.print(f"[bold red]You don't have {item} in your inventory![/bold red]")
        return

    # Armor dictionary: name -> DF
    armor_df = {
        "Padded Jack": 12,
        "Aketon": 16,
        "Studded Leather Armor": 20,
        "Brigandine": 48,
        "Heater Shield": 14
    }

    if item in armor_df:
        # Apply DF
        player_df = armor_df[item]
        console.print(f"[bold green]You equipped {item}![/bold green] [cyan]Defense set to {player_df}[/cyan]")
    else:
        console.print(f"[bold red]{item} cannot be worn as armor![/bold red]")

