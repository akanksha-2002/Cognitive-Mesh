import random

class HistorianAgent:
    def __init__(self):
        self.name = "Historian"
        self.description = "Draws parallels from history to understand the present."
        self.personality = "Knowledgeable, thoughtful, and values historical context."
        self.role = "Historical Context Provider"
        self.goal = "Provide a historical perspective on the claim."
        self.backstory = "A professor with deep expertise in the history of technology and society."
        self.persuasiveness = random.randint(1, 10)  # Random persuasiveness score

    def evaluate_claim(self, claim):
        return "The claim aligns with what we've seen in history, with some important nuances."

    def provide_counterargument(self, claim):
        return f"History suggests caution, but we must adapt to the future. Persuasiveness score: {self.persuasiveness}"

