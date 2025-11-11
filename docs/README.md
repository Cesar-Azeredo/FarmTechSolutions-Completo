# 🌾 FarmTech Solutions

**Sistema de Agricultura Inteligente com IoT, Python, R e Oracle**

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![R](https://img.shields.io/badge/R-4.0%2B-lightblue)

---

## 📋 Sobre o Projeto

FarmTech Solutions é uma startup voltada à **agricultura digital**, unindo tecnologia, inovação e sustentabilidade para otimizar os processos de cultivo e gestão agrícola.

O sistema é dividido em **três fases principais**:

- 🌱 **Fase 1:** Gestão de cultivos e análise de dados agrícolas
- 🤖 **Fase 2:** Sistema de irrigação inteligente com IoT (ESP32), integração com Oracle Database e análise estatística
- 📊 **Fase 3:** Dashboard interativo e modelos de Machine Learning para predição de culturas

O objetivo é demonstrar o potencial da agricultura de precisão através do uso de IoT, IA e análise de dados para aprimorar a produtividade e eficiência no agronegócio.

---

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Estrutura do Projeto](#-estrutura-do-projeto)
  - [Fase 1 – Gestão de Cultivos e Análise de Dados](#-fase-1--gestão-de-cultivos-e-análise-de-dados)
  - [Fase 2 – IoT e Sistemas Integrados](#-fase-2--iot-e-sistemas-integrados)
  - [Fase 3 – Dashboard, Machine Learning e Integração Oracle](#-fase-3--dashboard-machine-learning-e-integração-oracle)
- [Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [Como Executar](#-como-executar)
- [Validação e Testes](#-validação-e-testes)
- [Documentação](#-documentação)
- [Autores](#-autores)
- [Licença](#-licença)

---

<!-- 
## 📸 Demonstração

> 💡 **Dica:** Adicione screenshots do dashboard, simulação Wokwi e análises de ML aqui para melhor visualização do projeto.

![Dashboard](docs/screenshots/dashboard.png)
![Wokwi Simulation](docs/screenshots/wokwi.png)
![ML Analysis](docs/screenshots/ml_analysis.png)
-->

---

## 📂 Estrutura do Projeto

### 🌱 Fase 1 – Gestão de Cultivos e Análise de Dados

#### 📘 Introdução

Nesta primeira fase, a equipe da **FarmTech Solutions** desenvolveu uma aplicação em **Python** para apoiar fazendas em transição para a **Agricultura Digital**, visando aumentar produtividade e controle de insumos.

#### 🧩 Funcionalidades Principais

- **Suporte a 2 tipos de culturas agrícolas** escolhidas pelo grupo
- **Cálculo da área de plantio** com diferentes figuras geométricas (retângulo, trapézio, círculo)
- **Cálculo do manejo de insumos** (fertilizantes, herbicidas, inseticidas) considerando área e quantidade aplicada
- **Estruturas de dados com vetores** para armazenar e manipular informações das culturas
- **Menu interativo** com operações de:
  - Entrada de dados
  - Saída de dados (relatórios no terminal)
  - Atualização e exclusão de registros
  - Opção de encerramento da aplicação
- **Uso de loops e estruturas condicionais** para fluxo lógico e repetição de cálculos

#### 🧮 Integração com R

Após a coleta e cálculo de dados, uma aplicação em **R** realiza análises estatísticas:

- Médias, desvios-padrão e dispersão
- Visualizações gráficas
- Integração opcional com API meteorológica pública ([Open-Meteo](https://open-meteo.com)) para análise climática

#### 🌦️ Ir Além

Usando **R**, é possível conectar-se a APIs meteorológicas para coletar dados climáticos e exibir informações diretamente no terminal, integrando dados agrícolas e variáveis ambientais.

---

### 🤖 Fase 2 – IoT e Sistemas Integrados

#### 📘 Introdução

A **Fase 2** avança para a aplicação prática da agricultura digital, com foco em **IoT e automação agrícola**. A equipe desenvolveu um **sistema de irrigação inteligente** capaz de monitorar variáveis do solo e decidir automaticamente quando irrigar.

#### ⚙️ Simulação Wokwi (`Fase2/SimulacaoWokwi/`)

Com base na simulação do ambiente agrícola, foram implementados os seguintes sensores e atuadores:

- **Botões (3)** representando sensores de **Nitrogênio (N)**, **Fósforo (P)** e **Potássio (K)**
- **Sensor LDR (Light Dependent Resistor)** simulando o **pH do solo**, variando entre 0 e 14
- **Sensor DHT22** representando a **umidade do solo** (substituindo o sensor real de umidade)
- **Relé azul** representando uma **bomba de irrigação** real, controlada automaticamente

#### 💧 Lógica de Irrigação

O sistema monitora em tempo real os níveis de N, P, K, pH e umidade. Com base nesses dados, o ESP32 decide se a irrigação deve ser ativada, simulando a operação real de uma lavoura digital. A lógica de irrigação varia conforme a cultura agrícola escolhida.

#### 🌐 Ir Além – Integração com Python e R

- **Integração com API meteorológica ([OpenWeather](https://openweathermap.org)):** permite prever chuva e ajustar a irrigação automaticamente
- **Leitura via Serial Monitor:** permite inserir dados manuais no simulador Wokwi durante execução
- **Análise estatística em R:** o sistema pode usar R para decidir quando ativar a bomba de irrigação com base em variáveis climáticas e nutricionais

Esta etapa promove a integração entre **sensoriamento, IoT, Data Science e automação agrícola**, reforçando o conceito de **fazenda inteligente**.

---

### 🏗️ Sistema de Gestão Agrícola (`Fase2/SistemaGestaoAgricola/`)

#### 📘 Contexto

O **agronegócio** abrange todas as atividades ligadas à produção, comercialização e distribuição de produtos agrícolas, sendo um dos pilares da economia brasileira. O sistema de gestão agrícola da FarmTech Solutions foi desenvolvido para integrar **dados operacionais, ambientais e financeiros**, promovendo **tomada de decisão baseada em dados**.

#### ⚙️ Funcionalidades

- **Arquitetura modular em Python**
  - `cultivo_manager`: gerenciamento de culturas agrícolas
  - `sensor_monitor`: integração com sensores físicos ou simulados
  - `irrigacao_controller`: controle automatizado de irrigação
  - `estoque_manager`: controle de insumos e recursos agrícolas
- **Oracle Database 19c** para armazenamento centralizado
- **Persistência em JSON** para fácil leitura e backup
- **Testes automatizados** para validar módulos, entradas e saídas
- **Análise de consistência dos dados** e interface clara no terminal

#### 🌱 Contextualização do Agronegócio

O sistema está inserido em um cenário de **transformação digital no agro**, caracterizado por:

- Segurança alimentar e sustentabilidade
- Inovação com IoT e análise de dados
- Redução de desperdícios e otimização de recursos hídricos
- Uso de **agrotechs** como agentes de digitalização do campo

---

### 📊 Análise R (`Fase2/AnaliseR/`)

#### 📘 Contexto

Nesta etapa, o grupo trabalha com **dados reais do agronegócio brasileiro**, obtidos de fontes públicas como:

- **[CONAB](https://www.conab.gov.br)** (Companhia Nacional de Abastecimento)
- **[IBGE](https://www.ibge.gov.br)** (Instituto Brasileiro de Geografia e Estatística)
- **[MAPA](https://www.gov.br/agricultura)** (Ministério da Agricultura)
- **[EMBRAPA](https://www.embrapa.br)** (Empresa Brasileira de Pesquisa Agropecuária)
- **[CNA Brasil](https://www.cnabrasil.org.br)** (Confederação da Agricultura e Pecuária)

#### 📈 Entregáveis

- **Base de dados em Excel** com:
  - 30 linhas e 4 colunas
  - Variável quantitativa discreta
  - Variável quantitativa contínua
  - Variável qualitativa nominal
  - Variável qualitativa ordinal
- **Análise exploratória em R** contendo:
  - Medidas de tendência central
  - Medidas de dispersão
  - Medidas separatrizes
  - Análise gráfica de variáveis quantitativas e qualitativas

#### 🌾 Objetivo

Com base nessas análises, a equipe da FarmTech Solutions busca:

- Entender padrões e comportamentos produtivos regionais
- Avaliar indicadores de produtividade e sustentabilidade
- Consolidar um painel estatístico com dados de 35 propriedades por região

---

### 📊 Fase 3 – Dashboard, Machine Learning e Integração Oracle

#### 📘 Introdução

A **Fase 3** completa o ciclo de digitalização agrícola com a implementação de um **dashboard interativo** desenvolvido em **Python/Streamlit** integrado ao banco de dados **Oracle Database**, além de análises avançadas de **Machine Learning** para predição de culturas ideais.

---

#### 🎯 Dashboard e Integração Oracle

**Funcionalidades:**

- **Dashboard em tempo real** com visualizações de:
  - Níveis de umidade do solo, pH, nutrientes (N, P, K)
  - Dados climáticos (temperatura, umidade do ar, precipitação, vento, pressão)
  - Status de irrigação e produtividade
- **Integração com Oracle Database** através do driver `oracledb`
- **Normalização automática de dados** para ajuste de escalas
- **Sugestões de irrigação** baseadas em condições climáticas e do solo
- **Gráficos interativos** com Plotly
- **Scripts de validação e exportação** de dados

**Estrutura:**

```
Fase3/Oracle/
├── data/                    # Dados CSV para testes
├── docs/                    # Documentação técnica
├── scripts/                 # Scripts Python
│   ├── dashboard.py         # Dashboard Streamlit principal
│   ├── test_connection.py   # Teste de conexão Oracle
│   ├── check_normalization.py
│   ├── data_load_test.py
│   └── export_evidence.py
├── sql/                     # Scripts SQL
├── requirements.txt         # Dependências Python
└── start_dashboard.bat      # Inicializador Windows
```

---

#### 🤖 Machine Learning - Análise Preditiva de Culturas

**Objetivo:**  
Desenvolver modelos de Machine Learning para **predizer a cultura agrícola ideal** com base em condições climáticas e de solo, promovendo decisões baseadas em dados e otimização da produtividade.

**Metodologia:**

1. **Análise Exploratória de Dados (EDA)**
   - Familiarização com dataset de sensores IoT
   - Verificação de qualidade dos dados (nulos, duplicados, outliers)
   - Estatísticas descritivas completas

2. **Análise Descritiva Visual**
   - Mínimo de 5 gráficos analíticos:
     - Distribuição de culturas
     - Temperatura vs Umidade do solo
     - Boxplots de variáveis climáticas
     - Matriz de correlação
     - Produtividade por cultura
     - Comparação de modelos ML
     - Matriz de confusão

3. **Perfil Ideal de Solo/Clima**
   - Análise estatística de condições ótimas por cultura
   - Comparação entre diferentes culturas (Banana, Milho, etc.)
   - Identificação de padrões climáticos e nutricionais

4. **Desenvolvimento de 5 Modelos Preditivos**
   - **Regressão Logística:** Baseline linear
   - **K-Nearest Neighbors (KNN):** Classificação por proximidade
   - **Support Vector Machine (SVM):** Kernel RBF para relações não-lineares
   - **Decision Tree:** Modelo interpretável baseado em regras
   - **Random Forest:** Ensemble robusto

5. **Avaliação e Comparação**
   - Métricas: Accuracy, Precision, Recall, F1-Score
   - Matriz de confusão
   - Validação com dados de teste (80/20 split)
   - Identificação do melhor modelo

**Resultados Esperados:**

- Acurácia superior a 50% (baseline aleatório)
- Identificação de features mais relevantes (temperatura, umidade, pH, NPK)
- Sistema de recomendação de culturas baseado em ML
- Insights sobre perfis climáticos ideais

**Estrutura:**

```
Fase3/MachineLearning/
├── Analise_Produtos_Agricolas.ipynb  # Notebook Jupyter completo
├── Atividade_Cap10_produtos_agricolas.csv  # Dataset
├── requirements.txt                   # Dependências Python
└── atividade                          # Especificações do projeto
```

**Como Executar:**

```powershell
cd Fase3\MachineLearning
pip install -r requirements.txt
jupyter notebook Analise_Produtos_Agricolas.ipynb
```

**Bibliotecas Utilizadas:**

- `pandas`, `numpy`: Manipulação de dados
- `matplotlib`, `seaborn`: Visualizações
- `scikit-learn`: Modelos de ML, pré-processamento e métricas

---

#### 🚀 Como Executar a Fase 3 Completa

**Dashboard Oracle:**

```powershell
cd Fase3\Oracle
pip install -r requirements.txt
streamlit run scripts\dashboard.py
```

**Machine Learning:**

```powershell
cd Fase3\MachineLearning
pip install -r requirements.txt
jupyter notebook Analise_Produtos_Agricolas.ipynb
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+:** Gestão de cultivos, análise, backend e Machine Learning
- **R 4.0+:** Análise estatística e visualizações
- **C++/Arduino:** Firmware ESP32
- **Oracle Database 19c:** Banco de dados
- **Streamlit:** Dashboard interativo (Fase 3)
- **Plotly:** Visualizações de dados (Fase 3)
- **scikit-learn:** Modelos de Machine Learning (Fase 3)
- **Jupyter Notebook:** Análise ML interativa (Fase 3)
- **ESP32:** Microcontrolador IoT
- **Wokwi:** Simulação de hardware

---

## 🚀 Como Executar

### ✅ Validação Completa

```powershell
cd testes
python teste_completo.py
```

### 🐍 Fase 1 - Aplicação Python

```powershell
cd Fase1\python_app
python main.py
```

### 🧮 Fase 1 - Análise R

```powershell
cd Fase1\r_app
Rscript analise.R
Rscript clima.R banana
```

### 🤖 Fase 2 - Simulação Wokwi

1. Acesse [wokwi.com](https://wokwi.com)
2. Carregue `Fase2/SimulacaoWokwi/config/diagram.json`
3. Cole o código de `Fase2/SimulacaoWokwi/FarmTech.ino`
4. Execute a simulação

### 💼 Fase 2 - Sistema de Gestão

```powershell
cd Fase2\SistemaGestaoAgricola
python main.py
```

### 📊 Fase 3 - Dashboard Oracle/Streamlit

```powershell
cd Fase3\Oracle
pip install -r requirements.txt
streamlit run scripts\dashboard.py
```

### 🤖 Fase 3 - Machine Learning

```powershell
cd Fase3\MachineLearning
pip install -r requirements.txt
jupyter notebook Analise_Produtos_Agricolas.ipynb
```

---

## 🧪 Validação e Testes

O projeto inclui um sistema completo de validação automática em `testes/teste_completo.py` que verifica:

- ✅ Sintaxe e execução de todas as aplicações Python
- ✅ Presença e estrutura de todos os componentes
- ✅ Validação de configurações ESP32 e Wokwi
- ✅ Verificação de scripts R e datasets

---

## 📚 Documentação

A documentação técnica completa está disponível na pasta `docs/`:

- 📘 Guia de instalação
- 📗 Instruções de uso
- 📖 Especificações técnicas

---

## 👥 Autores

**Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo**

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## 🎓 Sobre Este Projeto

Este projeto foi desenvolvido como parte do programa acadêmico de **Engenharia de Software e Ciência de Dados**, demonstrando a aplicação prática de tecnologias modernas (IoT, Machine Learning, Cloud Database) no contexto do agronegócio brasileiro. O objetivo é evidenciar como a integração entre sensoriamento, análise de dados e automação pode transformar a agricultura tradicional em um modelo digital, sustentável e baseado em decisões orientadas por dados.

**FarmTech Solutions** representa a convergência entre inovação tecnológica e agricultura de precisão. 🌾🚀
