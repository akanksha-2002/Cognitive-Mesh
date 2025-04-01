import random
from pydantic import BaseModel  # Only if you're using Pydantic for validation

# Base Agent class
class Agent:
    def __init__(self, name, description, personality, role, goal, backstory):
        self.name = name
        self.description = description
        self.personality = personality
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.persuasiveness = random.randint(1, 10)  # Random persuasiveness score

    def evaluate_claim(self, claim):
        # Default evaluation logic for any agent
        return "This claim seems reasonable."

    def provide_counterargument(self, claim):
        # Default counterargument logic for any agent
        return "I don't agree with this claim, here's why."

# SkepticAgent class (inherits from Agent)
class SkepticAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Skeptic",
            description="Challenges arguments and verifies factual accuracy.",
            personality="Analytical, cautious, and always questions assumptions.",
            role="Fact Checker",
            goal="Ensure only well-supported claims are accepted.",
            backstory="A former researcher who now dedicates efforts to debunking misinformation."
        )
    
    def evaluate_claim(self, claim):
        if "evidence" not in claim.lower():
            return "This claim lacks strong evidence. Can you provide supporting data?"
        return "The claim is reasonable, but further verification is needed."

    def provide_counterargument(self, claim):
        return f"I challenge this claim because it lacks verifiable data to back it up. Persuasiveness score: {self.persuasiveness}"

# OptimistAgent class (inherits from Agent)
class OptimistAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Optimist",
            description="Focuses on the positive aspects and opportunities.",
            personality="Hopeful, enthusiastic, and always sees the potential in any situation.",
            role="Opportunity Seeker",
            goal="Highlight the potential benefits and success of the claim.",
            backstory="An idealist who believes in progress and the power of innovation."
        )
    
    def evaluate_claim(self, claim):
        return "I believe this claim has great potential for success!"

    def provide_counterargument(self, claim):
        return f"I see great opportunities for success here, despite the challenges. Persuasiveness score: {self.persuasiveness}"

# PragmatistAgent class (inherits from Agent)
class PragmatistAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Pragmatist",
            description="Focuses on practical and actionable steps.",
            personality="Realistic, grounded, and always looking for practical solutions.",
            role="Problem Solver",
            goal="Make the claim more workable and actionable.",
            backstory="A practical thinker who focuses on realistic outcomes."
        )
    
    def evaluate_claim(self, claim):
        return "This claim seems workable with the right steps in place."

    def provide_counterargument(self, claim):
        return f"While this claim is plausible, we need practical steps to make it work. Persuasiveness score: {self.persuasiveness}"

# HistorianAgent class (inherits from Agent)
class HistorianAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Historian",
            description="Looks at past events and draws insights from history.",
            personality="Thoughtful, reflective, and always looks at the past for lessons.",
            role="History Expert",
            goal="Ensure the claim aligns with historical trends and context.",
            backstory="A historian who draws insights from the past to inform the present."
        )
    
    def evaluate_claim(self, claim):
        return "The claim aligns with what we've seen in history, with some important nuances."

    def provide_counterargument(self, claim):
        return f"History suggests caution, but we must adapt to the future. Persuasiveness score: {self.persuasiveness}"

# EthicistAgent class (inherits from Agent)
class EthicistAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Ethicist",
            description="Focuses on the ethical implications of the claim.",
            personality="Principled, compassionate, and concerned with moral implications.",
            role="Ethical Advisor",
            goal="Ensure the claim is ethically sound and considers moral consequences.",
            backstory="An ethicist who believes in the importance of moral considerations in decision-making."
        )
    
    def evaluate_claim(self, claim):
        return "Ethically, this claim seems to be sound, but further reflection is needed."

    def provide_counterargument(self, claim):
        return f"Ethically, we must ensure that the rights of individuals are not harmed. Persuasiveness score: {self.persuasiveness}"

# Main execution (you can test the agents here)
if __name__ == "__main__":
    skeptic = SkepticAgent()
    optimist = OptimistAgent()
    pragmatist = PragmatistAgent()
    historian = HistorianAgent()
    ethicist = EthicistAgent()
    
    # Test: Evaluate claim and counterarguments
    claim = "AI will replace all jobs."
    print(skeptic.evaluate_claim(claim))
    print(skeptic.provide_counterargument(claim))
    
    print(optimist.evaluate_claim(claim))
    print(optimist.provide_counterargument(claim))
    
    print(pragmatist.evaluate_claim(claim))
    print(pragmatist.provide_counterargument(claim))
    
    print(historian.evaluate_claim(claim))
    print(historian.provide_counterargument(claim))
    
    print(ethicist.evaluate_claim(claim))
    print(ethicist.provide_counterargument(claim))
