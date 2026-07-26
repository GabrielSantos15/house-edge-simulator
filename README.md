# 🎲 House Edge Simulator

**Simulando milhares de jogadores e diferentes estratégias de aposta para demonstrar, com dados, que nenhuma delas escapa da vantagem matemática da casa.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#-licença)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)](#-roadmap)

---

## 📖 Visão Geral

**House Edge Simulator** é um projeto de simulação estatística construído em torno de uma única ideia: quando um jogo tem expectativa matemática negativa, nenhuma forma de jogar muda isso — só muda o caminho até lá.

Utilizando Python, milhares de jogadores são simulados apostando na roleta europeia, cada um seguindo uma estratégia diferente. Os resultados são exportados para o Power BI, onde se transformam em visualizações que mostram, na prática, conceitos como probabilidade, valor esperado, vantagem da casa e Lei dos Grandes Números.

O objetivo não é incentivar apostas nem descobrir uma estratégia vencedora — é usar um cenário simples e controlado para observar, com dados reais de simulação, como a matemática se impõe no longo prazo, independentemente do estilo de aposta.

Os principais conceitos explorados no projeto são:

- 🏛️ **House Edge (vantagem da casa)**
- 📈 **Lei dos Grandes Números**
- 💰 **Valor Esperado**
- 🎯 **Probabilidade**
- 🎰 **Simulações de Monte Carlo**
- 📖 **Storytelling com Dados**

A roleta é usada aqui como um laboratório de probabilidade fixa — um sistema simples, com regras claras e vantagem conhecida, ideal para observar como essa vantagem se acumula de forma implacável ao longo de milhares de eventos independentes, não importa a estratégia por trás de cada aposta.

---

## ❓ A Pergunta

> **"Existe alguma estratégia de aposta capaz de vencer a vantagem matemática da casa no longo prazo?"**

Esse é o fio condutor do projeto. A roleta europeia tem 37 números (0 a 36). Uma aposta simples em "Vermelho" paga 1:1, mas a probabilidade real de vitória é **18/37 (≈48,65%)**, não 50%. Essa diferença de **2,7%** é o *house edge* — pequena o suficiente para parecer irrelevante em uma única rodada, mas decisiva quando multiplicada por milhares de jogadas.

A crença popular é que uma estratégia bem construída — dobrar a aposta após perder, seguir uma progressão, gerenciar o risco de forma inteligente — pode reverter esse quadro. O House Edge Simulator testa essa crença simulando milhares de jogadores sob diferentes estratégias e observando o que realmente acontece com o saldo de cada um ao longo do tempo.

O projeto existe para responder essa pergunta **com dados simulados, não com intuição**.

---

## ⚙️ Como Funciona

O fluxo do projeto segue um pipeline simples de ponta a ponta:

```
Configuração
    ↓
Motor de Simulação
    ↓
CSV
    ↓
Power BI
    ↓
Análises e Insights
```

1. **Configuração** — Define os parâmetros do experimento (número de jogadores, banca inicial, valor de aposta, estratégia, tipo de roleta).
2. **Motor de Simulação** — Executa rodadas de Monte Carlo para cada jogador até a falência (ou até um limite de rodadas configurado).
3. **CSV** — Os resultados são exportados em três datasets estruturados, prontos para análise.
4. **Power BI** — Os CSVs alimentam um dashboard interativo com métricas, gráficos e storytelling de dados.
5. **Análises e Insights** — Análises obtidas a partir dos resultados da simulação, mostrando como cada estratégia se comporta diante da mesma vantagem matemática da casa.

---

## 🏗️ Arquitetura do Projeto

```
house-edge-simulator/
│
├── src/
│   ├── main.py
│   ├── simulator.py
│   ├── config.py
│   ├── roulette/
│   ├── strategies/
│   └── exporter/
│
├── data/
│   ├── experimentos.csv
│   ├── resumo_jogadores.csv
│   └── historico.csv
│
├── dashboard/
│   └── house_edge_dashboard.pbix
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Tecnologias

| Tecnologia | Uso no Projeto |
|---|---|
| **Python** | Linguagem principal do motor de simulação |
| **Pandas** | Estruturação e exportação dos dados simulados |
| **Power BI** | Construção dos dashboards analíticos e storytelling |
| **Git / GitHub** | Versionamento e distribuição do projeto |

## 🧠 Conceitos Estudados

| Conceito | Aplicação no Projeto |
|---|---|
| **House Edge** | Vantagem matemática da casa, presente em toda estratégia simulada |
| **Lei dos Grandes Números** | Convergência dos resultados para a expectativa matemática conforme o número de rodadas cresce |
| **Valor Esperado** | Retorno médio esperado por rodada, dado a probabilidade real de vitória |
| **Probabilidade** | Base para o sorteio dos números e cálculo das chances reais de cada aposta |
| **Simulação de Monte Carlo** | Núcleo estatístico que gera milhares de trajetórias possíveis para cada estratégia |

---

## 🎯 Estratégias — Cenários de Teste, não Soluções

As estratégias implementadas no simulador **não são candidatas a "vencer" a roleta**. Elas são cenários experimentais usados para testar a mesma hipótese sob diferentes formas de gerenciar a aposta: mudar o valor apostado a cada rodada altera a volatilidade e o tempo de sobrevivência, mas não altera a probabilidade real por trás de cada giro.

Cada estratégia adicionada ao projeto existe para reforçar — não contradizer — a resposta à pergunta central.

**Disponível atualmente:**

| Estratégia | Descrição |
|---|---|
| ✅ **Fixed Bet** | Aposta um valor fixo em Vermelho a cada rodada, independentemente dos resultados anteriores |

**Planejadas (roadmap):**

| Estratégia | Descrição |
|---|---|
| 🔜 **Martingale** | Dobra a aposta a cada derrota, na tentativa de recuperar perdas na próxima vitória |
| 🔜 **Fibonacci** | Progressão de apostas baseada na sequência de Fibonacci após derrotas |
| 🔜 **D'Alembert** | Aumenta a aposta em uma unidade após derrota e reduz uma unidade após vitória |
| 🔜 **Labouchere** | Sistema de cancelamento baseado em uma sequência de números definida previamente |

---

## 🗃️ Estrutura dos Dados

A simulação exporta três arquivos CSV, que são os arquivos utilizados pelo Power BI para montar o dashboard.

### `experimentos.csv`
Metadados de cada cenário simulado — uma linha por experimento. Permite comparar diferentes configurações (estratégias, roletas, bancas) entre si.

| Coluna | Descrição |
|---|---|
| `experimento` | ID do experimento |
| `jogadores` | Total de jogadores simulados |
| `banca_inicial` | Banca inicial configurada |
| `valor_aposta` | Valor fixo apostado por rodada |
| `estrategia` | Estratégia de aposta utilizada |
| `roleta` | Tipo de roleta (europeia, americana...) |

### `resumo_jogadores.csv`
Resultado consolidado da sessão de cada jogador — uma linha por jogador. Base para as métricas de sobrevivência e falência.

| Coluna | Descrição |
|---|---|
| `experimento` | ID do experimento |
| `jogador` | ID do jogador |
| `tempo_sobrevivencia` | Quantidade de rodadas jogadas até parar |
| `banca_inicial` | Banca inicial |
| `banca_final` | Saldo ao final da sessão |
| `maior_banca` | Maior saldo atingido durante a sessão |
| `falencia` | Indica se o jogador ficou sem saldo suficiente para apostar |

### `historico.csv`
O histórico detalhado de cada rodada — uma linha por **rodada** de **cada jogador**. Base para gráficos de evolução de saldo ao longo do tempo.

| Coluna | Descrição |
|---|---|
| `experimento` | ID do experimento |
| `jogador` | ID do jogador |
| `rodada` | Número da rodada |
| `numero` | Número sorteado (0–36) |
| `cor` | Cor sorteada (Vermelho / Preto / Verde) |
| `resultado` | Vitória ou Derrota |
| `valor_aposta` | Valor apostado na rodada |
| `variacao` | Ganho (+) ou perda (-) na rodada |
| `saldo_inicial` | Saldo antes da rodada |
| `saldo_final` | Saldo depois da rodada |

> ⚠️ **Nota sobre volume:** `historico.csv` cresce rapidamente (jogadores × rodadas). Para simulações grandes, vale considerar exportação incremental, amostragem ou migração para um banco colunar (Parquet/DuckDB).

---

## 📊 Dashboard

O dashboard foi desenvolvido para contar uma história baseada em dados. Em vez de apresentar apenas gráficos, cada página responde a uma pergunta específica sobre o comportamento estatístico da roleta europeia — e, no fim, todas convergem para a mesma conclusão.

**Perguntas respondidas:**

- 🎲 O que acontece com um único jogador?
- 👥 O que muda quando milhares de jogadores são simulados?
- 📉 Em que momento a vantagem da casa se torna evidente?
- ⚖️ Mudar de estratégia muda o resultado — ou só o caminho até ele?

**Análises presentes no dashboard:**

- 📉 **Evolução do saldo** — trajetória do saldo de jogadores ao longo das rodadas, mostrando altos e baixos até a falência.
- ⏱️ **Tempo médio até a falência** — quantas rodadas, em média, um jogador sobrevive antes de zerar a banca.
- 📊 **Distribuição das bancas finais** — histograma mostrando onde a maioria dos jogadores termina.
- ❤️ **Taxa de sobrevivência** — percentual de jogadores que ainda possuem saldo ao final do experimento.
- ⚖️ **Estratégia por estratégia** — como cada uma altera a volatilidade e o tempo de jogo, sem alterar a expectativa matemática final.
- 🎯 **KPIs centrais** — banca média final, maior banca atingida, % de jogadores falidos, rodada média de falência.

---

## 🎓 Objetivos de Aprendizagem

Este projeto foi construído como um exercício prático de ponta a ponta, cobrindo:

- 🐍 **Programação em Python** (orientação a objetos, dataclasses, boas práticas)
- 🗂️ **Modelagem de dados** (normalização em múltiplos datasets relacionáveis)
- 📐 **Estatística** aplicada a fenômenos de longo prazo
- 🎲 **Probabilidade** e eventos independentes
- 🔁 **Simulação** (Monte Carlo) como ferramenta de análise
- 🔄 **ETL** (extração, transformação e exportação de dados simulados)
- 📊 **Power BI** (modelagem, DAX, storytelling visual)
- 📈 **Data Visualization** e comunicação de insights

---

## 🗺️ Roadmap

### Simulação
- [x] Simulação da roleta europeia
- [x] Estratégia de aposta fixa
- [x] Simulação de múltiplos jogadores
- [x] Exportação para CSV

### Dashboard
- [ ] Dashboard inicial
- [ ] KPIs
- [ ] Storytelling
- [ ] Análise da Lei dos Grandes Números
- [ ] Simulações comparativas

### Estratégias (novos cenários de teste)
- [ ] Martingale
- [ ] Fibonacci
- [ ] D'Alembert
- [ ] Labouchere
- [ ] Comparação de volatilidade entre estratégias

### Melhorias Futuras
- [ ] Testes automatizados
- [ ] Configuração via arquivo JSON
- [ ] Geração automática de relatórios

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Windows) para abrir o dashboard

### 1. Clone o repositório

```bash
git clone https://github.com/<seu-usuario>/house-edge-simulator.git
cd house-edge-simulator
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a simulação

```bash
python src/main.py
```

Isso irá gerar os arquivos `experimentos.csv`, `resumo_jogadores.csv` e `historico.csv` na pasta `data/`.

### 5. Abra o dashboard no Power BI

1. Abra o **Power BI Desktop**.
2. Abra o arquivo `dashboard/house_edge_dashboard.pbix`.
3. Atualize a fonte de dados apontando para os CSVs gerados na pasta `data/`.
4. Clique em **Atualizar** para carregar os novos resultados da simulação.

---

## ⚠️ Aviso

Este projeto tem **finalidade exclusivamente educacional e estatística**. Seu objetivo é demonstrar, através de simulações matemáticas, que nenhuma estratégia de aposta altera uma expectativa matemática negativa no longo prazo.

**O House Edge Simulator não incentiva, promove ou ensina formas de apostar.** Nenhum dinheiro real é utilizado, apostado ou processado em nenhuma etapa deste projeto. Os dados gerados são inteiramente sintéticos, produzidos por um gerador de números aleatórios em um ambiente controlado de simulação.

Se você ou alguém que você conhece luta com problemas relacionados a jogos de azar, procure ajuda profissional especializada.

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

Não importa a estratégia. Enquanto a expectativa matemática for negativa, a vantagem da casa prevalece no longo prazo.

</div>
