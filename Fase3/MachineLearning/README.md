# 🤖 Machine Learning - FarmTech Solutions

## 📋 Sobre

Análise de Machine Learning aplicada à agricultura de precisão, utilizando dados de sensores IoT para prever culturas agrícolas ideais baseadas em condições climáticas e de solo.

---

## 🎯 Objetivos da Análise

1. **Análise Exploratória**: Familiarização com os dados agrícolas
2. **Análise Descritiva**: Identificação de padrões com 7 gráficos
3. **Perfil Ideal**: Determinação das condições ótimas para cada cultura
4. **Modelos Preditivos**: Desenvolvimento de 5 algoritmos de ML diferentes
5. **Avaliação**: Métricas de desempenho e comparação de modelos

---

## 📊 Dataset

**Fonte**: Dados coletados dos sensores IoT ESP32 (Fase 2)  
**Localização**: `../Oracle/data/demo_dados_r.csv`

**Variáveis:**
- 🌡️ **Temperatura** (°C)
- 💧 **Umidade do Solo** (%)
- 🧪 **pH do Solo**
- 🌧️ **Precipitação** (mm)
- 🌫️ **Umidade do Ar** (%)
- 📊 **Pressão Atmosférica** (hPa)
- 🌿 **NPK** (Nitrogênio, Fósforo, Potássio)
- 📈 **Produtividade** (%)
- 🌾 **Cultura** (Banana, Milho, etc.)

---

## 🚀 Como Executar

### 1. Instalar Dependências

```powershell
cd Fase3\MachineLearning
pip install -r requirements.txt
```

### 2. Executar Análise

```powershell
python analise_ml_farmtech.py
```

### 3. Visualizar Resultados

Os gráficos serão salvos automaticamente na pasta `graficos/`:
- `01_distribuicao_culturas.png`
- `02_temp_vs_umidade.png`
- `03_boxplot_variaveis.png`
- `04_matriz_correlacao.png`
- `05_produtividade_cultura.png`
- `06_comparacao_modelos.png`
- `07_matriz_confusao.png`

---

## 🤖 Modelos Implementados

1. **Regressão Logística** - Modelo linear probabilístico
2. **K-Nearest Neighbors (KNN)** - Classificação por proximidade
3. **Support Vector Machine (SVM)** - Kernel RBF para dados não-lineares
4. **Decision Tree** - Árvore de decisão
5. **Random Forest** - Ensemble de árvores de decisão

---

## 📈 Métricas de Avaliação

- **Acurácia**: Percentual de predições corretas
- **Precision**: Precisão por classe
- **Recall**: Taxa de recuperação
- **F1-Score**: Média harmônica de precisão e recall
- **Matriz de Confusão**: Visualização de erros de classificação

---

## 🌱 Principais Insights

### Perfil Ideal por Cultura

**🍌 Banana:**
- Temperatura: 25-30°C
- Umidade do Solo: 45-55%
- pH: 6.3-6.8
- Alta umidade do ar
- Baixa tolerância ao frio

**🌽 Milho:**
- Temperatura: 28-35°C
- Umidade do Solo: 35-50%
- pH: 6.0-7.0
- Tolera maior variação climática
- Requer NPK balanceado

### Variáveis Mais Importantes

1. **Temperatura** - Fator determinante para cada cultura
2. **Umidade do Solo** - Impacto direto na produtividade
3. **pH** - Define viabilidade de nutrientes
4. **NPK** - Essencial para crescimento saudável

---

## 📊 Estrutura de Arquivos

```
MachineLearning/
├── analise_ml_farmtech.py      # Script principal de análise
├── requirements.txt             # Dependências Python
├── atividade                    # Descrição da atividade
├── README.md                    # Esta documentação
└── graficos/                    # Gráficos gerados (criado automaticamente)
    ├── 01_distribuicao_culturas.png
    ├── 02_temp_vs_umidade.png
    ├── 03_boxplot_variaveis.png
    ├── 04_matriz_correlacao.png
    ├── 05_produtividade_cultura.png
    ├── 06_comparacao_modelos.png
    └── 07_matriz_confusao.png
```

---

## 🔧 Tecnologias Utilizadas

- **Python 3.8+**
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Matplotlib** - Visualização de dados
- **Seaborn** - Gráficos estatísticos
- **Scikit-learn** - Machine Learning

---

## 🎓 Aplicação Prática

Este modelo pode ser integrado ao sistema FarmTech Solutions para:
- ✅ Recomendar culturas ideais baseadas em condições climáticas
- ✅ Prever produtividade esperada
- ✅ Otimizar decisões de plantio
- ✅ Alertar sobre condições adversas
- ✅ Maximizar retorno financeiro

---

## 👥 Equipe FarmTech Solutions

Phellype Massarente • Carlos Costato • Cesar Azeredo

---

## 📄 Licença

MIT License
