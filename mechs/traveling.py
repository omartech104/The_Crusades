from mechs import cathedral_boss
from .puzzles import riddle
from rich.console import Console
# --- Maps ---

symbols = {
    "empty": " ",
    "Road": "▪",
    "Crossroad": "+",

    "Prague": "G",      # G from "Gothic" (or just unique letter)
    "Venice": "V",      # V from Venice
    "Tours": "U" ,
    
    # London area
    "London": "L",
    "Castle": "K",     # Keep 'K' for Castle
    "Docks": "D",
    "Gatehouse": "H",  # H = House, avoids clash
    
    # Paris area
    "Paris": "P",
    "Louvre": "V",     # V from LouVre
    "Cathedral": "C",
    "Tavern": "T",
    "Inn": "I",
    
    # Cairo area
    "Cairo": "R",      # R from CaiRo
    "Mosque": "M",
    "Pyramids": "Y",   # Y from pYramids
    "Citadel": "Z",    # Z = citadel stronghold
    "Oasis": "O",
    "Caravanserai": "N", # N = iNn/caravaN, avoids G
    
    # Common locations
    "Armory": "A",
    "Market": "S",     # ⚠ clash with Mosque, so change:
    "Market": "E",     # E = ExchangE
    "Bazaar": "B",
    "Tower": "W",      # W from toWer
    "Bridge": "∩",      # ⚠ clash with Cairo, so change:
}

# Tours landmarks
symbols.update({
    "Clock Tower Of Tours": "T",
    "Pont Wilson": "X",
    "Chateau De Tours": "C",
    "St.Gatien Cathedral": "G",
    "Loire Gate": "L",
    "Pilgrims Inn": "I"
})

# Prague landmarks
symbols.update({
    "Old Town Hall": "H",
    "Charles Bridge": "B",
    "Hradčany Castle": "K",
    "St.Vitus Cathedral": "V",
    "Powder Gate": "P",
    "GoldenLane Inn": "I"
})

# Venice landmarks
symbols.update({
    "Arsenale": "A",
    "Rialto Bridge": "R",
    "Doge Palace": "D",
    "St.Marks Basilica": "S",
    "Porta Da Mare": "M",
    "Sailors Inn": "I"
})

# London Map (7x7)
london_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Armory", "Tower", "Road", "Road", "Road", "Bridge"],
    ["Road", "Road", "Crossroad", "London", "Crossroad", "Road", "Road"],
    ["Road", "Castle", "Road", "Crossroad", "Road", "Market", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Docks", "Road", "Road", "Road", "Gatehouse", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

# Paris Map (7x7)
paris_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Armory", "Louvre", "Road", "Road", "Road", "Tavern"],
    ["Road", "Road", "Crossroad", "Paris", "Crossroad", "Road", "Road"],
    ["Road", "Cathedral", "Road", "Crossroad", "Road", "Market", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Gatehouse", "Road", "Road", "Road", "Inn", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

# Cairo Map (7x7)
cairo_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Bazaar", "Road", "Road", "Road", "Armory", "Mosque"],
    ["Road", "Road", "Crossroad", "Cairo", "Crossroad", "Road", "Road"],
    ["Road", "Pyramids", "Road", "Crossroad", "Road", "Citadel", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Oasis", "Road", "Road", "Road", "Caravanserai", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

prague_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Old Town Hall", "Road", "Road", "Road", "Market", "Charles Bridge"],
    ["Road", "Road", "Crossroad", "Prague", "Crossroad", "Road", "Road"],
    ["Road", "Hradčany Castle", "Road", "Crossroad", "Road", "St.Vitus Cathedral", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Powder Gate", "Road", "Road", "Road", "GoldenLane Inn", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

venice_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Arsenale", "Road", "Road", "Road", "Market", "Rialto Bridge"],
    ["Road", "Road", "Crossroad", "Venice", "Crossroad", "Road", "Road"],
    ["Road", "Doge Palace", "Road", "Crossroad", "Road", "St.Marks Basilica", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Porta Da Mare", "Road", "Road", "Road", "Sailors Inn", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

tours_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Clock Tower Of Tours", "Road", "Road", "Road", "Market", "Pont Wilson"],
    ["Road", "Road", "Crossroad", "Tours", "Crossroad", "Road", "Road"],
    ["Road", "Chateau De Tours", "Road", "Crossroad", "Road", "St.Gatien Cathedral", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Loire Gate", "Road", "Road", "Road", "Pilgrims Inn", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

london_landmarks = [
    {"name": "Tower", "coords": (1, 2)},
    {"name": "Bridge", "coords": (1, 6)},
    {"name": "London", "coords": (2, 3)},
    {"name": "Castle", "coords": (3, 1)},
    {"name": "Docks", "coords": (5, 1)},
    {"name": "Gatehouse", "coords": (5, 5)}
]

# Paris Landmarks
paris_landmarks = [
    {"name": "Louvre", "coords": (1, 2)},
    {"name": "Tavern", "coords": (1, 6)},
    {"name": "Paris", "coords": (2, 3)},
    {"name": "Cathedral", "coords": (3, 1)},
    {"name": "Gatehouse", "coords": (5, 1)},
    {"name": "Inn", "coords": (5, 5)}
]

# Cairo Landmarks
cairo_landmarks = [
    {"name": "Mosque", "coords": (1, 6)},
    {"name": "Cairo", "coords": (2, 3)},
    {"name": "Pyramids", "coords": (3, 1)},
    {"name": "Citadel", "coords": (3, 5)},
    {"name": "Oasis", "coords": (5, 1)},
    {"name": "Caravanserai", "coords": (5, 5)}
]

prague_landmarks = [
    {"name": "Old Town Hall", "coords": (1, 1)},
    {"name": "Charles Bridge", "coords": (1, 6)},
    {"name": "Prague", "coords": (2, 3)},
    {"name": "Hradčany Castle", "coords": (3, 1)},
    {"name": "St.Vitus Cathedral", "coords": (3, 5)},
    {"name": "Powder Gate", "coords": (5, 1)},
    {"name": "GoldenLane Inn", "coords": (5, 5)}
]


venice_landmarks = [
    {"name": "Arsenale", "coords": (1, 1)},
    {"name": "Rialto Bridge", "coords": (1, 6)},
    {"name": "Venice", "coords": (2, 3)},
    {"name": "Doge Palace", "coords": (3, 1)},
    {"name": "St.Marks Basilica", "coords": (3, 5)},
    {"name": "Porta Da Mare", "coords": (5, 1)},
    {"name": "Sailors Inn", "coords": (5, 5)}
]


tours_landmarks = [
    {"name": "Clock Tower Of Tours", "coords": (1, 1)},
    {"name": "Pont Wilson", "coords": (1, 6)},
    {"name": "Tours", "coords": (2, 3)},
    {"name": "Chateau De Tours", "coords": (3, 1)},
    {"name": "St.Gatien Cathedral", "coords": (3, 5)},
    {"name": "Loire Gate", "coords": (5, 1)},
    {"name": "Pilgrims Inn", "coords": (5, 5)}
]



# Starting location
current_city = "London"
player_pos = (2, 3)
cities = ["London", "Paris", "Cairo", "Prague", "Venice", "Tours"]
current_map = london_map


import time
from rich.text import Text

def render_map(blink_on=True):
    console.clear()
    console.rule(f"[bold cyan]{current_city} Map[/bold cyan]")

    pr, pc = player_pos

    for r, row in enumerate(current_map):
        line = Text()
        for c, tile in enumerate(row):
            symbol = symbols.get(tile, "?")

            if (r, c) == (pr, pc):
                # PLAYER BLINK
                if blink_on:
                    line.append(f" {symbol} ", style="bold black on yellow")
                else:
                    line.append(f" {symbol} ", style="bold red")
            else:
                line.append(f" {symbol} ", style="white")
        console.print(line)

def show_map_with_blink(duration=3, speed=0.4):
    blink = True
    start = time.time()

    while time.time() - start < duration:
        render_map(blink_on=blink)
        blink = not blink
        time.sleep(speed)


def get_location_name():
    row, col = player_pos
    tile = current_map[row][col]

    # Generic road and crossroad descriptions
    if tile == "Road":
        return {
            "London": "a cobblestone road, damp from the English mist",
            "Paris": "a narrow stone road, echoing with footsteps",
            "Cairo": "a sandy path, warm under the desert sun",
            "Prague": "a cobbled street lined with gothic buildings",
            "Venice": "a narrow alley between canal-side buildings",
            "Tours": "a stone-paved street bustling with townsfolk"
        }.get(current_city, "a simple path")
    
    if tile == "Crossroad":
        return "a busy crossroad where paths meet"

    # Landmark descriptions
    landmark_descriptions = {
        # London
        "Tower": "The Tower of London, grim and foreboding",
        "Bridge": "A wooden bridge spanning the river",
        "Castle": "The royal castle, strong and majestic",
        "Market": "The bustling London market, full of traders",
        "Docks": "The docks by the Thames, busy with ships",
        "Gatehouse": "The gatehouse guarding the city walls",

        # Paris
        "Louvre": "The Louvre, a palace of kings and art",
        "Tavern": "A lively tavern, filled with laughter and wine",
        "Cathedral": "The great cathedral, its bells tolling",
        "Inn": "A modest inn for weary travelers",

        # Cairo
        "Bazaar": "The Cairo bazaar, alive with merchants and scents",
        "Mosque": "A grand mosque, echoing with prayers",
        "Pyramids": "The great pyramids, ancient and timeless",
        "Citadel": "The Citadel, standing proud over Cairo",
        "Oasis": "A small oasis, refreshing and green",
        "Caravanserai": "A caravanserai where travelers rest",

        # Prague
        "Old Town Hall": "The Old Town Hall, its gothic spire rising above the square",
        "Charles Bridge": "A historic stone bridge over the Vltava River, adorned with statues",
        "Hradčany Castle": "Hradčany Castle, seat of royalty with towering walls",
        "St.Vitus Cathedral": "St. Vitus Cathedral, majestic with intricate gothic windows",
        "Powder Gate": "The Powder Gate, an ancient city gate guarding the entrance",
        "GoldenLane Inn": "A small inn with colorful houses, once home to castle craftsmen",

        # Venice
        "Arsenale": "The Venetian Arsenale, a massive shipyard where war galleys are built",
        "Rialto Bridge": "The Rialto Bridge, crossing the Grand Canal and crowded with merchants",
        "Doge Palace": "The Doge's Palace, adorned with gilded halls and ornate windows",
        "St.Marks Basilica": "St. Mark's Basilica, with golden mosaics and soaring domes",
        "Porta Da Mare": "The Sea Gate, guarding Venice from intruders by the lagoon",
        "Sailors Inn": "A quaint inn favored by sailors docking in the canals",

        # Tours
        "Clock Tower Of Tours": "A medieval clock tower, visible from across the town",
        "Pont Wilson": "An old stone bridge crossing the Loire River",
        "Chateau De Tours": "The Chateau de Tours, an imposing castle overlooking the river",
        "St.Gatien Cathedral": "The Gothic St. Gatien Cathedral, its stained glass glowing in the sun",
        "Loire Gate": "The Loire Gate, once guarding the approach from the river",
        "Pilgrims Inn": "A welcoming inn for pilgrims traveling the Loire valley",
    }

    if tile in landmark_descriptions:
        return landmark_descriptions[tile]

    # City centers
    city_centers = {
        "London": "the heart of London, filled with life and activity",
        "Paris": "the heart of Paris, bustling with merchants and townsfolk",
        "Cairo": "the center of Cairo, alive with desert trade",
        "Prague": "the heart of Prague, lively with merchants and townsfolk",
        "Venice": "the center of Venice, canals winding between tall palaces",
        "Tours": "the bustling town center of Tours, alive with trade and people"
    }

    return city_centers.get(tile, tile)

def get_current_tile():
    row, col = player_pos
    return current_map[row][col]


def get_tile_description():
    row, col = player_pos
    tile = current_map[row][col]

    # Special events
    if tile == "Cathedral" and current_city == "Paris" and not cathedral_boss.defeated:
        print("You step into the grand Paris Cathedral...")
        cathedral_boss.fight_cathedral_boss()
        return "The Cathedral stands tall, silent after the battle."

    if tile == "Citadel" and current_city == "Cairo":
        if not riddle.solved:
            print("You arrive at the mighty Cairo Citadel...")
            riddle.play_riddle()
            return "The Citadel tests your wisdom with a riddle."
        else:
            return "The Citadel stands silent, its riddle already solved."

    # Generic descriptions
    descriptions = {
        "Market": {
            "London": "You are now in London Market, filled with goods and merchants.",
            "Paris": "You are now in Parisian market stalls with spices and fabrics.",
            "Cairo": "You are now in Cairo Bazaar, bustling with traders and colors.",
            "Prague": "The Prague market, bustling with Bohemian goods and traders.",
            "Venice": "Venetian market stalls, filled with exotic spices and silk.",
            "Tours": "The Tours market, with local cheeses, wines, and crafts."
        },
        "Castle": {
            "London": "You are in the grand London Castle.",
            "Paris": "You are in the fortified Paris Castle.",
            "Cairo": "You are in the historic Cairo Citadel.",
            "Prague": "You are in Hradčany Castle, seat of royalty.",
            "Venice": "You are in the Doge's Palace, majestic and ornate.",
            "Tours": "You are in the Chateau de Tours, overlooking the Loire River."
        },
        "Tower": {
            "London": "You stand near the tall Tower of London.",
            "Paris": "Near the iconic Paris Tower.",
            "Cairo": "Near the ancient Cairo Tower.",
            "Prague": "The Old Town Hall clock tower dominates the square.",
            "Tours": "You stand by the Clock Tower Of Tours."
        },
        "Bridge": {
            "London": "You are on London Bridge.",
            "Paris": "You are on the Seine bridge.",
            "Cairo": "Crossing the Nile bridge.",
            "Prague": "Walking over Charles Bridge, statues lining the sides.",
            "Venice": "Crossing the Rialto Bridge over the Grand Canal.",
            "Tours": "Walking across Pont Wilson, connecting town districts."
        },
        "Inn": {
            "Paris": "A modest inn for weary travelers.",
            "Prague": "GoldenLane Inn, quaint and colorful.",
            "Venice": "Sailors Inn, cozy for travelers from the lagoon.",
            "Tours": "Pilgrims Inn, welcoming all travelers."
        },
        "Cathedral": {
            "Paris": "You are inside the Paris Cathedral.",
            "Prague": "St. Vitus Cathedral, soaring gothic spires and stained glass.",
            "Venice": "St. Mark's Basilica, golden mosaics shimmering.",
            "Tours": "St. Gatien Cathedral, illuminated by colorful stained glass."
        }
    }

    return descriptions.get(tile, {}).get(current_city, f"You are at {tile} in {current_city}.")

def move(direction: str):
    global player_pos
    row, col = player_pos

    if direction == "N":
        new_pos = (row - 1, col)
    elif direction == "S":
        new_pos = (row + 1, col)
    elif direction == "W":
        new_pos = (row, col - 1)
    elif direction == "E":
        new_pos = (row, col + 1)
    else:
        return "Invalid direction."

    # Check boundaries
    max_row = len(current_map) - 1
    max_col = len(current_map[0]) - 1
    if 0 <= new_pos[0] <= max_row and 0 <= new_pos[1] <= max_col:
        player_pos = new_pos
        return f"You moved {direction} to {get_location_name()}."
    else:
        return "You cannot go that way."


from rich.console import Console
from rich.text import Text

console = Console()

def fast_travel():
    global player_pos
    console.print("[bold cyan]Travel to any landmark[/bold cyan]")

    if current_city == "London":
        for i, landmark in enumerate(london_landmarks):
            console.print(f"[yellow]{i}[/yellow] - [green]{landmark['name']}[/green]")
        landmark_num = console.input("[bold magenta]Type the number of the Landmark: [/bold magenta]")
        for i, landmark in enumerate(london_landmarks):
            if i == int(landmark_num):
                player_pos = landmark["coords"]
                console.print(f"[bold green]You moved to [cyan]{get_location_name()}[/cyan].[/bold green]")

    elif current_city == "Paris":
        for i, landmark in enumerate(paris_landmarks):
            console.print(f"[yellow]{i}[/yellow] - [green]{landmark['name']}[/green]")
        landmark_num = console.input("[bold magenta]Type the number of the Landmark: [/bold magenta]")
        for i, landmark in enumerate(paris_landmarks):
            if i == int(landmark_num):
                player_pos = landmark["coords"]
                console.print(f"[bold green]You moved to [cyan]{get_location_name()}[/cyan].[/bold green]")

    elif current_city == "Cairo":
        for i, landmark in enumerate(cairo_landmarks):
            console.print(f"[yellow]{i}[/yellow] - [green]{landmark['name']}[/green]")
        landmark_num = console.input("[bold magenta]Type the number of the Landmark: [/bold magenta]")
        for i, landmark in enumerate(cairo_landmarks):
            if i == int(landmark_num):
                player_pos = landmark["coords"]
                console.print(f"[bold green]You moved to [cyan]{get_location_name()}[/cyan].[/bold green]")

    elif current_city == "Prague":
        for i, landmark in enumerate(prague_landmarks):
            console.print(f"[yellow]{i}[/yellow] - [green]{landmark['name']}[/green]")
        landmark_num = console.input("[bold magenta]Type the number of the Landmark: [/bold magenta]")
        for i, landmark in enumerate(prague_landmarks):
            if i == int(landmark_num):
                player_pos = landmark["coords"]
                console.print(f"[bold green]You moved to [cyan]{get_location_name()}[/cyan].[/bold green]")

    elif current_city == "Venice":
        for i, landmark in enumerate(venice_landmarks):
            console.print(f"[yellow]{i}[/yellow] - [green]{landmark['name']}[/green]")
        landmark_num = console.input("[bold magenta]Type the number of the Landmark: [/bold magenta]")
        for i, landmark in enumerate(venice_landmarks):
            if i == int(landmark_num):
                player_pos = landmark["coords"]
                console.print(f"[bold green]You moved to [cyan]{get_location_name()}[/cyan].[/bold green]")

    elif current_city == "Tours":
        for i, landmark in enumerate(tours_landmarks):
            console.print(f"[yellow]{i}[/yellow] - [green]{landmark['name']}[/green]")
        landmark_num = console.input("[bold magenta]Type the number of the Landmark: [/bold magenta]")
        for i, landmark in enumerate(tours_landmarks):
            if i == int(landmark_num):
                player_pos = landmark["coords"]
                console.print(f"[bold green]You moved to [cyan]{get_location_name()}[/cyan].[/bold green]")

