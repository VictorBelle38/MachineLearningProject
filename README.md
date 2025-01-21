# Projeto: Predição de Solubilidade de Moléculas usando Machine Learning

Este projeto tem como objetivo prever a solubilidade de moléculas (`logS`) com base em suas características físico-químicas, utilizando técnicas de Machine Learning. O dataset utilizado contém informações como peso molecular, proporção de átomos aromáticos, entre outras.

---

## Descrição do Projeto

O dataset utilizado contém as seguintes colunas:
- `MolLogP`: Coeficiente de partição octanol-água.
- `MolWt`: Peso molecular.
- `NumRotatableBonds`: Número de ligações rotacionais.
- `AromaticProportion`: Proporção de átomos aromáticos.
- `logS`: Solubilidade (variável alvo).

O projeto inclui:
- Pré-processamento dos dados.
- Treinamento de modelos de Machine Learning (Regressão Linear e Random Forest).
- Avaliação dos modelos usando métricas como RMSE e R².

---

## Estrutura do Projeto

/MachineLearningProject/
├── /data/ # Pasta para armazenar os dados
│ └── delaney_solubility_with_descriptors.csv # Dataset original
├── /notebooks/ # Pasta para armazenar notebooks
│ └── Machine_Learning_Project.ipynb # Notebook principal
├── /scripts/ # Pasta para scripts auxiliares
│ ├── preprocessamento.py # Script de pré-processamento
│ └── train.py # Script de treinamento e avaliação
├── README.md # Arquivo README principal
└── requirements.txt # Lista de dependências do projeto
