# FarmTech Solutions - Projeto Completo

## 📋 Sobre o Projeto

FarmTech Solutions é um projeto de agricultura inteligente desenvolvido pela FIAP, focado em monitoramento e automação de cultivos agrícolas utilizando IoT, análise de dados e tecnologias modernas.

## 🗂️ Estrutura do Projeto

```
FarmTechSolutions-Completo/
├── Fase1/               # Primeira fase - Análise de dados e predições
│   ├── python_app/      # Aplicação Python para análise
│   └── r_app/           # Aplicação R para modelagem estatística
├── Fase2/               # Segunda fase - IoT e Sistema Completo
│   ├── Cap 1/           # IoT com ESP32 e sensores
│   ├── Cap 6/           # Sistema Python com banco de dados
│   └── Cap 7/           # Análise de dados do agronegócio
└── docs/                # Documentação completa do projeto
    ├── Fase1/           # Documentação da Fase 1
    └── Fase2/           # Documentação da Fase 2
        ├── Cap1/
        ├── Cap6/
        └── Cap7/
```

## 🚀 Fase 1 - Análise e Predição

### Python App
- Análise de dados agrícolas
- Predição de safras
- Geração de exemplos e visualizações

### R App
- Modelagem estatística
- Análise climática
- Processamento de dados

**📖 Documentação:** Ver pasta `docs/Fase1/`

## 🌱 Fase 2 - IoT e Sistema Integrado

### Capítulo 1 - IoT com ESP32
- Monitoramento de sensores (NPK, pH, LDR)
- Integração com Wokwi
- Controle de irrigação automatizado
- Sistema de coleta de dados em tempo real

**Tecnologias:** ESP32, PlatformIO, C++, Python, R

### Capítulo 6 - Sistema de Gestão
- Gerenciamento de cultivos
- Controle de estoque
- Sistema de irrigação inteligente
- Monitoramento de sensores
- Integração com banco de dados Oracle

**Tecnologias:** Python, Oracle Database, JSON

### Capítulo 7 - Análise de Dados do Agronegócio
- Análise estatística de dados reais
- Visualizações e gráficos
- Insights para tomada de decisão

**Tecnologias:** R, ggplot2, dplyr

**📖 Documentação:** Ver pasta `docs/Fase2/`

## 🛠️ Tecnologias Utilizadas

### Linguagens
- Python
- R
- C++ (Arduino/ESP32)
- SQL

### Ferramentas e Frameworks
- ESP32 / PlatformIO
- Wokwi (simulação)
- Oracle Database
- Pandas, NumPy, Matplotlib
- ggplot2, dplyr, tidyverse

### Hardware (Fase 2)
- ESP32
- Sensores NPK
- Sensor de pH
- LDR (sensor de luminosidade)
- Sistema de irrigação

## 📦 Instalação e Execução

### Fase 1

**Python App:**
```bash
cd Fase1/python_app
pip install -r requirements.txt
python main.py
```

**R App:**
```bash
cd Fase1/r_app
# Instalar dependências listadas em requirements_r.txt
Rscript analise.R
```

### Fase 2

**Cap 1 (IoT):**
```bash
cd Fase2/cursotiaor/pbl/Fase2/Cap\ 1
# Abrir no PlatformIO ou Wokwi
```

**Cap 6 (Sistema Python):**
```bash
cd Fase2/cursotiaor/pbl/Fase2/Cap\ 6
pip install -r requirements.txt
python main.py
```

**Cap 7 (Análise R):**
```bash
cd Fase2/cursotiaor/pbl/Fase2/Cap\ 7
Rscript analise_R_grupo19.R
```

## 👥 Equipe

Projeto desenvolvido por estudantes da FIAP - Grupo 19

## 📄 Licença

Este projeto é desenvolvido para fins educacionais na FIAP.

## 📞 Contato

Para mais informações, consulte a documentação completa em `docs/`
