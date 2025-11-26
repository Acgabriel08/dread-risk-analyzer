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
            self.damage +
            self.reproducibility +
            self.exploitability +
            self.affected_users +
            self.discoverability
        )

    def risk_level(self):
        score = self.total_score()

        if score >= 40:
            return "CRITICAL"
        elif score >= 30:
            return "HIGH"
        elif score >= 20:
            return "MEDIUM"
        else:
            return "LOW"