# 🌾 FarmTech Solutions
**Sistema de Agricultura Inteligente com IoT, Python, R e Oracle**

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![R](https://img.shields.io/badge/R-4.0%2B-lightblue)

---

## 📋 Sobre o Projeto

FarmTech Solutions é uma startup voltada à **agricultura digital**, que une tecnologia, inovação e sustentabilidade para otimizar os processos de cultivo e gestão agrícola.  

O sistema é dividido em **duas fases principais**:  
- 🌱 **Fase 1:** Gestão de cultivos e análise de dados agrícolas.  
- 🤖 **Fase 2:** Desenvolvimento de um sistema de **irrigação inteligente com IoT (ESP32)** e integração com banco de dados Oracle, análise estatística e simulação de dados reais.

O objetivo é demonstrar o potencial da agricultura de precisão e do uso de IoT, IA e análise de dados para aprimorar a produtividade e eficiência no agronegócio.

---

## 📂 Estrutura do Projeto

### 🌱 Fase 1 – Gestão de Cultivos e Análise de Dados

#### 📘 Introdução

Nesta primeira fase, a equipe da **FarmTech Solutions** iniciou o desenvolvimento de uma aplicação em **Python** para apoiar uma fazenda em transição para a **Agricultura Digital**, visando aumentar produtividade e controle de insumos.

#### 🧩 Funcionalidades Principais

- **Suporte a 2 tipos de culturas agrícolas** escolhidas pelo grupo.  
- **Cálculo da área de plantio**, permitindo escolher diferentes figuras geométricas (retângulo, trapézio, círculo etc.).  
- **Cálculo do manejo de insumos**, como fertilizantes, herbicidas e inseticidas, considerando área e quantidade aplicada.  
- **Estruturas de dados com vetores** para armazenar e manipular informações das culturas.  
- **Menu interativo** com operações de:
  - Entrada de dados
  - Saída de dados (relatórios no terminal)
  - Atualização e exclusão de registros
  - Opção de encerramento da aplicação  
- **Uso de loops e estruturas condicionais** para fluxo lógico e repetição de cálculos.

#### 🧮 Integração com R

Após a coleta e cálculo de dados, uma aplicação em **R** realiza análises estatísticas básicas:
- Médias, desvios-padrão e dispersão
- Visualizações gráficas
- Integração opcional com API meteorológica pública (Open-Meteo) para análise climática

#### 🌦️ Ir Além

Usando **R (e não Python)**, é possível conectar-se a uma API meteorológica para coletar dados climáticos e exibir informações meteorológicas diretamente no terminal, promovendo uma integração entre dados agrícolas e variáveis ambientais.

---

### 🤖 Fase 2 – IoT e Sistemas Integrados

#### 📘 Introdução

A **Fase 2** avança para a aplicação prática da agricultura digital, com foco em **IoT e automação agrícola**.  
A equipe desenvolveu um **sistema de irrigação inteligente** capaz de monitorar variáveis do solo e decidir automaticamente quando irrigar uma plantação.

#### ⚙️ Simulação Wokwi Walkthrough (`Fase2/SimulacaoWokwi/`)

Com base na simulação do ambiente agrícola, foram implementados os seguintes sensores e atuadores:

- **Botões (3)** representando sensores de **Nitrogênio (N)**, **Fósforo (P)** e **Potássio (K)**.  
- **Sensor LDR (Light Dependent Resistor)** simulando o **pH do solo**, variando entre 0 e 14.  
- **Sensor DHT22** representando a **umidade do solo** (substituindo o sensor real de umidade).  
- **Relé azul** representando uma **bomba de irrigação** real, controlada automaticamente.  

#### 💧 Lógica de Irrigação

O sistema monitora em tempo real os níveis de N, P, K, pH e umidade.  
Com base nesses dados, o ESP32 decide se a irrigação deve ser ativada ou não, simulando a operação real de uma lavoura digital.  
A lógica de irrigação varia conforme a cultura agrícola escolhida pelo grupo.

#### 🌐 Ir Além – Integração com Python e R

- **Integração com API meteorológica (OpenWeather):** permite prever chuva e ajustar a irrigação automaticamente.  
- **Leitura via Serial Monitor:** permite inserir dados manuais no simulador Wokwi durante execução.  
- **Análise estatística em R:** opcionalmente, o sistema pode usar R para decidir quando ativar a bomba de irrigação com base em variáveis climáticas e nutricionais.

Essa etapa promove a integração entre **sensoriamento, IoT, Data Science e automação agrícola**, reforçando o conceito de **fazenda inteligente**.

---

### 🏗️ Sistema de Gestão Agrícola (`Fase2/SistemaGestaoAgricola/`)

#### 📘 Contexto

O **agronegócio** é um setor que abrange todas as atividades ligadas à produção, comercialização e distribuição de produtos agrícolas — sendo um dos pilares da economia brasileira.  
O sistema de gestão agrícola da FarmTech Solutions foi desenvolvido para integrar **dados operacionais, ambientais e financeiros**, promovendo **tomada de decisão baseada em dados**.

#### ⚙️ Funcionalidades

- **Arquitetura modular em Python**
  - `cultivo_manager`: gerenciamento de culturas agrícolas  
  - `sensor_monitor`: integração com sensores físicos ou simulados  
  - `irrigacao_controller`: controle automatizado de irrigação  
  - `estoque_manager`: controle de insumos e recursos agrícolas
- **Banco de dados Oracle Database 19c** para armazenamento centralizado  
- **Persistência em JSON** para fácil leitura e backup  
- **Testes automatizados** para validar módulos, entradas e saídas  
- **Análise de consistência dos dados** e interface clara no terminal

#### 🌱 Contextualização do Agronegócio

O sistema está inserido dentro de um cenário de **transformação digital no agro**, caracterizado por:
- Segurança alimentar e sustentabilidade  
- Inovação com IoT e análise de dados  
- Redução de desperdícios e otimização de recursos hídricos  
- Uso de **agrotechs** como agentes de digitalização do campo  

---

### 📊 Análise R (`Fase2/AnaliseR/`)

#### 📘 Contexto

Nesta etapa, o grupo trabalha com **dados reais do agronegócio brasileiro**, obtidos de fontes públicas como:
- **CONAB** – Companhia Nacional de Abastecimento  
- **IBGE** – Instituto Brasileiro de Geografia e Estatística  
- **MAPA** – Ministério da Agricultura  
- **EMBRAPA** – Empresa Brasileira de Pesquisa Agropecuária  
- **CNA Brasil** – Confederação da Agricultura e Pecuária  

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

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**  Gestão de cultivos, análise e backend  
- **R 4.0+**  Análise estatística e visualizações  
- **C++/Arduino**  Firmware ESP32  
- **Oracle Database 19c**  Banco de dados  
- **ESP32**  Microcontrolador IoT  
- **Wokwi**  Simulação de hardware  

---

## 🚀 Como Executar

### ✅ Validação Completa
```powershell
cd testes
python teste_completo.py
```

### 🐍 Fase 1 - Python App
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

### 🤖 Fase 2 - Simulação Wokwi Walkthrough
1. Acesse [wokwi.com](https://wokwi.com)
2. Carregue `Fase2/SimulacaoWokwi/config/diagram.json`
3. Cole o código de `Fase2/SimulacaoWokwi/FarmTech.ino`
4. Execute a simulação

### 💼 Fase 2 - Sistema de Gestão
```powershell
cd Fase2\SistemaGestaoAgricola
python main.py
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
Phellype Massarente • Carlos Costato • Cesar Azeredo  

## 📄 Licença
MIT
