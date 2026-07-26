from config import configs
import simulator
import exporter
 
 
def main():
    experimentos = []
    resumos = []
    historicos = []
 
    for config in configs:
        e, r, h = simulator.run_simulation(config)

        experimentos.extend(e)
        resumos.extend(r)
        historicos.extend(h)
 
    exporter.export_csv(experimentos, resumos, historicos)
    print("Arquivos gerados com sucesso!")
 
 
if __name__ == "__main__":
    main()
 