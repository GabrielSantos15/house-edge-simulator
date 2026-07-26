from config import config
import simulator
import exporter

experimentos, resumo, historico = simulator.run_simulation(config)
exporter.export_csv(experimentos, resumo, historico)