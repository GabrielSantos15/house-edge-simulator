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
        players=500,
        initial_bank=1000,
        bet=50,
        strategy="Fixed Bet",
        roulette="European"
    ),
        SimulationConfig(
        experiment_id=2,
        players=500,
        initial_bank=1000,
        bet=50,
        strategy="D'Alembert",
        roulette="European",
    ),
    SimulationConfig(
        experiment_id=3,
        players=500,
        initial_bank=1000,
        bet=50,
        strategy="Fibonacci",
        roulette="European",
    ),
    SimulationConfig(
        experiment_id=4,
        players=500,
        initial_bank=1000,
        bet=50,
        strategy="Martingale",
        roulette="European"
    ),
]

@dataclass
class AnalysisConfig:
    top_players: int = 30
    bottom_players: int = 30
    random_players: int = 40

analysis_config = AnalysisConfig()