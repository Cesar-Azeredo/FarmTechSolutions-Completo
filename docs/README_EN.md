# 🌾 FarmTech Solutions
**Intelligent Agriculture System with IoT, Python, R, and Oracle**

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![R](https://img.shields.io/badge/R-4.0%2B-lightblue)

---

## 📋 About the Project

FarmTech Solutions is a startup focused on **digital agriculture**, combining technology, innovation, and sustainability to optimize crop cultivation and agricultural management processes.

The system is divided into **three main phases**:
- 🌱 **Phase 1:** Crop management and agricultural data analysis.
- 🤖 **Phase 2:** Development of a **smart irrigation system with IoT (ESP32)** and integration with Oracle database, statistical analysis, and real data simulation.
- 📊 **Phase 3:** Interactive dashboard with Oracle Database integration for real-time agricultural data visualization.

The goal is to demonstrate the potential of precision agriculture and the use of IoT, AI, and data analysis to improve productivity and efficiency in agribusiness.

---

## 📂 Project Structure

### 🌱 Phase 1 – Crop Management and Data Analysis

#### 📘 Introduction

In this first phase, the **FarmTech Solutions** team began developing an application in **Python** to support a farm transitioning to **Digital Agriculture**, aiming to increase productivity and input control.

#### 🧩 Main Features

- **Support for 2 types of agricultural crops** chosen by the team.
- **Planting area calculation**, allowing different geometric shapes (rectangle, trapezoid, circle, etc.).
- **Input management calculation**, such as fertilizers, herbicides, and insecticides, considering area and applied quantity.
- **Data structures with vectors** to store and manipulate crop information.
- **Interactive menu** with operations:
  - Data entry
  - Data output (terminal reports)
  - Update and delete records
  - Application termination option
- **Use of loops and conditional structures** for logical flow and calculation repetition.

#### 🧮 Integration with R

After data collection and calculation, an application in **R** performs basic statistical analyses:
- Means, standard deviations, and dispersion
- Graphical visualizations
- Optional integration with public weather API (Open-Meteo) for climate analysis

#### 🌦️ Going Beyond

Using **R (not Python)**, it's possible to connect to a weather API to collect climate data and display meteorological information directly in the terminal, promoting integration between agricultural data and environmental variables.

---

### 🤖 Phase 2 – IoT and Integrated Systems

#### 📘 Introduction

**Phase 2** advances to the practical application of digital agriculture, focusing on **IoT and agricultural automation**.
The team developed a **smart irrigation system** capable of monitoring soil variables and automatically deciding when to irrigate a plantation.

#### ⚙️ Wokwi Simulation Walkthrough (`Fase2/SimulacaoWokwi/`)

Based on agricultural environment simulation, the following sensors and actuators were implemented:

- **Buttons (3)** representing **Nitrogen (N)**, **Phosphorus (P)**, and **Potassium (K)** sensors.
- **LDR Sensor (Light Dependent Resistor)** simulating **soil pH**, ranging from 0 to 14.
- **DHT22 Sensor** representing **soil moisture** (replacing the actual moisture sensor).
- **Blue Relay** representing a real **irrigation pump**, automatically controlled.

#### 💧 Irrigation Logic

The system monitors in real-time the levels of N, P, K, pH, and moisture.
Based on this data, the ESP32 decides whether irrigation should be activated, simulating the actual operation of a digital farm.
The irrigation logic varies according to the agricultural crop chosen by the team.

#### 🌐 Going Beyond – Integration with Python and R

- **Integration with weather API (OpenWeather):** allows rain prediction and automatic irrigation adjustment.
- **Reading via Serial Monitor:** allows manual data input in the Wokwi simulator during execution.
- **Statistical analysis in R:** optionally, the system can use R to decide when to activate the irrigation pump based on climate and nutritional variables.

This stage promotes integration between **sensing, IoT, Data Science, and agricultural automation**, reinforcing the concept of **smart farming**.

---

### 🏗️ Agricultural Management System (`Fase2/SistemaGestaoAgricola/`)

#### 📘 Context

**Agribusiness** is a sector that encompasses all activities related to the production, commercialization, and distribution of agricultural products — being one of the pillars of the Brazilian economy.
The FarmTech Solutions agricultural management system was developed to integrate **operational, environmental, and financial data**, promoting **data-driven decision making**.

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
- **CONAB** – National Supply Company
- **IBGE** – Brazilian Institute of Geography and Statistics
- **MAPA** – Ministry of Agriculture
- **EMBRAPA** – Brazilian Agricultural Research Corporation
- **CNA Brasil** – Agriculture and Livestock Confederation

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

### 📊 Phase 3 – Dashboard and Oracle Integration

#### 📘 Introduction

**Phase 3** completes the agricultural digitalization cycle with the implementation of an **interactive dashboard** developed in **Python/Streamlit** integrated with **Oracle Database**.

#### 🎯 Features

- **Real-time dashboard** with visualizations of:
  - Soil moisture levels, pH, nutrients (N, P, K)
  - Climate data (temperature, air humidity, precipitation, wind, pressure)
  - Irrigation status and productivity
- **Integration with Oracle Database** through the `oracledb` driver
- **Automatic data normalization** for scale adjustment
- **Irrigation suggestions** based on climate and soil conditions
- **Interactive charts** with Plotly
- **Validation and data export scripts**

#### 📁 Structure

```
Fase3/
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

#### 🚀 How to Run

```powershell
cd Fase3
pip install -r requirements.txt
streamlit run scripts/dashboard.py
```

---

## 🛠️ Technologies Used

- **Python 3.8+** → Crop management, analysis, and backend
- **R 4.0+** → Statistical analysis and visualizations
- **C++/Arduino** → ESP32 firmware
- **Oracle Database 19c** → Database
- **Streamlit** → Interactive dashboard (Phase 3)
- **Plotly** → Data visualizations (Phase 3)
- **ESP32** → IoT microcontroller
- **Wokwi** → Hardware simulation

---

## 🚀 How to Run

### ✅ Complete Validation
```powershell
cd testes
python teste_completo.py
```

### 🐍 Phase 1 - Python App
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

### 🤖 Phase 2 - Wokwi Simulation Walkthrough
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
cd Fase3
pip install -r requirements.txt
streamlit run scripts\dashboard.py
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
Phellype Massarente • Carlos Costato • Cesar Azeredo

## 📄 License
MIT
