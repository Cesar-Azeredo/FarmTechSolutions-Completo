# 🌾 FarmTech Solutions# 🌾 FarmTech Solutions# 🌾 FarmTech Solutions# 🌾 FarmTech Solutions



Sistema completo de agricultura de precisão com IoT, análise de dados e automação de irrigação.



[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)Sistema inteligente de agricultura de precisão com IoT, análise de dados e automação.

[![R](https://img.shields.io/badge/R-4.0+-276DC3.svg)](https://www.r-project.org/)

[![ESP32](https://img.shields.io/badge/ESP32-Wokwi-orange.svg)](https://wokwi.com/)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)> **Sistema inteligente de agricultura de precisão** integrando IoT, análise de dados e machine learning para otimização de cultivos agrícolas.> **Sistema inteligente de agricultura de precisão** integrando IoT, análise de dados e machine learning para otimização de cultivos agrícolas.

---

[![R](https://img.shields.io/badge/R-4.0+-276DC3.svg)](https://www.r-project.org/)

## 📖 Sobre o Projeto

[![ESP32](https://img.shields.io/badge/ESP32-IoT-orange.svg)](https://www.espressif.com/)

A **FarmTech Solutions** é uma startup que desenvolve tecnologia para agricultura digital. Este projeto implementa um sistema completo de gestão agrícola que integra:

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

- **Gestão de Cultivos** - Sistema Python para cálculo de área plantada e manejo de insumos

- **Análise Estatística** - Processamento de dados em R com estatísticas e API meteorológica[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

- **IoT ESP32** - Monitoramento de NPK, pH e umidade com irrigação automatizada

- **Sistema de Gestão** - Plataforma completa com banco de dados Oracle---



---[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)



## 👥 Equipe## 📋 Sobre



**Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo**[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)



---Plataforma completa para agricultura inteligente que integra:



## 🎯 Funcionalidades[![ESP32](https://img.shields.io/badge/ESP32-IoT-orange.svg)](https://www.espressif.com/)[![ESP32](https://img.shields.io/badge/ESP32-IoT-orange.svg)](https://www.espressif.com/)



### Fase 1: Gestão de Cultivos e Análise- **IoT com ESP32** - Monitoramento e controle automático de irrigação



#### Python Application- **Análise de Dados** - Processamento estatístico em Python e R

Aplicação completa para gestão de **2 culturas** (Banana e Milho):

- **Gestão Agrícola** - Sistema completo com banco de dados Oracle

- ✅ **Menu interativo** com 5 opções:

  - Entrada de dados------

  - Saída de dados (impressão no terminal)

  - Atualização de dados em posições específicasO sistema monitora NPK, pH do solo e umidade em tempo real, automatizando decisões de irrigação.

  - Deleção de dados

  - Sair do programa



- ✅ **Cálculo de área plantada** com figuras geométricas:---

  - Banana: Retângulo, Trapézio, Círculo

  - Milho: Retângulo, Trapézio, Círculo## 📖 Sobre o Projeto## 📖 Sobre o Projeto



- ✅ **Manejo de insumos**:## 👥 Autores

  - Tipos: Fosfato, Nitrogênio, Potássio, Herbicida, Inseticida

  - Cálculo automático de quantidade necessária (mL, L, kg, g)

  - Exemplo: "Pulverizar 500 mL/metro no café"

**Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo**

- ✅ **Estrutura de dados**:

  - Dados organizados em vetores (listas Python)**FarmTech Solutions** é uma solução completa para **agricultura inteligente**, combinando:**FarmTech Solutions** é uma solução completa para **agricultura inteligente**, combinando:

  - Rotinas de loop e decisão

  - Exportação para CSV---



#### R Statistical Analysis

- 📊 **Estatísticas básicas**: média, mediana, desvio padrão

- 📈 **Análise de distribuição** por tipo geométrico e unidade## 🏗️ Estrutura do Projeto

- 🌦️ **API Meteorológica** (Ir Além): Integração com Open-Meteo para dados climáticos

- 🤖 **IoT & Automação** - Sistema de irrigação inteligente com ESP32- 🤖 **IoT & Automação** - Sistema de irrigação inteligente com ESP32

---

```

### Fase 2: IoT e Automação

FarmTechSolutions-Completo/- 📊 **Análise de Dados** - Processamento estatístico de dados agrícolas- 📊 **Análise de Dados** - Processamento estatístico de dados agrícolas

#### Capítulo 1: Sistema de Irrigação Inteligente (ESP32)

│

**Objetivo**: Monitorar NPK, pH e umidade para controle automático de irrigação.

├── Fase1/                          # Análise de Dados- 🗄️ **Gestão Completa** - Sistema de gerenciamento com banco de dados Oracle- 🗄️ **Gestão Completa** - Sistema de gerenciamento com banco de dados Oracle

**Hardware Simulado no Wokwi**:

- 🟢 **3 Botões Verdes** → Sensores NPK (Nitrogênio, Fósforo, Potássio)│   ├── python_app/                 # Sistema Python de gestão de cultivos

- 💡 **LDR (Fotoresistor)** → Sensor de pH (simula pH de 0-14)

- 🌡️ **DHT22** → Sensor de umidade do solo (simula umidade %)│   └── r_app/                      # Análise estatística em R- 🔬 **Machine Learning** - Modelos preditivos para otimização de cultivos- 🔬 **Machine Learning** - Modelos preditivos para otimização de cultivos

- 🔵 **Relé Azul** → Bomba d'água (irrigação automática)

│

**Lógica de Irrigação**:

```├── Fase2/                          # IoT e Sistemas Integrados

Irrigar SE:

  - NPK adequado (botões pressionados conforme cultura)│   ├── Cap 1/                      # Sistema IoT ESP32 + Sensores

  - pH entre 5.5 e 7.5

  - Umidade < 40%│   ├── Cap 6/                      # Sistema de Gestão com OracleO sistema monitora **níveis de NPK, pH do solo e umidade** em tempo real, tomando decisões automáticas de irrigação.O sistema monitora **níveis de NPK, pH do solo e umidade** em tempo real, tomando decisões automáticas de irrigação baseadas em dados científicos.

```

│   └── Cap 7/                      # Análise de dados reais (CONAB/IBGE)

**Culturas Suportadas**:

- 🍌 **Banana**: N=15g/m², P=10g/m², K=20g/m²│

- 🌽 **Milho**: N=12g/m², P=8g/m², K=10g/m²

├── testes/                         # Scripts de validação automática

**Projetos Ir Além**:

- 🐍 **Python + API**: Integração com OpenWeather para prever chuva e ajustar irrigação└── docs/                           # Documentação técnica------

- 📊 **R + Análise**: Decisão estatística de irrigação usando Data Science

```

#### Capítulo 6: Sistema de Gestão Agrícola

Sistema Python modular com Oracle Database:

- `cultivo_manager.py` - CRUD de cultivos

- `sensor_monitor.py` - Monitoramento de sensores---

- `irrigacao_controller.py` - Controle de irrigação

- `estoque_manager.py` - Gestão de insumos## 👥 Autores## 👥 Autores

- `database.py` - Integração Oracle

- `file_utils.py` - Persistência JSON## 🚀 Funcionalidades



#### Capítulo 7: Análise de Dados Reais

- Dados CONAB/IBGE de produção de banana e milho (2024)

- 35 registros de propriedades por região### Fase 1: Análise de Dados

- Análise estatística completa em R

**Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo****Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo**

---

**Python Application**

## 🏗️ Estrutura do Projeto

- Cadastro interativo de cultivos (Banana e Milho)

```

FarmTechSolutions-Completo/- Cálculo automático de área plantada

│

├── Fase1/                          # Fase 1: Gestão e Análise- Estimativa de insumos por m²------

│   ├── python_app/

│   │   ├── main.py                 # App principal (681 linhas)- Exportação para CSV

│   │   ├── gerador_exemplos.py    # Gerador de dados de teste

│   │   ├── banana.csv              # Dataset banana (20 registros)

│   │   └── milho.csv               # Dataset milho (20 registros)

│   └── r_app/**R Statistical Analysis**

│       ├── analise.R               # Análise estatística

│       └── clima.R                 # API meteorológica (Ir Além)- Análise estatística completa## 🚀 Features## 🚀 Features

│

├── Fase2/                          # Fase 2: IoT e Sistemas- Visualizações (histogramas, boxplots)

│   ├── Cap 1/                      # IoT ESP32

│   │   ├── FarmTech.ino           # Código Arduino (854 linhas)- Correlação entre variáveis

│   │   ├── src/main.cpp           # Código C++ PlatformIO

│   │   ├── config/

│   │   │   └── diagram.json       # Configuração Wokwi

│   │   └── ir_alem/               # Projetos Ir Além### Fase 2: IoT e Gestão### 🌱 Fase 1: Análise e Predição de Dados### 🌱 Fase 1: Análise e Predição de Dados

│   │       ├── iralempython/      # Python + API OpenWeather

│   │       └── iralemR/           # R + Análise Estatística

│   │

│   ├── Cap 6/                     # Sistema de Gestão**ESP32 IoT (Cap 1)**

│   │   ├── main.py

│   │   ├── modules/               # 6 módulos Python- Sensores: NPK, pH, temperatura, umidade

│   │   ├── data/                  # JSON (cultivos, sensores, etc)

│   │   └── sql/                   # Scripts Oracle- Controle automático de irrigação#### Python Application#### Python Application

│   │

│   └── Cap 7/                     # Análise de Dados Reais- Simulação Wokwi disponível

│       ├── analise_R_grupo19.R    # Análise CONAB/IBGE

│       └── dados_agronegocio_grupo19.csv- ✅ Sistema interativo de cadastro de cultivos (Banana e Milho)- ✅ Sistema interativo de cadastro de cultivos (Banana e Milho)

│

├── testes/**Sistema de Gestão (Cap 6)**

│   └── teste_completo.py          # Validação automática

│- Arquitetura modular Python- ✅ Cálculo automático de área plantada (círculo, retângulo, quadrado)- ✅ Cálculo automático de área plantada (círculo, retângulo, quadrado)

└── docs/                           # Documentação

    ├── README.md- Integração com Oracle Database

    ├── INSTALL.md

    └── USAGE.md- Módulos: cultivos, sensores, irrigação, estoque- ✅ Estimativa de insumos necessários por m²- ✅ Estimativa de insumos necessários por m²

```



---

**Análise de Dados Reais (Cap 7)**- ✅ Exportação de dados para CSV- ✅ Exportação de dados para CSV

## 🚀 Instalação e Uso

- Dados CONAB/IBGE de produção agrícola

### Pré-requisitos

- Python 3.8+- Estatísticas por região- ✅ Validação de entrada e tratamento de erros- ✅ Validação de entrada e tratamento de erros

- R 4.0+ (opcional)

- Git- Testes estatísticos e visualizações



### Instalação



```bash---

git clone https://github.com/Cesar-Azeredo/FarmTechSolutions-Completo.git

cd FarmTechSolutions-Completo#### R Statistical Analysis#### R Statistical Analysis

```

## 🛠️ Tecnologias

### Uso Rápido

- 📊 Análise estatística completa (média, mediana, desvio padrão)- 📊 Análise estatística completa (média, mediana, desvio padrão)

#### Fase 1 - Python App

```bash- **Linguagens:** Python, R, C++ (Arduino), SQL

cd Fase1/python_app

python main.py- **Hardware:** ESP32, sensores NPK/pH, DHT22- 📈 Visualizações interativas (histogramas, boxplots)- 📈 Visualizações interativas (histogramas, boxplots)

```

- **Banco de Dados:** Oracle 19c, JSON, CSV

**Menu**:

```- **Ferramentas:** PlatformIO, Wokwi- 🔍 Distribuição por tipo geométrico e unidade de medida- 🔍 Distribuição por tipo geométrico e unidade de medida

1. Entrada de dados (cadastrar cultivos)

2. Saída de dados (visualizar)

3. Atualização de dados (editar)

4. Deleção de dados (remover)---- 📉 Análise de correlação entre variáveis- 📉 Análise de correlação entre variáveis

5. Sair

```



#### Fase 1 - Análise R## 📦 Instalação

```bash

cd Fase1/r_app



# Análise estatística### Requisitos------

Rscript analise.R

- Python 3.8+

# API meteorológica (Ir Além)

Rscript clima.R banana- R 4.0+ (opcional)

```

- Git

#### Fase 2 - ESP32 (Wokwi)

1. Acesse [wokwi.com](https://wokwi.com)### 🤖 Fase 2: IoT e Sistemas Integrados### 🤖 Fase 2: IoT e Sistemas Integrados

2. Carregue `Fase2/Cap 1/config/diagram.json`

3. Cole o código de `FarmTech.ino`### Clone

4. Execute a simulação



**Como usar**:

- Pressione botões NPK (Nitrogênio, Fósforo, Potássio)```bash

- Ajuste LDR (pH) e DHT22 (umidade)

- Observe decisão de irrigação (relé liga/desliga)git clone https://github.com/Cesar-Azeredo/FarmTechSolutions-Completo.git#### Capítulo 1: Sistema IoT com ESP32#### Capítulo 1: Sistema IoT com ESP32



#### Fase 2 - Sistema de Gestãocd FarmTechSolutions-Completo

```bash

cd Fase2/Cap\ 6```

pip install cx_Oracle

python main.py

```

### Uso Rápido**Hardware:****Hardware:**

---



## ✅ Validação

**Python App (Fase 1)**- ESP32 microcontroller- ESP32 microcontroller

Execute o teste completo para validar todas as fases:

```bash

```bash

cd testescd Fase1/python_app- Sensores NPK (Nitrogênio, Fósforo, Potássio)- Sensores NPK (Nitrogênio, Fósforo, Potássio)

python teste_completo.py

```python main.py



**Resultado esperado**:```- Sensor de pH do solo (LDR)- Sensor de pH do solo (LDR)

```

✅ Fase 1 - Python App: PASSOU

✅ Fase 1 - R App: PASSOU

✅ Fase 2 Cap 1 - ESP32 IoT: PASSOU**Análise R (Fase 1)**- DHT22 (temperatura e umidade)- DHT22 (temperatura e umidade)

✅ Fase 2 Cap 6 - Sistema de Gestão: PASSOU

✅ Fase 2 Cap 7 - Análise Estatística: PASSOU```bash



Total: 5/5 componentes passaram (100.0%)cd Fase1/r_app- Relé para controle de irrigação- Relé para controle de irrigação

```

Rscript analise.R

---

```

## 🛠️ Tecnologias



### Linguagens

- **Python 3.8+** - Gestão de cultivos, análise, backend**Sistema ESP32 (Fase 2)****Funcionalidades:****Funcionalidades:**

- **R 4.0+** - Estatística, visualizações, API meteorológica

- **C++/Arduino** - Firmware ESP32- Simular online: [wokwi.com](https://wokwi.com) + carregar `Fase2/Cap 1/config/diagram.json`

- **SQL** - Banco de dados Oracle

- Hardware real: Usar PlatformIO- ⚡ Leitura de sensores em tempo real- ⚡ Leitura de sensores em tempo real

### Hardware IoT

- **ESP32** - Microcontrolador

- **Botões (3x)** - Sensores NPK simulados

- **LDR** - Sensor pH simulado**Sistema de Gestão (Fase 2)**- 🧠 Decisão automática de irrigação- 🧠 Decisão automática de irrigação

- **DHT22** - Sensor umidade simulado

- **Relé** - Controle de bomba d'água```bash



### Ferramentascd Fase2/Cap\ 6- 📊 Log de dados via Serial Monitor- 📊 Log de dados via Serial Monitor

- **Wokwi** - Simulação ESP32 online

- **PlatformIO** - Desenvolvimento ESP32 realpip install cx_Oracle

- **Oracle 19c** - Banco de dados

- **Git** - Controle de versãopython main.py- 🔧 Calibração baseada em dados científicos- 🔧 Calibração baseada em dados científicos (EMBRAPA/IAC)



---```



## 📚 Documentação- 🌐 Suporte para simulação Wokwi- 🌐 Suporte para simulação Wokwi



- 📘 [Guia de Instalação](docs/INSTALL.md)---

- 📗 [Guia de Uso](docs/USAGE.md)

- 📖 [Documentação Completa](docs/README.md)



---## ✅ Validação



## 🎓 Especificações do Projeto**Projetos Avançados (ir_alem/):****Projetos Avançados (ir_alem/):**



Este projeto foi desenvolvido conforme as especificações das disciplinas:Execute o teste completo:



**Fase 1**: - 🐍 API Python para comunicação serial com ESP32- 🐍 API Python para comunicação serial com ESP32

- Aplicação Python com suporte a 2 culturas

- Cálculo de área plantada (figuras geométricas)```bash

- Cálculo de manejo de insumos

- Menu com entrada/saída/atualização/deleção/saircd testes- 📈 Modelos preditivos em R para otimização- 📈 Modelos preditivos em R para otimização

- Dados organizados em vetores

- Análise estatística em R (média, desvio padrão)python teste_completo.py

- **Ir Além**: API meteorológica em R

```- 🔗 Integração completa Python + R + ESP32- 🔗 Integração completa Python + R + ESP32

**Fase 2**:

- Sistema ESP32 com sensores NPK (botões), pH (LDR), umidade (DHT22)

- Decisão automática de irrigação (relé)

- Lógica baseada em necessidades da culturaValida automaticamente todas as fases do projeto.

- **Ir Além**: Integração Python + API OpenWeather

- **Ir Além**: Análise estatística em R para decisão de irrigação



------------



## 📄 Licença



MIT License - Consulte [LICENSE](LICENSE) para detalhes.## 📚 Documentação



---



<div align="center">Consulte [`docs/`](docs/) para:#### Capítulo 6: Sistema de Gestão Agrícola#### Capítulo 6: Sistema de Gestão Agrícola



**🌾 FarmTech Solutions**  - Guias de instalação detalhados

*Agricultura digital para o futuro sustentável*

- Instruções de uso

[GitHub](https://github.com/Cesar-Azeredo/FarmTechSolutions-Completo) • [Documentação](docs/)

- Documentação técnica

</div>

**Stack Tecnológico:****Stack Tecnológico:**

---

- Python 3.8+- Python 3.8+

## 📄 Licença

- Oracle Database 19c- Oracle Database 19c

MIT License - veja [LICENSE](LICENSE) para detalhes.

- Arquitetura modular (MVC)- Arquitetura modular (MVC)

---



<div align="center">

**Módulos:****Módulos:**

**🌾 FarmTech Solutions**  

*Tecnologia para agricultura sustentável*- 🌾 `cultivo_manager` - CRUD de cultivos- 🌾 `cultivo_manager` - CRUD de cultivos



</div>- 📡 `sensor_monitor` - Leitura e processamento de sensores- 📡 `sensor_monitor` - Leitura e processamento de sensores


- 💧 `irrigacao_controller` - Lógica de irrigação inteligente- 💧 `irrigacao_controller` - Lógica de irrigação inteligente

- 📦 `estoque_manager` - Controle de insumos- 📦 `estoque_manager` - Controle de insumos

- 🗄️ `database` - Integração Oracle- 🗄️ `database` - Integração Oracle

- 📄 `file_utils` - Persistência JSON- 📄 `file_utils` - Persistência JSON



**Features:****Features:**

- ✅ Cadastro completo de cultivos- ✅ Cadastro completo de cultivos

- ✅ Monitoramento de sensores- ✅ Monitoramento de sensores

- ✅ Decisões automáticas de irrigação- ✅ Decisões automáticas de irrigação

- ✅ Gestão de estoque de insumos- ✅ Gestão de estoque de insumos

- ✅ Relatórios e exportação de dados- ✅ Relatórios e exportação de dados

- ✅ Suite completa de testes automatizados

---

---

#### Capítulo 7: Análise de Dados Reais

#### Capítulo 7: Análise de Dados Reais

**Fonte de Dados:**

- CONAB (Companhia Nacional de Abastecimento)**Fonte de Dados:**

- IBGE (Instituto Brasileiro de Geografia e Estatística)- CONAB (Companhia Nacional de Abastecimento)

- Dados de produção de banana e milho (2024)- IBGE (Instituto Brasileiro de Geografia e Estatística)

- Dados de produção de banana e milho (2024)

**Análises:**

- 📊 Estatística descritiva completa**Análises:**

- 📈 Análise de tendências por região- 📊 Estatística descritiva completa

- 🔍 Testes de normalidade e correlação- 📈 Análise de tendências por região

- 📉 Visualizações profissionais (ggplot2)- 🔍 Testes de normalidade e correlação

- 📉 Visualizações profissionais (ggplot2)

---- 📑 Relatórios executivos



## 🗂️ Estrutura do Projeto---



```## 🗂️ Estrutura do Projeto

FarmTechSolutions-Completo/

│```

├── 📊 Fase1/                       # Análise de DadosFarmTechSolutions-Completo/

│   ├── python_app/                 # Sistema Python│

│   │   ├── main.py                 # App principal├── 📊 Fase1/                       # Análise de Dados

│   │   ├── gerador_exemplos.py    # Gerador de dados de teste│   ├── python_app/                 # Sistema Python

│   │   ├── banana.csv              # Dataset banana│   │   ├── main.py                 # App principal

│   │   └── milho.csv               # Dataset milho│   │   ├── gerador_exemplos.py    # Gerador de dados de teste

│   └── r_app/                      # Análise Estatística R│   │   ├── banana.csv              # Dataset banana

│       ├── analise.R               # Análise completa│   │   └── milho.csv               # Dataset milho

│       └── clima.R                 # Análise climática│   └── r_app/                      # Análise Estatística R

││       ├── analise.R               # Análise completa

├── 🤖 Fase2/                       # IoT e Sistemas│       └── clima.R                 # Análise climática

│   ├── Cap 1/                      # IoT ESP32│

│   │   ├── FarmTech.ino           # Código Arduino├── 🤖 Fase2/                       # IoT e Sistemas

│   │   ├── src/main.cpp           # Código C++│   ├── Cap 1/                      # IoT ESP32

│   │   ├── config/                # Configurações│   │   ├── FarmTech.ino           # Código Arduino

│   │   ├── scripts/               # Scripts auxiliares│   │   ├── src/main.cpp           # Código C++

│   │   └── ir_alem/               # Projetos avançados│   │   ├── config/                # Configurações

│   ││   │   │   ├── platformio.ini

│   ├── Cap 6/                     # Sistema de Gestão│   │   │   ├── wokwi.toml

│   │   ├── main.py                # App principal│   │   │   └── diagram.json

│   │   ├── test_farmtech.py       # Testes│   │   ├── scripts/               # Scripts auxiliares

│   │   ├── modules/               # Módulos│   │   └── ir_alem/               # Projetos avançados

│   │   ├── data/                  # Dados JSON│   │       ├── iralempython/      # API Python

│   │   └── sql/                   # Scripts SQL│   │       └── iralemR/           # Modelos ML

│   ││   │

│   └── Cap 7/                     # Análise Estatística│   ├── Cap 6/                     # Sistema de Gestão

│       ├── analise_R_grupo19.R│   │   ├── main.py                # App principal

│       └── dados_agronegocio_grupo19.csv│   │   ├── test_farmtech.py       # Testes

││   │   ├── modules/               # Módulos

├── 🧪 testes/                      # Scripts de Validação│   │   │   ├── cultivo_manager.py

││   │   │   ├── sensor_monitor.py

└── 📚 docs/                        # Documentação│   │   │   ├── irrigacao_controller.py

    ├── README.md│   │   │   ├── estoque_manager.py

    ├── INSTALL.md│   │   │   ├── database.py

    └── USAGE.md│   │   │   └── file_utils.py

```│   │   ├── data/                  # Dados JSON

│   │   └── sql/                   # Scripts SQL

---│   │

│   └── Cap 7/                     # Análise Estatística

## 🛠️ Instalação e Configuração│       ├── analise_R_grupo19.R

│       ├── dados_agronegocio_grupo19.csv

Veja a documentação completa em [`docs/`](docs/):│       └── teste_rapido.R

│

- 📘 [Guia de Instalação](docs/INSTALL.md)└── 📚 docs/                        # Documentação

- 📗 [Guia de Uso](docs/USAGE.md)    ├── Fase1/                      # Docs Fase 1

    │   ├── INSTALL.md

---    │   ├── INSTALL_R.md

    │   ├── TECHNICAL_DOCS.md

## 🛠️ Stack Tecnológico    │   └── requirements.txt

    └── Fase2/                      # Docs Fase 2

### Linguagens        ├── Cap1/                   # Docs IoT

- **Python** 3.8+ - Backend, IoT, análise        ├── Cap6/                   # Docs Sistema

- **R** 4.0+ - Estatística, visualizações        └── Cap7/                   # Docs Análise

- **C++** - Firmware ESP32```

- **SQL** - Banco de dados

---

### Frameworks & Bibliotecas

## 🛠️ Instalação e Configuração

**Python:**

- `csv`, `os`, `re` - Manipulação de dados### Pré-requisitos

- `json`, `datetime` - Persistência

- `cx_Oracle` - Conexão Oracle- **Python** 3.8 ou superior

- **R** 4.0 ou superior

**R:**- **Git** para controle de versão

- `readr` - Leitura de dados- **PlatformIO** (opcional, para ESP32)

- `ggplot2` - Visualizações

- `dplyr` - Manipulação de dados### Clone do Repositório



**IoT:**```bash

- Arduino/ESP32git clone https://github.com/seu-usuario/FarmTechSolutions-Completo.git

- PlatformIOcd FarmTechSolutions-Completo

- Wokwi (simulação)```



### Banco de Dados---

- **Oracle Database** 19c

- **JSON** (persistência local)### 📊 Fase 1 - Setup

- **CSV** (exportação)

#### Python App

### Hardware

- ESP32 microcontroller```bash

- Sensores NPKcd Fase1/python_app

- Sensor pH (LDR)python main.py

- DHT22 (temp/umidade)```

- Relé de irrigação

> **Nota:** Sem dependências externas. Usa apenas bibliotecas padrão do Python.

---

#### R App

## 🤝 Contribuições

```bash

Contribuições são bem-vindas! Para contribuir:cd Fase1/r_app



1. Fork o projeto# Instalar pacotes R

2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)Rscript -e "install.packages(c('readr', 'ggplot2', 'dplyr', 'tidyverse'))"

3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)

4. Push para a branch (`git push origin feature/AmazingFeature`)# Executar análise

5. Abra um Pull RequestRscript analise.R

```

---

---

## 📄 Licença

### 🤖 Fase 2 - Setup

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

#### Cap 1: IoT ESP32

---

**Opção 1 - Simulação Online (Wokwi):**

<div align="center">

1. Acesse [wokwi.com](https://wokwi.com)

**🌾 FarmTech Solutions - Tecnologia a serviço da agricultura sustentável 🇧🇷**2. Carregue o arquivo `config/diagram.json`

3. Cole o código de `FarmTech.ino`

</div>4. Execute a simulação


**Opção 2 - PlatformIO (Hardware Real):**

```bash
cd Fase2/Cap\ 1

# Compilar
pio run

# Upload para ESP32
pio run --target upload

# Monitor Serial
pio device monitor
```

---

#### Cap 6: Sistema de Gestão

```bash
cd Fase2/Cap\ 6

# Instalar dependências
pip install cx_Oracle

# Executar aplicação
python main.py

# Executar testes
python test_farmtech.py
```

**Configuração do Oracle:**
- Veja `docs/Fase2/Cap6/INSTALACAO_ORACLE.md`

---

#### Cap 7: Análise Estatística

```bash
cd Fase2/Cap\ 7

# Executar análise completa
Rscript analise_R_grupo19.R
```

**Saída:**
- Estatísticas descritivas no console
- Gráficos salvos automaticamente
- Relatório em `RESUMO_EXECUTIVO.md`

---

## 📚 Documentação Detalhada

### Fase 1
- 📘 [Guia de Instalação Python](docs/Fase1/INSTALL.md)
- 📙 [Guia de Instalação R](docs/Fase1/INSTALL_R.md)
- 📗 [Documentação Técnica Python](docs/Fase1/TECHNICAL_DOCS.md)
- 📕 [Documentação Técnica R](docs/Fase1/TECHNICAL_DOCS_R.md)
- 📔 [Exemplos Práticos R](docs/Fase1/EXEMPLOS_R.md)

### Fase 2
- 🔧 [Calibração de Sensores](docs/Fase2/Cap1/CALIBRACAO_LDR_WOKWI.md)
- 📊 [Tabela NPK/pH](docs/Fase2/Cap1/RELACAO_NPK_PH.md)
- 🗄️ [Instalação Oracle](docs/Fase2/Cap6/INSTALACAO_ORACLE.md)
- 🔗 [Integração ESP32](docs/Fase2/Cap6/INTEGRACAO_ESP32.md)
- 💧 [Lógica de Irrigação](docs/Fase2/Cap6/LOGICA_IRRIGACAO.md)
- 📈 [Fontes de Dados](docs/Fase2/Cap7/FONTES_DADOS_REAIS.md)

---

## 🧪 Testes

### Fase 1

```bash
# Python - Executar manualmente e testar funcionalidades
cd Fase1/python_app
python main.py

# R - Verificar análises
cd Fase1/r_app
Rscript analise.R
```

### Fase 2

```bash
# Cap 6 - Suite de testes automatizados
cd Fase2/Cap\ 6
python test_farmtech.py

# Saída esperada:
# ✅ Teste de Cultivo Manager
# ✅ Teste de Sensor Monitor
# ✅ Teste de Irrigação Controller
# ✅ Teste de Estoque Manager
```

---

## 🎯 Casos de Uso

### 1. Agricultor Pequeno Porte
- Monitoramento de 1-5 hectares
- Irrigação automatizada
- Redução de custos com insumos

### 2. Fazenda Média/Grande
- Gestão de múltiplos cultivos
- Integração com banco de dados corporativo
- Relatórios e análises avançadas

### 3. Pesquisador/Agrônomo
- Análise estatística de dados agrícolas
- Modelagem preditiva
- Otimização de processos

---

## 🛠️ Stack Tecnológico

### Linguagens
- **Python** 3.8+ - Backend, IoT, análise
- **R** 4.0+ - Estatística, visualizações
- **C++** - Firmware ESP32
- **SQL** - Banco de dados

### Frameworks & Bibliotecas

**Python:**
- `csv`, `os`, `re` - Manipulação de dados
- `json`, `datetime` - Persistência
- `cx_Oracle` - Conexão Oracle

**R:**
- `readr` - Leitura de dados
- `ggplot2` - Visualizações
- `dplyr` - Manipulação de dados
- `tidyverse` - Ecossistema completo

**IoT:**
- Arduino/ESP32
- PlatformIO
- Wokwi (simulação)

### Banco de Dados
- **Oracle Database** 19c
- **JSON** (persistência local)
- **CSV** (exportação)

### Hardware
- ESP32 microcontroller
- Sensores NPK
- Sensor pH (LDR)
- DHT22 (temp/umidade)
- Relé de irrigação

---

## 📊 Dados Científicos

### Dosagens NPK por Cultura

| Cultura | Nitrogênio (N) | Fósforo (P) | Potássio (K) |
|---------|----------------|-------------|--------------|
| 🍌 Banana | 15 g/m² | 10 g/m² | **20 g/m²** |
| 🌽 Milho | **12 g/m²** | 8 g/m² | 10 g/m² |

### Limites de pH

- **pH Mínimo:** 5.5
- **pH Ideal:** 6.5
- **pH Máximo:** 7.5

### Limites de Umidade do Solo

- **Mínima (irrigar):** < 40%
- **Ideal:** 60%
- **Máxima (encharcado):** > 80%

**Fonte:** EMBRAPA, IAC, CONAB

---

## 🚀 Roadmap Futuro

- [ ] 📱 App mobile para monitoramento remoto
- [ ] ☁️ Integração com cloud (AWS/Azure)
- [ ] 🤖 Modelos de ML mais avançados
- [ ] 📡 Suporte para mais sensores
- [ ] 🌐 Dashboard web em tempo real
- [ ] 📊 Alertas e notificações
- [ ] 🔗 API RESTful pública

---

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

- **EMBRAPA** - Dados técnicos sobre cultivos brasileiros
- **CONAB** - Dados estatísticos de produção agrícola
- **IBGE** - Dados geográficos e regionais
- **Comunidade Open Source** - Bibliotecas e ferramentas incríveis

---

## 📞 Contato

**FarmTech Solutions Team**

- 📧 Email: farmtech.solutions@example.com
- 💼 LinkedIn: [FarmTech Solutions](https://linkedin.com)
- 🐙 GitHub: [github.com/seu-usuario](https://github.com)

---

<div align="center">

**🌾 FarmTech Solutions - Tecnologia a serviço da agricultura sustentável 🇧🇷**

*Desenvolvido com ❤️ por [Phellype Massarente](https://github.com), [Carlos Costato](https://github.com), [Cesar Azeredo](https://github.com)*

</div>
