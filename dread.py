class Dread:
    def __init__(self, name, damage, reproducibility, exploitability, affected_users, discoverability):
        self.name = name
        self.damage = damage
        self.reproducibility = reproducibility
        self.exploitability = exploitability
        self.affected_users = affected_users
        self.discoverability = discoverability

    def total_score(self):
        return (
            self.damage
            + self.reproducibility
            + self.exploitability
            + self.affected_users
            + self.discoverability
        )

    def risk_level(self):
        score = self.total_score()

        if score <= 15:
            return "Low"
        elif 16 <= score <= 30:
            return "Medium"
        elif 31 <= score <= 40:
            return "High"
        else:
            return "Critical"

    def coloured_risk(self):
        """Return colour-coded risk classification for CLI display."""
        level = self.risk_level()

        colours = {
            "Low": "\033[92m",       # Green
            "Medium": "\033[93m",    # Yellow
            "High": "\033[91m",      # Red
            "Critical": "\033[95m",  # Magenta
        }

        reset = "\033[0m"
        return f"{colours[level]}{level}{reset}"