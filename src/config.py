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


configs = [
    SimulationConfig(
        experiment_id=1,
        players=1000,
        initial_bank=1000,
        bet=50,
        strategy="Fixed Bet",
        roulette="European"
    ),
    SimulationConfig(
        experiment_id=2,
        players=1000,
        initial_bank=1000,
        bet=50,
        strategy="Martingale",
        roulette="European"
    ),
]