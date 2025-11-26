import json
import csv
import os
from dread import Dread
from colorama import Fore, Style, init

init(autoreset=True)

# ---------------------------
# TEMPLATE SYSTEM
# ---------------------------
def list_templates():
    if not os.path.exists("templates"):
        os.makedirs("templates")
    return [f for f in os.listdir("templates") if f.endswith(".json")]

def load_template(filename):
    with open(os.path.join("templates", filename)) as f:
        return json.load(f)

# ---------------------------
# INPUT VALIDATION
# ---------------------------
def get_score(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 10:
                return value
            else:
                print(Fore.RED + "Please enter a number between 0 and 10.")
        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number.")

# ---------------------------
# SAVE RESULTS
# ---------------------------
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

# ---------------------------
# COLOR RISK LEVEL
# ---------------------------
def color_risk_level(level):
    if level == "Low":
        return Fore.GREEN + level + Style.RESET_ALL
    elif level == "Medium":
        return Fore.YELLOW + level + Style.RESET_ALL
    elif level == "High":
        return Fore.RED + level + Style.RESET_ALL
    else:
        return level

# ---------------------------
# MAIN APPLICATION
# ---------------------------
def main():
    print(Fore.CYAN + "\n--- DREAD Risk Scoring Tool ---" + Style.RESET_ALL)

    while True:
        print("\nChoose input method:")
        print("1. Manual entry")
        print("2. Load from template")

        choice = input("Select 1 or 2: ")
        while choice not in ("1", "2"):
            choice = input("Please enter 1 or 2: ")

        if choice == "1":
            # ---------------------------
            # MANUAL ENTRY
            # ---------------------------
            name = input("Threat name: ")
            damage = get_score("Damage (0–10): ")
            reproducibility = get_score("Reproducibility (0–10): ")
            exploitability = get_score("Exploitability (0–10): ")
            affected_users = get_score("Affected Users (0–10): ")
            discoverability = get_score("Discoverability (0–10): ")

        else:
            # ---------------------------
            # TEMPLATE LOADING
            # ---------------------------
            templates = list_templates()
            if not templates:
                print(Fore.RED + "No templates found! Please add JSON files in templates/")
                continue

            print("\nAvailable templates:")
            for idx, t in enumerate(templates, 1):
                print(f"{idx}. {t}")

            t_choice = input("Select template number: ")
            while not t_choice.isdigit() or not (1 <= int(t_choice) <= len(templates)):
                t_choice = input("Enter valid template number: ")

            data = load_template(templates[int(t_choice)-1])
            name = data["name"]
            damage = data["damage"]
            reproducibility = data["reproducibility"]
            exploitability = data["exploitability"]
            affected_users = data["affected_users"]
            discoverability = data["discoverability"]

            print(Fore.GREEN + f"\nLoaded template: {name}" + Style.RESET_ALL)

        # ---------------------------
        # CREATE DREAD OBJECT
        # ---------------------------
        threat = Dread(name, damage, reproducibility, exploitability, affected_users, discoverability)

        # ---------------------------
        # DISPLAY RESULTS
        # ---------------------------
        print(Fore.MAGENTA + "\n--- RESULTS ---" + Style.RESET_ALL)
        print(f"Threat: {threat.name}")
        print(f"Total Score: {threat.total_score()}")
        print(f"Risk Level: {color_risk_level(threat.risk_level())}")

        # ---------------------------
        # SAVE RESULTS
        # ---------------------------
        save_to_csv(threat)
        save_to_json(threat)

        print(Fore.GREEN + "[+] Saved to CSV and JSON.\n" + Style.RESET_ALL)

        again = input("Do you want to score another threat? (y/n): ").lower()
        while again not in ("y", "n"):
            again = input("Please enter 'y' or 'n': ").lower()
        if again == "n":
            print(Fore.CYAN + "Exiting... Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()