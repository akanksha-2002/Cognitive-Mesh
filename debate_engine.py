import sys
import os

# Add the parent directory to sys.path to fix module import issue
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from agents.skeptic_agent import SkepticAgent
from agents.optimist_agent import OptimistAgent
from agents.pragmatist_agent import PragmatistAgent
from agents.historian_agent import HistorianAgent
from agents.ethicist_agent import EthicistAgent

class DebateEngine:
    def __init__(self, claim, rounds=3):
        self.claim = claim
        self.rounds = rounds
        self.agents = [
            SkepticAgent(),
            OptimistAgent(),
            PragmatistAgent(),
            HistorianAgent(),
            EthicistAgent()
        ]
    
    def start_debate(self):
        print(f"Debating the claim: {self.claim}\n")
        for round_num in range(self.rounds):
            print(f"--- Round {round_num + 1} ---")
            for agent in self.agents:
                print(f"{agent.name} says: {agent.evaluate_claim(self.claim)}")
                print(f"{agent.name} counter-argues: {agent.provide_counterargument(self.claim)}\n")

if __name__ == "__main__":
    claim = "AI will replace all jobs."
    debate = DebateEngine(claim, rounds=3)  # Set the number of rounds to 3 for this example
    debate.start_debate()
