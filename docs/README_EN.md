# 🌾 FarmTech Solutions

**Intelligent Agriculture System with IoT, Python, R, and Oracle**

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![R](https://img.shields.io/badge/R-4.0%2B-lightblue)

---

## 📋 About the Project

FarmTech Solutions is a startup focused on **digital agriculture**, combining technology, innovation, and sustainability to optimize crop cultivation and agricultural management processes.

The system is divided into **four main phases**:

- 🌱 **Phase 1:** Crop management and agricultural data analysis
- 🤖 **Phase 2:** Smart irrigation system with IoT (ESP32), Oracle Database integration, and statistical analysis
- 📊 **Phase 3:** Interactive dashboard and Machine Learning models for crop prediction
- 🧠 **Phase 4:** Wheat grain classification and intelligent agricultural forecasting with supervised regression

The goal is to demonstrate the potential of precision agriculture through IoT, AI, and data analysis to improve productivity and efficiency in agribusiness.

---

## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Project Structure](#-project-structure)
  - [Phase 1 – Crop Management and Data Analysis](#-phase-1--crop-management-and-data-analysis)
  - [Phase 2 – IoT and Integrated Systems](#-phase-2--iot-and-integrated-systems)
  - [Phase 3 – Dashboard, Machine Learning, and Oracle Integration](#-phase-3--dashboard-machine-learning-and-oracle-integration)
  - [Phase 4 – Intelligent Forecasting and Grain Classification](#-phase-4--intelligent-forecasting-and-grain-classification)
- [Technologies Used](#️-technologies-used)
- [How to Run](#-how-to-run)
- [Validation and Testing](#-validation-and-testing)
- [Documentation](#-documentation)
- [Authors](#-authors)
- [License](#-license)

---

<!-- 
## 📸 Demonstration

> 💡 **Tip:** Add screenshots of the dashboard, Wokwi simulation, and ML analyses here for better project visualization.

![Dashboard](docs/screenshots/dashboard.png)
![Wokwi Simulation](docs/screenshots/wokwi.png)
![ML Analysis](docs/screenshots/ml_analysis.png)
-->

---

## 📂 Project Structure

### 🌱 Phase 1 – Crop Management and Data Analysis

#### 📘 Introduction

In this first phase, the **FarmTech Solutions** team developed an application in **Python** to support farms transitioning to **Digital Agriculture**, aiming to increase productivity and input control.

#### 🧩 Main Features

- **Support for 2 types of agricultural crops** chosen by the team
- **Planting area calculation** with different geometric shapes (rectangle, trapezoid, circle)
- **Input management calculation** (fertilizers, herbicides, insecticides) considering area and applied quantity
- **Data structures with vectors** to store and manipulate crop information
- **Interactive menu** with operations:
  - Data entry
  - Data output (terminal reports)
  - Update and delete records
  - Application termination option
- **Use of loops and conditional structures** for logical flow and calculation repetition

#### 🧮 Integration with R

After data collection and calculation, an application in **R** performs statistical analyses:

- Means, standard deviations, and dispersion
- Graphical visualizations
- Optional integration with public weather API ([Open-Meteo](https://open-meteo.com)) for climate analysis

#### 🌦️ Going Beyond

Using **R**, it's possible to connect to weather APIs to collect climate data and display information directly in the terminal, integrating agricultural and environmental data.

---

### 🤖 Phase 2 – IoT and Integrated Systems

#### 📘 Introduction

**Phase 2** advances to the practical application of digital agriculture, focusing on **IoT and agricultural automation**. The team developed a **smart irrigation system** capable of monitoring soil variables and automatically deciding when to irrigate.

#### ⚙️ Wokwi Simulation (`Fase2/SimulacaoWokwi/`)

Based on agricultural environment simulation, the following sensors and actuators were implemented:

- **Buttons (3)** representing **Nitrogen (N)**, **Phosphorus (P)**, and **Potassium (K)** sensors
- **LDR Sensor (Light Dependent Resistor)** simulating **soil pH**, ranging from 0 to 14
- **DHT22 Sensor** representing **soil moisture** (replacing the actual moisture sensor)
- **Blue Relay** representing a real **irrigation pump**, automatically controlled

#### 💧 Irrigation Logic

The system monitors in real-time the levels of N, P, K, pH, and moisture. Based on this data, the ESP32 decides whether irrigation should be activated, simulating the actual operation of a digital farm. The irrigation logic varies according to the agricultural crop chosen.

#### 🌐 Going Beyond – Integration with Python and R

- **Integration with weather API ([OpenWeather](https://openweathermap.org)):** allows rain prediction and automatic irrigation adjustment
- **Reading via Serial Monitor:** allows manual data input in the Wokwi simulator during execution
- **Statistical analysis in R:** the system can use R to decide when to activate the irrigation pump based on climate and nutritional variables

This stage promotes integration between **sensing, IoT, Data Science, and agricultural automation**, reinforcing the concept of **smart farming**.

---

### 🏗️ Agricultural Management System (`Fase2/SistemaGestaoAgricola/`)

#### 📘 Context

**Agribusiness** encompasses all activities related to the production, commercialization, and distribution of agricultural products, being one of the pillars of the Brazilian economy. The FarmTech Solutions agricultural management system was developed to integrate **operational, environmental, and financial data**, promoting **data-driven decision making**.

#### ⚙️ Features

- **Modular architecture in Python**
  - `cultivo_manager`: agricultural crop management
  - `sensor_monitor`: integration with physical or simulated sensors
  - `irrigacao_controller`: automated irrigation control
  - `estoque_manager`: input and agricultural resource control
- **Oracle Database 19c** for centralized storage
- **JSON persistence** for easy reading and backup
- **Automated tests** to validate modules, inputs, and outputs
- **Data consistency analysis** and clear terminal interface

#### 🌱 Agribusiness Context

The system is inserted within a scenario of **digital transformation in agriculture**, characterized by:

- Food security and sustainability
- Innovation with IoT and data analysis
- Waste reduction and water resource optimization
- Use of **agrotechs** as agents of field digitalization

---

### 📊 R Analysis (`Fase2/AnaliseR/`)

#### 📘 Context

At this stage, the team works with **real data from Brazilian agribusiness**, obtained from public sources such as:

- **[CONAB](https://www.conab.gov.br)** (National Supply Company)
- **[IBGE](https://www.ibge.gov.br)** (Brazilian Institute of Geography and Statistics)
- **[MAPA](https://www.gov.br/agriculture)** (Ministry of Agriculture)
- **[EMBRAPA](https://www.embrapa.br)** (Brazilian Agricultural Research Corporation)
- **[CNA Brasil](https://www.cnabrasil.org.br)** (Agriculture and Livestock Confederation)

#### 📈 Deliverables

- **Excel database** with:
  - 30 rows and 4 columns
  - Discrete quantitative variable
  - Continuous quantitative variable
  - Nominal qualitative variable
  - Ordinal qualitative variable
- **Exploratory analysis in R** containing:
  - Measures of central tendency
  - Measures of dispersion
  - Separatrix measures
  - Graphical analysis of quantitative and qualitative variables

#### 🌾 Objective

Based on these analyses, the FarmTech Solutions team seeks to:

- Understand regional productive patterns and behaviors
- Evaluate productivity and sustainability indicators
- Consolidate a statistical panel with data from 35 properties per region

---

### 📊 Phase 3 – Dashboard, Machine Learning, and Oracle Integration

#### 📘 Introduction

**Phase 3** completes the agricultural digitalization cycle with the implementation of an **interactive dashboard** developed in **Python/Streamlit** integrated with **Oracle Database**, plus advanced **Machine Learning** analyses for predicting ideal crops.

---

#### 🎯 Dashboard and Oracle Integration

**Features:**

- **Real-time dashboard** with visualizations of:
  - Soil moisture levels, pH, nutrients (N, P, K)
  - Climate data (temperature, air humidity, precipitation, wind, pressure)
  - Irrigation status and productivity
- **Integration with Oracle Database** through the `oracledb` driver
- **Automatic data normalization** for scale adjustment
- **Irrigation suggestions** based on climate and soil conditions
- **Interactive charts** with Plotly
- **Validation and data export scripts**

**Structure:**

```
Fase3/Oracle/
├── data/                    # CSV data for testing
├── docs/                    # Technical documentation
├── scripts/                 # Python scripts
│   ├── dashboard.py         # Main Streamlit dashboard
│   ├── test_connection.py   # Oracle connection test
│   ├── check_normalization.py
│   ├── data_load_test.py
│   └── export_evidence.py
├── sql/                     # SQL scripts
├── requirements.txt         # Python dependencies
└── start_dashboard.bat      # Windows launcher
```

---

#### 🤖 Machine Learning - Predictive Crop Analysis

**Objective:**  
Develop Machine Learning models to **predict the ideal agricultural crop** based on climate and soil conditions, promoting data-driven decisions and productivity optimization.

**Methodology:**

1. **Exploratory Data Analysis (EDA)**
   - Familiarization with IoT sensor dataset
   - Data quality verification (nulls, duplicates, outliers)
   - Complete descriptive statistics

2. **Visual Descriptive Analysis**
   - Minimum of 5 analytical charts:
     - Crop distribution
     - Temperature vs Soil moisture
     - Climate variables boxplots
     - Correlation matrix
     - Productivity by crop
     - ML models comparison
     - Confusion matrix

3. **Ideal Soil/Climate Profile**
   - Statistical analysis of optimal conditions per crop
   - Comparison between different crops (Banana, Corn, etc.)
   - Identification of climate and nutritional patterns

4. **Development of 5 Predictive Models**
   - **Logistic Regression:** Linear baseline
   - **K-Nearest Neighbors (KNN):** Proximity-based classification
   - **Support Vector Machine (SVM):** RBF kernel for non-linear relationships
   - **Decision Tree:** Interpretable rule-based model
   - **Random Forest:** Robust ensemble

5. **Evaluation and Comparison**
   - Metrics: Accuracy, Precision, Recall, F1-Score
   - Confusion matrix
   - Validation with test data (80/20 split)
   - Best model identification

**Expected Results:**

- Accuracy above 50% (random baseline)
- Identification of most relevant features (temperature, humidity, pH, NPK)
- ML-based crop recommendation system
- Insights on ideal climate profiles

**Structure:**

```
Fase3/MachineLearning/
├── Analise_Produtos_Agricolas.ipynb  # Complete Jupyter Notebook
├── Atividade_Cap10_produtos_agricolas.csv  # Dataset
├── requirements.txt                   # Python dependencies
└── atividade                          # Project specifications
```

**How to Run:**

```powershell
cd Fase3\MachineLearning
pip install -r requirements.txt
jupyter notebook Analise_Produtos_Agricolas.ipynb
```

**Libraries Used:**

- `pandas`, `numpy`: Data manipulation
- `matplotlib`, `seaborn`: Visualizations
- `scikit-learn`: ML models, preprocessing, and metrics

---

#### 🚀 How to Run Complete Phase 3

**Oracle Dashboard:**

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

### 🧠 Phase 4 – Intelligent Forecasting and Grain Classification

#### 📘 Overview

Phase 4 is implemented in two deliverable folders:
- `Fase4/Sklearn/`: wheat grain classification with CRISP-DM workflow
- `Fase4/Dados/`: intelligent farming assistant with regression pipeline + Streamlit dashboard

#### 🌾 Activity 1 – Wheat Grain Classification (`Fase4/Sklearn/`)

Implemented files:
```
Fase4/Sklearn/
├── wheat_classification.ipynb
└── seeds_dataset.txt
```

What is implemented:
- Exploratory Data Analysis (histograms, boxplots, pairplot, correlation heatmap)
- Data preprocessing and train/test split
- Comparison of multiple classifiers (KNN, SVM, Random Forest, Naive Bayes, Logistic Regression)
- Evaluation with Accuracy, Precision, Recall, F1-score, and confusion matrix
- Hyperparameter optimization with GridSearchCV
- Interpretation and actionable insights

#### 🤖 Activity 2 – Intelligent Agricultural Forecasting (`Fase4/Dados/`)

Implemented files:
```
Fase4/Dados/
├── app.py
├── iot_ingestion.py
├── ml_pipeline.py
├── database/
│   └── farmtech.db
└── logs_irrigacao_api.json
```

What is implemented:
- Regression pipeline with model comparison and metrics (MAE, MSE, RMSE, R²)
- Interactive Streamlit dashboard with:
  - model metrics table
  - correlation charts and trend analysis
  - real-time yield prediction form
  - irrigation/soil management recommendations
- IoT log ingestion into SQLite table (`iot_weather_logs`) for data integration

#### 🚀 How to Run Phase 4

**Grain Classification Notebook:**

```powershell
cd Fase4\Sklearn
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
jupyter notebook wheat_classification.ipynb
```

**Forecasting Dashboard:**

```powershell
cd Fase4\Dados
pip install pandas numpy scikit-learn streamlit plotly
python iot_ingestion.py
streamlit run app.py
```

---

## 🛠️ Technologies Used

- **Python 3.8+:** Crop management, analysis, backend, and Machine Learning
- **R 4.0+:** Statistical analysis and visualizations
- **C++/Arduino:** ESP32 firmware
- **Oracle Database 19c:** Database
- **Streamlit:** Interactive dashboard (Phases 3 and 4)
- **Plotly:** Data visualizations (Phases 3 and 4)
- **scikit-learn:** Machine Learning models (Phases 3 and 4)
- **Jupyter Notebook:** Interactive ML analysis (Phases 3 and 4)
- **ESP32:** IoT microcontroller
- **Wokwi:** Hardware simulation

---

## 🚀 How to Run

### ✅ Complete Validation

```powershell
cd testes
python teste_completo.py
```

### 🐍 Phase 1 - Python Application

```powershell
cd Fase1\python_app
python main.py
```

### 🧮 Phase 1 - R Analysis

```powershell
cd Fase1\r_app
Rscript analise.R
Rscript clima.R banana
```

### 🤖 Phase 2 - Wokwi Simulation

1. Access [wokwi.com](https://wokwi.com)
2. Load `Fase2/SimulacaoWokwi/config/diagram.json`
3. Paste the code from `Fase2/SimulacaoWokwi/FarmTech.ino`
4. Run the simulation

### 💼 Phase 2 - Management System

```powershell
cd Fase2\SistemaGestaoAgricola
python main.py
```

### 📊 Phase 3 - Oracle/Streamlit Dashboard

```powershell
cd Fase3\Oracle
pip install -r requirements.txt
streamlit run scripts\dashboard.py
```

### 🤖 Phase 3 - Machine Learning

```powershell
cd Fase3\MachineLearning
pip install -r requirements.txt
jupyter notebook Analise_Produtos_Agricolas.ipynb
```

### 🧠 Phase 4 - Wheat Grain Classification

```powershell
cd Fase4\Sklearn
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
jupyter notebook wheat_classification.ipynb
```

### 🧠 Phase 4 - Intelligent Forecasting Dashboard

```powershell
cd Fase4\Dados
pip install pandas numpy scikit-learn streamlit plotly
python iot_ingestion.py
streamlit run app.py
```

---

## 🧪 Validation and Testing

The project includes a complete automatic validation system in `testes/teste_completo.py` that verifies:

- ✅ Syntax and execution of all Python applications
- ✅ Presence and structure of all components
- ✅ Validation of ESP32 and Wokwi configurations
- ✅ Verification of R scripts and datasets

---

## 📚 Documentation

Complete technical documentation is available in the `docs/` folder:

- 📘 Installation guide
- 📗 Usage instructions
- 📖 Technical specifications

---

## 👥 Authors

**Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo**

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🎓 About This Project

This project was developed as part of the **Software Engineering and Data Science** academic program, demonstrating the practical application of modern technologies (IoT, Machine Learning, Cloud Database) in the context of Brazilian agribusiness. The goal is to showcase how the integration of sensing, data analysis, and automation can transform traditional agriculture into a digital, sustainable, and data-driven model.

**FarmTech Solutions** represents the convergence of technological innovation and precision agriculture. 🌾🚀
