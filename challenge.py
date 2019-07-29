import pandas as pd
import random
from operator import attrgetter

applicants = pd.read_csv("applicants.csv")

df = pd.DataFrame(applicants)


class Applicant:
    def __init__(
        self, name, health, damage, attacks, dodge, critical, initiative
    ):
        self.name = name
        self.health = health
        self.damage = damage
        self.attacks = attacks
        self.initial_attacks = attacks
        self.dodge = dodge
        self.critical = critical
        self.initiative = initiative
        self.wins = 0
        self.losses = 0

    def initializer():
        return random.uniform(0, 1)

    def check_winner(self, char1, char2):
        if char1.health <= 0:
            char2.wins += 1
            char1.losses += 1
            print(f"{str(char2.name)} wins")
        elif char2.health <= 0:
            char1.wins += 1
            char2.losses += 1
            print(f"{str(char1.name)} wins")

    def fight(self, enemy, counter=1):
        counter = counter
        while (self.health > 0) and (enemy.health > 0):
            print(f"Round {counter}:")
            while (self.attacks > 0) and (enemy.attacks > 0):
                init = random.uniform(0, 1)
                if init < 0.50:
                    print(
                        f"{self.name} hits {enemy.name} for {self.damage} ({enemy.health} -> {enemy.health - self.damage})"
                    )
                    enemy.health -= self.damage
                    self.attacks -= 1
                    return enemy.fight(self, counter)
                else:
                    print(
                        f"{enemy.name} hits {self.name} for {enemy.damage} ({self.health} -> {self.health - enemy.damage})"
                    )
                    self.health -= enemy.damage
                    enemy.attacks -= 1
                    return self.fight(enemy, counter)
            while self.attacks > 0:
                print(
                    f"{self.name} hits {enemy.name} for {self.damage} ({enemy.health} -> {enemy.health - self.damage})"
                )
                enemy.health -= self.damage
                self.attacks -= 1
            while enemy.attacks > 0:
                print(
                    f"{enemy.name} hits {self.name} for {enemy.damage} ({self.health} -> {self.health - enemy.damage})"
                )
                self.health -= enemy.damage
                enemy.attacks -= 1
            self.attacks = self.initial_attacks
            enemy.attacks = enemy.initial_attacks
            counter += 1
        self.check_winner(self, enemy)


applicants = [
    Applicant(
        name=row["Name"],
        health=row["Health"],
        damage=row["Damage"],
        attacks=row["Attacks"],
        dodge=row["Dodge"],
        critical=row["Critical"],
        initiative=row["Initiative"],
    )
    for index, row in df.iterrows()
]

for i in range(len(applicants)):
    for j in range(i + 1, len(applicants)):
        applicants[i].fight(applicants[j])

total_wins = [applicant for applicant in applicants]
winner = max(total_wins, key=attrgetter("wins"))
print(f"{str(winner.name)} is the BEST")
