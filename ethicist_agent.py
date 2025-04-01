import random

class EthicistAgent:
    def __init__(self):
        self.name = "Ethicist"
        self.description = "Focuses on the moral and ethical implications of actions."
        self.personality = "Principled, reflective, and deeply concerned with ethics."
        self.role = "Moral Compass"
        self.goal = "Evaluate the ethical implications of the claim."
        self.backstory = "A philosopher who examines technological impacts on society and individuals."
        self.persuasiveness = random.randint(1, 10)  # Random persuasiveness score

    def evaluate_claim(self, claim):
        return "Ethically, this claim seems to be sound, but further reflection is needed."

    def provide_counterargument(self, claim):
        return f"Ethically, we must ensure that the rights of individuals are not harmed. Persuasiveness score: {self.persuasiveness}"

