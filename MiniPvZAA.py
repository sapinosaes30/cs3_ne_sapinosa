class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        print(self.name + " attacks " + zombie.name + "!")
        zombie.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(self.name + " took " + str(amount) + " damage! Remaining HP: " + str(self.health))


class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        self.distance -= 1
        print(self.name + " walked 1 step closer! Distance left: " + str(self.distance))

    def attack(self, plant):
        print(self.name + " attacks " + plant.name + "!")
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(self.name + " took " + str(amount) + " damage! Remaining HP: " + str(self.health))


def run_game():
    plant1 = Plant("Peeshooter", 20, 15)
    plant2 = Plant("Snow Pee", 15, 10)
    zombie = Zombie("Rene Zombie", 60, 10, 2)

    turn = 1

    while True:
        print(f"\n=== TURN {turn} ===")
        print(f"{plant1.name} HP: {plant1.health} | "
              f"{plant2.name} HP: {plant2.health} | "
              f"{zombie.name} HP: {zombie.health} (Distance: {zombie.distance})")

        if plant1.health > 0:
            plant1.attack(zombie)
            if zombie.health == 0:
                print("\n" + zombie.name + " was defeated! PLANTS WIN!")
                return

        if plant2.health > 0:
            plant2.attack(zombie)
            if zombie.health == 0:
                print("\n" + zombie.name + " was defeated! PLANTS WIN!")
                return

        if plant1.health > 0:
            target = plant1
        else:
            target = plant2

        if zombie.distance > 0:
            zombie.move()
        else:
            zombie.attack(target)
            if plant1.health == 0 and plant2.health == 0:
                print("\nBoth plants were defeated! ZOMBIE WINS!")
                return

        turn += 1


if __name__ == "__main__":
    run_game()