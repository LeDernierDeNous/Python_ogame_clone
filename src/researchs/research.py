from abc import ABC, abstractmethod
from src.resources.resource import Resource

class Research(ABC):
    def __init__(self, name: str, metal_cost: int, crystal_cost: int, deuterium_cost: int):
        self.name = name
        self.metal_cost = metal_cost
        self.crystal_cost = crystal_cost
        self.deuterium_cost = deuterium_cost
        self.is_completed = False

    @abstractmethod
    def get_cost(self) -> Resource:
        """
        Returns the cost of the research as a Resource object.
        """
        return Resource(metal=self.metal_cost, crystal=self.crystal_cost, deuterium=self.deuterium_cost)

    def can_afford(self, available_resources: Resource) -> bool:
        """
        Determines if the research can be afforded given the available resources.
        """
        return (
            available_resources.metal >= self.metal_cost and
            available_resources.crystal >= self.crystal_cost and
            available_resources.deuterium >= self.deuterium_cost
        )

    def conduct_research(self, available_resources: Resource) -> bool:
        """
        Conducts the research if there are enough resources available.
        Returns True if the research was successfully conducted, False otherwise.
        """
        if self.can_afford(available_resources) and not self.is_completed:
            available_resources.metal -= self.metal_cost
            available_resources.crystal -= self.crystal_cost
            available_resources.deuterium -= self.deuterium_cost
            self.is_completed = True
            return True
        return False

    @abstractmethod
    def apply_effect(self):
        """
        Applies the effect of the research. This method should be implemented by subclasses.
        """
        pass

    def __str__(self) -> str:
        status = "Completed" if self.is_completed else "In Progress"
        return f"Research: {self.name}, Cost: {self.get_cost()}, Status: {status}"
