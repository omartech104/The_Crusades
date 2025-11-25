from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from mechs import traveling

console = Console()

# --- Player Variables ---
player_gold = 500
inventory = []


# --- SHOPS DATABASE ---
shops = {
    "London": {
        "Market": {
            "A loaf of bread": {"price": 5, "desc": "Baked in a simple oven.", "stock": 5},
            "Astrolabe": {"price": 400, "desc": "An instrument of navigation.", "stock": 5},
            "Gemstone": {"price": 800, "desc": "A rare gemstone.", "stock": 1},
            "Health Potion": {"price": 450, "desc": "Restores health instantly.", "stock": 6},
            "Map Of London": {"price": 10, "desc": "The map of London.", "stock": 2}
        },
        "Armory": {
            "Longsword": {"price": 80, "desc": "Strong blade favored by knights.", "damage": 300, "stock": 2},
            "Battle Axe": {"price": 100, "desc": "Heavy axe for brutal combat.", "damage": 350, "stock": 2},
            "Long Bow": {"price": 60, "desc": "A powerful longbow favored by English archers", "damage": 200, "stock": 3},
            "Warhammer": {"price": 120, "desc": "Crush your foes with force.", "damage": 400, "stock": 1},
            "Dagger": {"price": 30, "desc": "Quick, light, and deadly.", "damage": 150, "stock": 4},
        }
    },

    "Paris": {
        "Market": {
            "Book": {"price": 30, "desc": "A tome of medieval knowledge.", "stock": 3},
            "Wine": {"price": 20, "desc": "A fine Parisian vintage.", "stock": 5},
            "Illuminated Manuscript": {"price": 60, "desc": "A missing part of something unknown.", "stock": 1},
            "Map Of Paris": {"price": 8, "desc": "The Map of Paris.", "stock": 3}
        },
        "Armory": {
            "Rapier": {"price": 90, "desc": "Elegant fencing blade.", "damage": 250, "stock": 2},
            "Halberd": {"price": 110, "desc": "A polearm used by Parisian guards.", "damage": 370, "stock": 2},
            "Crossbow": {"price": 100, "desc": "Powerful but slow to reload.", "damage": 320, "stock": 2},
            "Mace": {"price": 70, "desc": "Crushing weapon popular among clergy knights.", "damage": 280, "stock": 3},
            "Dirk": {"price": 40, "desc": "Slim blade used by assassins.", "damage": 180, "stock": 4},
        }
    },

    "Cairo": {
        "Bazaar": {
            "Spices": {"price": 25, "desc": "Exotic spices from the East.", "stock": 5},
            "Halum Cheese": {"price": 50, "desc": "A half pound of local cheese.", "stock": 3},
            "A copy of matn al-ajrumiyyah": {"price": 100, "desc": "Rare Arabic grammar manuscript.", "stock": 1},
            "Map Of Cairo": {"price": 8, "desc": "The Map of Cairo.", "stock": 3}
        },
        "Armory": {
            "Shamshir": {"price": 85, "desc": "Curved sword, swift and sharp.", "damage": 270, "stock": 2},
            "Spear": {"price": 60, "desc": "Simple but effective.", "damage": 240, "stock": 3},
            "Composite Bow": {"price": 95, "desc": "Strong bow with great range.", "damage": 280, "stock": 2},
            "Khopesh": {"price": 120, "desc": "Ancient Egyptian sickle-sword.", "damage": 360, "stock": 1},
            "Jambiya": {"price": 35, "desc": "Curved dagger from Arabia.", "damage": 160, "stock": 4}
        }
    },

    "Prague": {
        "Market": {
            "Medieval Bread": {"price": 5, "desc": "Freshly baked bread from a Bohemian bakery.", "stock": 5},
            "Dark Ale": {"price": 15, "desc": "Locally brewed dark ale, popular with townsfolk.", "stock": 8},
            "Map of Prague": {"price": 10, "desc": "Detailed map of the city streets and landmarks.", "stock": 3},
            "Bohemian Amber Necklace": {"price": 100, "desc": "Necklace made from rare Bohemian amber.", "stock": 2}
        },
        "Armory": {
            "Zweihänder": {"price": 400, "desc": "Forged by local blacksmiths, sharp and reliable.", "damage": 480, "stock": 2},
            "War Axe": {"price": 100, "desc": "Heavy axe favored by knights of Bohemia.", "damage": 350, "stock": 2},
            "Throwing Knives": {"price": 90, "desc": "Set of sharp knives for precise attacks.", "damage": 100, "stock": 3},
            "Morning Star": {"price": 300, "desc": "A spiky Mace designed for close combat.", "damage": 390, "stock": 2},
        }
    },

    "Venice": {
        "Market": {
            "Venetian Glass Beads": {"price": 25, "desc": "Finely crafted glass beads from Murano.", "stock": 5},
            "Venetian Wine": {"price": 20, "desc": "Local vintage, enjoyed by merchants.", "stock": 6},
            "Map of Venice": {"price": 12, "desc": "Map detailing canals and major landmarks.", "stock": 3},
            "Silk Cloth": {"price": 60, "desc": "Imported silk from the East, very luxurious.", "stock": 2}
        },
        "Armory": {
            "Stiletto": {"price": 90, "desc": "Elegant Venetian dagger, perfect for duels.", "damage": 250, "stock": 2},
            "Pike": {"price": 110, "desc": "Used by the city guards to protect Venice.", "damage": 370, "stock": 2},
            "Short Bow": {"price": 60, "desc": "Compact bow suitable for urban defense.", "damage": 200, "stock": 3},
            "Cinquedea": {"price": 35, "desc": "Triangular dagger popular in Renaissance Italy.", "damage": 160, "stock": 4},
        }
    },

    "Tours": {
        "Market": {
            "Goat Cheese": {"price": 15, "desc": "Local cheese from the Loire Valley.", "stock": 5},
            "Loire Wine": {"price": 20, "desc": "Fine wine from surrounding vineyards.", "stock": 6},
            "Map of Tours": {"price": 8, "desc": "Map highlighting the town and river crossings.", "stock": 3},
            "Book of Prayers": {"price": 50, "desc": "A local religious text for pilgrims.", "stock": 2}
        },
        "Armory": {
            "Arming Sword": {"price": 80, "desc": "Sturdy soldier’s blade for defense.", "damage": 200, "stock": 2},
            "Poleaxe": {"price": 100, "desc": "Versatile axe used by knights.", "damage": 250, "stock": 2},
            "Throwing Spear": {"price": 90, "desc": "Balanced spear for distance attacks.", "damage": 180, "stock": 3},
            "Warhammer": {"price": 120, "desc": "Heavy weapon designed to crush armor.", "damage": 400, "stock": 1},
            "Heater Shield": {"price": 100, "desc": "A simple metal shield, preferd by infantry.", "defense": 14, "stock": 4}
         }
    }
}

shops["London"]["Clothing"] = {
    "Woolen Tunic": {"price": 25, "desc": "Everyday English tunic worn by peasants.", "stock": 6},
    "Gambeson Coat": {"price": 90, "desc": "Thick padded coat worn under armor.", "defense": 17, "stock": 3},
    "English Hood": {"price": 10, "desc": "The classic medieval hood.", "stock": 8},
    "Merchant's Coat": {"price": 60, "desc": "A fine coat worn by London merchants.", "stock": 2},
    # Armor moved from Armory
    "Padded Jack": {"price": 120, "desc": "Surprisingly good protection against cuts and some arrows.", "defense": 12, "stock": 2}
}

shops["Paris"]["Clothing"] = {
    "Pourpoint": {"price": 70, "desc": "A tight quilted jacket fashionable in Paris.", "stock": 3},
    "French Cloak": {"price": 40, "desc": "A stylish cloak worn by nobles.", "agility": 16,"stock": 2},
    "Woolen Hose": {"price": 20, "desc": "Common legwear in medieval France.", "stock": 6},
    "Silk Doublet": {"price": 120, "desc": "Luxury item worn by wealthy Parisians.", "stock": 1},
    # Armor moved from Armory
    "Aketon": {"price": 130, "desc": "Provides good protection for its material, preferred by archers.", "defense": 16, "stock": 2}
}

shops["Prague"]["Clothing"] = {
    "Bohemian Tunic": {"price": 25, "desc": "Simple tunic worn by common Prague citizens.", "stock": 6},
    "Fur-Lined Cloak": {"price": 80, "desc": "Warm winter cloak typical in Bohemia.", "stock": 3},
    "Linen Undershirt": {"price": 10, "desc": "Basic medieval garment.", "stock": 10},
    "Merchant Robe": {"price": 60, "desc": "Decorative robe worn by traders.", "stock": 2},
    # Armor moved from Armory
    "Studded Leather Armor": {"price": 230, "desc": "Armor used by Landsknechts.", "defense": 20, "stock": 3}
}

shops["Venice"]["Clothing"] = {
    "Venetian Doublet": {"price": 90, "desc": "Typical Renaissance Italian doublet.", "stock": 3},
    "Silk Hose": {"price": 40, "desc": "Fine hose worn by wealthy Venetians.", "stock": 4},
    "Merchant's Robe": {"price": 70, "desc": "Robes worn by Venetian traders.", "stock": 2},
    "Travel Cloak": {"price": 30, "desc": "Light cloak for navigating Venice’s canals.", "stock": 5},
    # Armor moved from Armory
    "Brigandine": {"price": 500, "desc": "Flexible armor with hidden metal plates.", "defense": 48, "stock": 3}
}

shops["Cairo"]["Clothing"] = {
    # Clothes
    "Galabiyya": {"price": 20, "desc": "Traditional Egyptian long robe worn by all classes.", "stock": 6},
    "Turban": {"price": 15, "desc": "Light headwrap protecting from the sun.", "stock": 8},
    "Mamluk Coat": {"price": 90, "desc": "Decorated coat worn by Mamluk soldiers.", "stock": 2},
    "Silk Kaftan": {"price": 150, "desc": "Luxurious court garment.", "stock": 1},
    # Armor (none historically common besides padded coats, already included)
}

city_market_pos = {
    "London": (3, 5),
    "Paris": (3, 5),
    "Cairo": (1, 1),
    "Prague": (1, 5),
    "Venice": (1, 5),
    "Tours": (1, 5),
}

# --- FUNCTIONS ---

def show_city_shops(city):
    """Shows all shops in the city and allows player to enter them"""
    if city not in shops:
        console.print(f"[bold red]No shops available in {city}[/bold red]")
        return

    while True:
        console.clear()
        console.print(Panel.fit(f"[bold cyan]{city} Shops[/bold cyan]", border_style="bright_blue"))
        city_shops = shops[city]
        for shop_name in city_shops:
            console.print(f"[bold yellow]- {shop_name}[/bold yellow]")
        console.print("[red]B[/red] - Go back to the Market")

        selected = Prompt.ask("[green]Enter shop name[/green]").strip()
        if selected.lower() == "b":
            set_player_to_market(city)
            break
        elif selected in city_shops:
            open_shop(city, selected)
        else:
            console.print("[red]Invalid shop name![/red]")

def open_shop(city, shop_name):
    global player_gold
    shop = shops[city][shop_name]
    console.clear()
    console.print(Panel.fit(f"[bold cyan]{shop_name} - {city}[/bold cyan]", border_style="yellow"))

    table = Table(title=f"{shop_name} Inventory", header_style="bold blue")
    table.add_column("Item", style="bold green")
    table.add_column("Price", justify="right")
    table.add_column("Stock", justify="center")
    table.add_column("Description", justify="left")

    for item, data in shop.items():
        table.add_row(item, f"{data['price']} gold", str(data['stock']), data['desc'])
    console.print(table)

    console.print(f"[bold magenta]Your gold:[/bold magenta] {player_gold}")
    buy_item = Prompt.ask("[green]Enter item to buy[/green] or [red]B to go back[/red]")
    if buy_item.lower() == "b":
        return
    if buy_item in shop:
        item = shop[buy_item]
        if player_gold >= item["price"] and item["stock"] > 0:
            player_gold -= item["price"]
            item["stock"] -= 1
            inventory.append(buy_item)
            console.print(f"[bold green]You bought {buy_item}![/bold green]")
        else:
            console.print("[red]You can’t afford that or it’s out of stock![/red]")
    else:
        console.print("[red]Invalid item name![/red]")

    input("> Press Enter...")


def show_inventory():
    console.print(Panel.fit("[bold cyan]Your Inventory[/bold cyan]", border_style="bright_magenta"))
    if not inventory:
        console.print("[italic yellow]Your inventory is empty.[/italic yellow]")
    else:
        for i, item in enumerate(inventory, 1):
            console.print(f"[bold green]{i}.[/bold green] {item}")
    console.print(f"\n[bold magenta]Gold:[/bold magenta] {player_gold}")
    input("> Press Enter...")


def set_player_to_market(city):
    """After leaving shop, set player to market tile"""
    pos = city_market_pos.get(city, (2, 3))
    traveling.player_pos = pos
