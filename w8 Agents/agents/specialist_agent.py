import modal
from agents.agent import Agent


class SpecialistAgent(Agent):
    """
    A wrapper class that calls the "Pricer" class from pricer-service app we deployed on Modal in the pricer_service2.py file.
    this simplifies the call of the price model and makes it easier to use in the agent.
    """

    name = "Specialist Agent"
    color = Agent.RED

    def __init__(self):
        """
        Set up this Agent by creating an instance of the modal class
        """
        self.log("Specialist Agent is initializing - connecting to modal")
        Pricer = modal.Cls.lookup("pricer-service", "Pricer")
        self.pricer = Pricer()
        self.log("Specialist Agent is ready")
        
    def price(self, description: str) -> float:
        """
        Make a remote call to return the estimate of the price of this item
        """
        self.log("Specialist Agent is calling remote fine-tuned model")
        result = self.pricer.price.remote(description)
        self.log(f"Specialist Agent completed - predicting ${result:.2f}")
        return result
