import json
import csv
from dread import Dread

def save_to_csv(threat):
    with open("dread_results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            threat.name,
            threat.damage,
            threat.reproducibility,
            threat.exploitability,
            threat.affected_users,
            threat.discoverability,
            threat.total_score(),
            threat.risk_level()
        ])

def save_to_json(threat):
    data = {
        "name": threat.name,
        "damage": threat.damage,
        "reproducibility": threat.reproducibility,
        "exploitability": threat.exploitability,
        "affected_users": threat.affected_users,
        "discoverability": threat.discoverability,
        "total_score": threat.total_score(),
        "risk_level": threat.risk_level()
    }
    with open("dread_results.json", "a") as json_file:
        json.dump(data, json_file)
        json_file.write("\n")

def get_score(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 10:
                return value
            else:
                print("Please enter a number between 0 and 10.")
        except ValueError:
            print("Invalid input. Enter a number.")

def main():
    print("\n--- DREAD Risk Scoring Tool ---")

    while True:
        print("\nEnter a new threat to score:\n")

        name = input("Threat name: ")

        damage = get_score("Damage (0–10): ")
        reproducibility = get_score("Reproducibility (0–10): ")
        exploitability = get_score("Exploitability (0–10): ")
        affected_users = get_score("Affected Users (0–10): ")
        discoverability = get_score("Discoverability (0–10): ")

        threat = Dread(
            name,
            damage,
            reproducibility,
            exploitability,
            affected_users,
            discoverability
        )

        print("\n--- RESULTS ---")
        print(f"Threat: {threat.name}")
        print(f"Total Score: {threat.total_score()}")
        print(f"Risk Level: {threat.risk_level()}")

        save_to_csv(threat)
        save_to_json(threat)

        print("\n[+] Saved to CSV and JSON.")

        again = input("\nDo you want to score another threat? (y/n): ").lower()

        while again not in ("y", "n"):
            again = input("Please enter 'y' or 'n': ").lower()

        if again == "n":
            print("\nExiting... Goodbye!")
            break

if __name__ == "__main__":
    main()