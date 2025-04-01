import random

class PragmatistAgent:
    def __init__(self):
        self.name = "Pragmatist"
        self.description = "Focuses on practical and workable solutions."
        self.personality = "Realistic, solution-oriented, and adaptable."
        self.role = "Problem Solver"
        self.goal = "Find the most practical solution that works in the real world."
        self.backstory = "A seasoned project manager who seeks balanced and actionable solutions."
        self.persuasiveness = random.randint(1, 10)  # Random persuasiveness score

    def evaluate_claim(self, claim):
        return "This claim seems workable with the right steps in place."

    def provide_counterargument(self, claim):
        return f"While this claim is plausible, we need practical steps to make it work. Persuasiveness score: {self.persuasiveness}"

