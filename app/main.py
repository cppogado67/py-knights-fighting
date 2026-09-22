# app/main.py

class Knight:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.power = data["power"] + data["weapon"]["power"]
        self.hp = data["hp"]
        self.protection = sum(armour["protection"] for armour in data.get("armour", []))
        # Add potion effects if exists
        if data.get("potion"):
            self.hp += data["potion"]["effect"].get("hp", 0)
            self.power += data["potion"]["effect"].get("power", 0)
            self.protection += data["potion"]["effect"].get("protection", 0)
    def take_damage(self, opponent_power: int) -> None:
        damage = max(0, opponent_power - self.protection)
        self.hp = max(0, self.hp - damage)

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 40,
        "hp": 70,
        "armour": [
            {"part": "breastplate", "protection": 25},
            {"part": "helmet", "protection": 10},
        ],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {"hp": 10, "power": 5},
        },
    },
    "arthur": {
        "name": "Arthur",
        "power": 35,
        "hp": 80,
        "armour": [
            {"part": "breastplate", "protection": 30},
        ],
        "weapon": {"name": "Excalibur", "power": 50},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 45,
        "hp": 65,
        "armour": [
            {"part": "breastplate", "protection": 20},
            {"part": "shield", "protection": 15},
        ],
        "weapon": {"name": "Spear", "power": 40},
        "potion": {
            "name": "Dark Potion",
            "effect": {"hp": -5, "power": 10},
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {"part": "breastplate", "protection": 25},
        ],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {"hp": 10, "power": 5},
        },
    },
}

def battle(knight1_name: str, knight2_name: str) -> dict:
    knight1 = Knight(KNIGHTS[knight1_name])
    knight2 = Knight(KNIGHTS[knight2_name])
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
