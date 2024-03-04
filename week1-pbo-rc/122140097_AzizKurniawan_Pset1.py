import random

class Robot:
    def __init__(self, name, max_hp, attack_damage_range, attack_accuracy):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack_damage_range = attack_damage_range
        self.attack_accuracy = attack_accuracy

    def attack_enemy(self, enemy):
        if random.random() < self.attack_accuracy:
            damage = random.randint(self.attack_damage_range[0], self.attack_damage_range[1])
            enemy.receive_damage(damage)
            print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack missed!")

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def regen_health(self):
        regen_amount = random.randint(1, self.max_hp // 4)
        self.hp += regen_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} regenerates {regen_amount} health.")

    def is_alive(self):
        return self.hp > 0


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.rounds = 0

    def display_health(self):
        print(f"{self.robot1.name} Health: {self.robot1.hp} | {self.robot2.name} Health: {self.robot2.hp}")

    def start_game(self):
        print(f"Battle between {self.robot1.name} and {self.robot2.name} begins!")
        while self.robot1.is_alive() and self.robot2.is_alive():
            self.rounds += 1
            print(f"\nRound {self.rounds}")
            self.display_health()

            self.robot1.attack_enemy(self.robot2)
            if not self.robot2.is_alive():
                print(f"{self.robot2.name} is defeated! {self.robot1.name} wins!")
                self.display_health_winner(self.robot1)
                break

            self.robot2.attack_enemy(self.robot1)
            if not self.robot1.is_alive():
                print(f"{self.robot1.name} is defeated! {self.robot2.name} wins!")
                self.display_health_winner(self.robot2)
                break

            self.robot1.regen_health()
            self.robot2.regen_health()

    def display_health_winner(self, winner):
        print(f"\n{winner.name} is the winner with {winner.hp} health remaining!")

# Example usage:
robot1 = Robot(name="Megatron", max_hp=100, attack_damage_range=(30, 50), attack_accuracy=0.7)
robot2 = Robot(name="Optimus Prime", max_hp=110, attack_damage_range=(15, 60), attack_accuracy=0.65)

game = Game(robot1, robot2)
game.start_game()
