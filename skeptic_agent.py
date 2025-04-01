import random
from pydantic import BaseModel  # Only if you're using Pydantic for validation

# If you are not using Pydantic validation, replace BaseModel with a regular class.
class SkepticAgent:
    def __init__(self):
        self.name = "Skeptic"
        self.description = "Challenges arguments and verifies factual accuracy."
        self.personality = "Analytical, cautious, and always questions assumptions."
        self.role = "Fact Checker"
        self.goal = "Ensure only well-supported claims are accepted."
        self.backstory = "A former researcher who now dedicates efforts to debunking misinformation."
        self.persuasiveness = random.randint(1, 10)  # Random persuasiveness score

    def evaluate_claim(self, claim):
        if "evidence" not in claim.lower():
            return "This claim lacks strong evidence. Can you provide supporting data?"
        return "The claim is reasonable, but further verification is needed."

    def provide_counterargument(self, claim):
        return f"I challenge this claim because it lacks verifiable data to back it up. Persuasiveness score: {self.persuasiveness}"

if __name__ == "__main__":
    skeptic = SkepticAgent()
    print(skeptic.evaluate_claim("AI will replace all jobs."))
