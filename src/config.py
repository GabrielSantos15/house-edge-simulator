from dataclasses import dataclass

@dataclass
class SimulationConfig:
    experiment_id: int
    players: int
    initial_bank: int
    bet: int
    strategy: str
    roulette: str
    max_rounds: int | None = None


config = SimulationConfig(
    experiment_id=1,
    players=100,
    initial_bank=100,
    bet=5,
    strategy="Fixed Bet",
    roulette="European"
)
