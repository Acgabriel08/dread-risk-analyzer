import json
import csv
from dread import Dread
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

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
            value = int(input(Fore.CYAN + prompt + Style.RESET_ALL))
            if 0 <= value <= 10:
                return value
            else:
                print(Fore.YELLOW + "Please enter a number between 0 and 10." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number." + Style.RESET_ALL)

def color_risk_level(level):
    """Return the colored string for the risk level."""
    level_upper = level.upper()
    if level_upper == "LOW":
        return Fore.GREEN + level + Style.RESET_ALL
    elif level_upper == "MEDIUM":
        return Fore.YELLOW + level + Style.RESET_ALL
    elif level_upper == "HIGH":
        return Fore.RED + level + Style.RESET_ALL
    else:
        return level  # Default, no color

def main():
    print(Fore.MAGENTA + "\n--- DREAD Risk Scoring Tool ---" + Style.RESET_ALL)

    while True:
        print(Fore.BLUE + "\nEnter a new threat to score:\n" + Style.RESET_ALL)

        name = input(Fore.CYAN + "Threat name: " + Style.RESET_ALL)

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

        print(Fore.MAGENTA + "\n--- RESULTS ---" + Style.RESET_ALL)
        print(Fore.GREEN + f"Threat: {threat.name}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Total Score: {threat.total_score()}" + Style.RESET_ALL)
        print(f"Risk Level: {color_risk_level(threat.risk_level())}")

        save_to_csv(threat)
        save_to_json(threat)

        print(Fore.GREEN + "\n[+] Saved to CSV and JSON." + Style.RESET_ALL)

        again = input(Fore.CYAN + "\nDo you want to score another threat? (y/n): " + Style.RESET_ALL).lower()

        while again not in ("y", "n"):
            again = input(Fore.YELLOW + "Please enter 'y' or 'n': " + Style.RESET_ALL).lower()

        if again == "n":
            print(Fore.MAGENTA + "\nExiting... Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()