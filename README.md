# ⚔️ The Crusades

_A text-adventure game set in Medieval Europe_

**👨‍💻 Authors:** [@omartech104](https://github.com/omartech104) & [@challenger467](https://github.com/challenger467)  
**📦 Repository:** [The_Crusades](https://github.com/omartech104/The_Crusades)

---

## 🎮 About  
**The Crusades** is a **text-based adventure game** written in Python.  
Step into Medieval Europe — make choices, face consequences, and shape your fate in the chaos of war, politics, and survival.  
This repository hosts the **demo version** of the game.

---

## 🧩 Features  
✅ 100% Python  
✅ Interactive command-line adventure  
✅ Narrative-driven gameplay with multiple outcomes  
✅ Modular structure (see `mechs/` folder)  
✅ Easy to expand — add your own stories or mechanics  
✅ A nice UI 
---

## 🚀 Getting Started  

### 🔧 Prerequisites  
- Python 3.x installed  
- (Optional) Virtual environment  

### 💻 Installation  
```bash
git clone https://github.com/omartech104/The_Crusades.git
cd The_Crusades
pip install -r requirements.txt
python main.py
```

---

## 🕹️ How to Play  
1. Run the game with `python main.py`.  
2. Read the story carefully.  
3. Type your choice (number or keyword).  
4. Experience the results of your decisions.  
5. Replay to explore different paths!  

---

## Maps & Map Key

🌍 London Map
▪ ▪ ▪ + ▪ ▪ ▪
▪ A W ▪ ▪ ▪ X
▪ ▪ + L + ▪ ▪
▪ K ▪ + ▪ E ▪
▪ ▪ ▪ + ▪ ▪ ▪
▪ D ▪ ▪ ▪ H ▪
▪ ▪ ▪ + ▪ ▪ ▪

🌆 Paris Map
▪ ▪ ▪ + ▪ ▪ ▪
▪ A V ▪ ▪ ▪ T
▪ ▪ + P + ▪ ▪
▪ C ▪ + ▪ E ▪
▪ ▪ ▪ + ▪ ▪ ▪
▪ H ▪ ▪ ▪ I ▪
▪ ▪ ▪ + ▪ ▪ ▪

🐪 Cairo Map
▪ ▪ ▪ + ▪ ▪ ▪
▪ B ▪ ▪ ▪ A M
▪ ▪ + R + ▪ ▪
▪ Y ▪ + ▪ Z ▪
▪ ▪ ▪ + ▪ ▪ ▪
▪ O ▪ ▪ ▪ N ▪
▪ ▪ ▪ + ▪ ▪ ▪

🏰 Prague Map
▪ ▪ ▪ + ▪ ▪ ▪
▪ H ▪ ▪ ▪ E B
▪ ▪ + G + ▪ ▪
▪ K ▪ + ▪ V ▪
▪ ▪ ▪ + ▪ ▪ ▪
▪ P ▪ ▪ ▪ I ▪
▪ ▪ ▪ + ▪ ▪ ▪

🚤 Venice Map
▪ ▪ ▪ + ▪ ▪ ▪
▪ A ▪ ▪ ▪ E R
▪ ▪ + V + ▪ ▪
▪ D ▪ + ▪ S ▪
▪ ▪ ▪ + ▪ ▪ ▪
▪ M ▪ ▪ ▪ I ▪
▪ ▪ ▪ + ▪ ▪ ▪

🕯️ Tours Map
▪ ▪ ▪ + ▪ ▪ ▪
▪ T ▪ ▪ ▪ E X
▪ ▪ + U + ▪ ▪
▪ C ▪ + ▪ G ▪
▪ ▪ ▪ + ▪ ▪ ▪
▪ L ▪ ▪ ▪ I ▪
▪ ▪ ▪ + ▪ ▪ ▪

ROADS & STRUCTURES
▪   Road
+   Crossroad
X   Bridge
W   Tower
∩   (unused — old bridge symbol)

CITIES
L   London
P   Paris
R   Cairo
G   Prague
V   Venice
U   Tours

COMMON LOCATIONS
A   Armory
E   Market / Exchange
B   Bazaar
D   Docks
H   Gatehouse
K   Castle / Keep
T   Tavern
I   Inn
C   Cathedral
M   Mosque
Y   Pyramids
Z   Citadel
O   Oasis
N   Caravanserai

TOURS LANDMARKS
T   Clock Tower of Tours
X   Pont Wilson
C   Chateau de Tours
G   St. Gatien Cathedral
L   Loire Gate
I   Pilgrims Inn

PRAGUE LANDMARKS
H   Old Town Hall
B   Charles Bridge
K   Hradčany Castle
V   St. Vitus Cathedral
P   Powder Gate
I   GoldenLane Inn

VENICE LANDMARKS
A   Arsenale
R   Rialto Bridge
D   Doge Palace
S   St. Mark’s Basilica
M   Porta da Mare
I   Sailors Inn


---

## 📁 Project Structure  
```
/ (root)
├─ main.py            # Entry-point of the game  
├─ requirements.txt   # Python dependencies  
├─ .gitignore  
└─ mechs/             # Folder for game mechanics, story logic, and modules  
    ├─ ...
```

---

## 🛠️ Extending the Game  
💡 Add your own stories, events, or characters in `mechs/`.  
💡 Create new mechanics for inventory, combat, or diplomacy.  
💡 Enhance input handling for smoother interaction.  

---

## 🎯 Roadmap  
- [ ] Add more story branches and endings  
- [x] Implement player stats (health, resources)  
- [ ] Add save/load system  
- [x] Improve UX with colored terminal output  
- [ ] Release v1.0 — Full campaign mode  

---

## 🤝 Contributing  
Contributions are welcome!  
1. Fork this repo 🍴  
2. Create a new branch 🌿  
3. Make your changes ✏️  
4. Submit a pull request 🚀  

Please keep consistent formatting and add docstrings where needed.

---

## 📄 License  
🪶 Licensed under the **MIT License** — you’re free to use, modify, and distribute this software, as long as proper credit is given.  
See the [LICENSE](LICENSE) file for full terms.

---

## 📬 Contact  
Found a bug or have an idea?  
📨 Open an issue on GitHub or reach out to the authors.

---

✨ _“History is written by the victors — will it be you?”_ ⚔️
