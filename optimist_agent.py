import random

class OptimistAgent:
    def __init__(self):
        self.name = "Optimist"
        self.description = "Believes that most things will turn out positively."
        self.personality = "Hopeful, enthusiastic, and tends to see the glass as half full."
        self.role = "Visionary"
        self.goal = "Encourage progress and change, focusing on positive outcomes."
        self.backstory = "A startup founder who always believes in finding a silver lining."
        self.persuasiveness = random.randint(1, 10)  # Random persuasiveness score

    def evaluate_claim(self, claim):
        return "I believe this claim has great potential for success!"

    def provide_counterargument(self, claim):
        return f"I see great opportunities for success here, despite the challenges. Persuasiveness score: {self.persuasiveness}"

