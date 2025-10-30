# FarmTech Solutions# FarmTech Solutions



Sistema de agricultura de precisão que integra IoT, análise de dados e automação para otimização de cultivos agrícolas.Sistema de agricultura de precisão com IoT (ESP32), Python e R. Minimalista, profissional e baseado no que existe no código.



## Sobre o Projeto## Conteúdo

- `Fase1/python_app`: app em Python para 2 culturas (entrada/saída/atualização/remoção), cálculos de área e exportação CSV

FarmTech Solutions é um sistema completo desenvolvido para agricultura inteligente, combinando hardware IoT (ESP32), análise estatística (Python e R) e gestão de dados para monitoramento e automação de cultivos.- `Fase1/r_app`: scripts R para estatística e exemplo de clima (Open-Meteo)

- `Fase2/Cap 1`: firmware ESP32 (NPK em botões, pH via LDR, umidade via DHT22, relé de irrigação) + `config/diagram.json` (Wokwi)

## Estrutura do Projeto- `Fase2/Cap 6`: sistema de gestão em Python (módulos: cultivo, sensores, irrigação, estoque) + SQL

- `Fase2/Cap 7`: análise R com dataset real

### Fase 1: Gestão de Cultivos e Análise de Dados- `testes/teste_completo.py`: validação automática de todas as fases



**Python Application** (`Fase1/python_app/`)## Como executar (Windows/PowerShell)

- Sistema interativo de gestão para 2 culturas (Banana e Milho)

- Menu CRUD completo: entrada, saída, atualização e deleção de dadosValidação completa:

- Cálculo automático de área plantada (retângulo, trapézio, círculo)```powershell

- Cálculo de manejo de insumos (Fosfato, Nitrogênio, Potássio, Herbicida, Inseticida)cd FarmTechSolutions-Completo\testes

- Exportação de dados para CSVpython teste_completo.py

- Dados organizados em vetores com rotinas de loop e decisão```



**R Statistical Analysis** (`Fase1/r_app/`)Fase 1 — App Python:

- Análise estatística completa: média, mediana, desvio padrão```powershell

- Análise de distribuição por tipo geométrico e unidadecd ..\Fase1\python_app

- Integração com API Open-Meteo para dados meteorológicos (Ir Além)python main.py

```

### Fase 2: IoT e Sistemas Integrados

Fase 1 — Análises em R (opcional):

**Capítulo 1: Sistema IoT com ESP32** (`Fase2/Cap 1/`)```powershell

- Monitoramento de sensores NPK (Nitrogênio, Fósforo, Potássio) via botõescd ..\r_app

- Sensor de pH do solo simulado com LDRRscript analise.R

- Sensor de umidade DHT22Rscript clima.R banana

- Controle automático de irrigação via relé```

- Lógica de decisão baseada em necessidades das culturas

- Simulação disponível no WokwiFase 2 — Cap 1 (ESP32 no Wokwi):

- Projetos Ir Além: API Python para comunicação serial e análise estatística em R- Abrir https://wokwi.com

- Carregar `Fase2/Cap 1/config/diagram.json`

**Capítulo 6: Sistema de Gestão Agrícola** (`Fase2/Cap 6/`)- Colar `Fase2/Cap 1/FarmTech.ino` e executar

- Arquitetura modular em Python

- Módulos: cultivo_manager, sensor_monitor, irrigacao_controller, estoque_managerFase 2 — Cap 6 (Sistema de Gestão):

- Integração com Oracle Database```powershell

- Persistência de dados em JSONcd ..\..\Fase2\Cap 6

- Suite completa de testes automatizadospython main.py

```

**Capítulo 7: Análise de Dados Reais** (`Fase2/Cap 7/`)

- Dataset com dados de produção agrícola (CONAB/IBGE)## Autores

- Análise estatística completa em RPhellype Massarente • Carlos Costato • Cesar Azeredo

- 35 registros de propriedades por região

## Licença

## Tecnologias UtilizadasMIT# 🌾 FarmTech Solutions# 🌾 FarmTech Solutions# 🌾 FarmTech Solutions# 🌾 FarmTech Solutions



- **Python 3.8+** - Gestão de cultivos, análise e backend

- **R 4.0+** - Análise estatística e visualizações

- **C++/Arduino** - Firmware ESP32Sistema completo de agricultura de precisão com IoT, análise de dados e automação de irrigação.

- **Oracle Database 19c** - Banco de dados

- **ESP32** - Microcontrolador IoT

- **Wokwi** - Simulação de hardware

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)Sistema inteligente de agricultura de precisão com IoT, análise de dados e automação.

## Como Executar

[![R](https://img.shields.io/badge/R-4.0+-276DC3.svg)](https://www.r-project.org/)

### Validação Completa

```powershell[![ESP32](https://img.shields.io/badge/ESP32-Wokwi-orange.svg)](https://wokwi.com/)

cd testes

python teste_completo.py[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

```

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)> **Sistema inteligente de agricultura de precisão** integrando IoT, análise de dados e machine learning para otimização de cultivos agrícolas.> **Sistema inteligente de agricultura de precisão** integrando IoT, análise de dados e machine learning para otimização de cultivos agrícolas.

### Fase 1 - Python App

```powershell---

cd Fase1\python_app

python main.py[![R](https://img.shields.io/badge/R-4.0+-276DC3.svg)](https://www.r-project.org/)

```

## 📖 Sobre o Projeto

### Fase 1 - Análise R

```powershell[![ESP32](https://img.shields.io/badge/ESP32-IoT-orange.svg)](https://www.espressif.com/)

cd Fase1\r_app

Rscript analise.RA **FarmTech Solutions** é uma startup que desenvolve tecnologia para agricultura digital. Este projeto implementa um sistema completo de gestão agrícola que integra:

Rscript clima.R banana

```[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)



### Fase 2 - Simulação ESP32 (Wokwi)- **Gestão de Cultivos** - Sistema Python para cálculo de área plantada e manejo de insumos

1. Acesse [wokwi.com](https://wokwi.com)

2. Carregue `Fase2/Cap 1/config/diagram.json`- **Análise Estatística** - Processamento de dados em R com estatísticas e API meteorológica[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

3. Cole o código de `Fase2/Cap 1/FarmTech.ino`

4. Execute a simulação- **IoT ESP32** - Monitoramento de NPK, pH e umidade com irrigação automatizada



### Fase 2 - Sistema de Gestão- **Sistema de Gestão** - Plataforma completa com banco de dados Oracle---

```powershell

cd Fase2\Cap 6

python main.py

```---[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)



## Validação e Testes



O projeto inclui um sistema completo de validação automática em `testes/teste_completo.py` que verifica:## 👥 Equipe## 📋 Sobre

- Sintaxe e execução de todas as aplicações Python

- Presença e estrutura de todos os componentes

- Validação de configurações ESP32 e Wokwi

- Verificação de scripts R e datasets**Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo**[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)



## Documentação



A documentação técnica completa está disponível na pasta `docs/`:---Plataforma completa para agricultura inteligente que integra:

- Guia de instalação

- Instruções de uso

- Especificações técnicas

## 🎯 Funcionalidades[![ESP32](https://img.shields.io/badge/ESP32-IoT-orange.svg)](https://www.espressif.com/)[![ESP32](https://img.shields.io/badge/ESP32-IoT-orange.svg)](https://www.espressif.com/)

## Autores



Phellype Massarente • Carlos Costato • Cesar Azeredo

### Fase 1: Gestão de Cultivos e Análise- **IoT com ESP32** - Monitoramento e controle automático de irrigação

## Licença



MIT

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

# FarmTech Solutions

Sistema de agricultura de precisão com IoT (ESP32), análise de dados (Python/R) e automação de irrigação.

---

## O que tem aqui
- `Fase1/python_app`: app em Python para gerenciar 2 culturas (entrada/saída/atualização/remoção), cálculos de área e exportação CSV
- `Fase1/r_app`: scripts R para estatística e exemplo de clima via API
- `Fase2/Cap 1`: firmware ESP32 (NPK via botões, pH via LDR, umidade via DHT22, relé de irrigação) + config Wokwi
- `Fase2/Cap 6`: sistema de gestão em Python (módulos de cultivo, sensores, irrigação, estoque) + SQL
- `Fase2/Cap 7`: análise R com dataset real (CONAB/IBGE)
- `testes/teste_completo.py`: validação automática de todas as fases

---

## Como executar (Windows/PowerShell)

Validar tudo (recomendado):
```powershell
cd FarmTechSolutions-Completo\testes
python teste_completo.py
```

Rodar o app Python (Fase 1):
```powershell
cd ..\Fase1\python_app
python main.py
```

Análises em R (opcional):
```powershell
cd ..\r_app
Rscript analise.R
Rscript clima.R banana
```

Simular o ESP32 (Fase 2 – Cap 1) no Wokwi:
- Abrir https://wokwi.com
- Carregar `Fase2/Cap 1/config/diagram.json`
- Colar `Fase2/Cap 1/FarmTech.ino` e executar

Sistema de Gestão (Fase 2 – Cap 6):
```powershell
cd ..\..\Fase2\Cap 6
python main.py
```

---

## Autores
Phellype Massarente • Carlos Costato • Cesar Azeredo

## Licença
MIT

