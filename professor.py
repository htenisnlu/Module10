class Professor:
    def __init__(self, name, weapons=None):
        self.name = name
        self.weapons = weapons if weapons else []

    def introduce(self):
        return f"Hello Professor {self.name}"

    def profile(self):
        return self.name, self.weapons

    def list_weapons(self):
        if self.weapons:
            return f"I am armed with: {', '.join(self.weapons)}."
        else:
            return "I have no weapons at the moment."

    def add_weapon(self, weapon):
        if weapon not in self.weapons:
            self.weapons.append(weapon)
            return f"{weapon} added to your arsenal."
        else:
            return f"{weapon} is already in your arsenal."

