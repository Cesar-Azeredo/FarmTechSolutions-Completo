# 🌾 FarmTech Solutions# 🌾 FarmTech Solutions

**Sistema de Agricultura Inteligente com IoT, Python, R e Oracle**

Sistema de agricultura de precisão com IoT, análise de dados e automação de irrigação.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

![License: MIT](https://img.shields.io/badge/License-MIT-green)---

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

![R](https://img.shields.io/badge/R-4.0%2B-lightblue)## 📋 Sobre o Projeto



---FarmTech Solutions é um sistema completo para agricultura inteligente que combina:



## 📋 Sobre o Projeto- 🤖 **IoT com ESP32** - Monitoramento e controle automático de irrigação

- 📊 **Análise de Dados** - Processamento estatístico em Python e R

FarmTech Solutions é uma startup voltada à **agricultura digital**, que une tecnologia, inovação e sustentabilidade para otimizar os processos de cultivo e gestão agrícola.  - 🗄️ **Gestão Completa** - Sistema de gerenciamento com banco de dados Oracle



O sistema é dividido em **duas fases principais**:  ---

- 🌱 **Fase 1:** Gestão de cultivos e análise de dados agrícolas.  

- 🤖 **Fase 2:** Desenvolvimento de um sistema de **irrigação inteligente com IoT (ESP32)** e integração com banco de dados Oracle, análise estatística e simulação de dados reais.## 📂 Estrutura do Projeto



O objetivo é demonstrar o potencial da agricultura de precisão e do uso de IoT, IA e análise de dados para aprimorar a produtividade e eficiência no agronegócio.### 🌱 Fase 1: Gestão de Cultivos e Análise de Dados



---#### Python Application (`Fase1/python_app/`)

- ✅ Sistema interativo de gestão para 2 culturas (Banana e Milho)

## 📂 Estrutura do Projeto- ✅ Menu CRUD completo: entrada, saída, atualização e deleção de dados

- ✅ Cálculo automático de área plantada (retângulo, trapézio, círculo)

### 🌱 Fase 1 – Gestão de Cultivos e Análise de Dados- ✅ Cálculo de manejo de insumos (Fosfato, Nitrogênio, Potássio, Herbicida, Inseticida)

- ✅ Exportação de dados para CSV

#### 📘 Introdução- ✅ Dados organizados em vetores com rotinas de loop e decisão



Nesta primeira fase, a equipe da **FarmTech Solutions** iniciou o desenvolvimento de uma aplicação em **Python** para apoiar uma fazenda em transição para a **Agricultura Digital**, visando aumentar produtividade e controle de insumos.#### R Statistical Analysis (`Fase1/r_app/`)

- 📈 Análise estatística completa: média, mediana, desvio padrão

#### 🧩 Funcionalidades Principais- 📊 Análise de distribuição por tipo geométrico e unidade

- 🌦️ Integração com API Open-Meteo para dados meteorológicos (Ir Além)

- **Suporte a 2 tipos de culturas agrícolas** escolhidas pelo grupo.  

- **Cálculo da área de plantio**, permitindo escolher diferentes figuras geométricas (retângulo, trapézio, círculo etc.).  ### 🤖 Fase 2: IoT e Sistemas Integrados

- **Cálculo do manejo de insumos**, como fertilizantes, herbicidas e inseticidas, considerando área e quantidade aplicada.  

- **Estruturas de dados com vetores** para armazenar e manipular informações das culturas.  #### Capítulo 1: Sistema IoT com ESP32 (`Fase2/Cap 1/`)

- **Menu interativo** com operações de:- 🟢 Monitoramento de sensores NPK (Nitrogênio, Fósforo, Potássio) via botões

  - Entrada de dados- 💡 Sensor de pH do solo simulado com LDR

  - Saída de dados (relatórios no terminal)- 🌡️ Sensor de umidade DHT22

  - Atualização e exclusão de registros- 💧 Controle automático de irrigação via relé

  - Opção de encerramento da aplicação  - 🧠 Lógica de decisão baseada em necessidades das culturas

- **Uso de loops e estruturas condicionais** para fluxo lógico e repetição de cálculos.- 🔧 Simulação disponível no Wokwi

- 🚀 Projetos Ir Além: API Python para comunicação serial e análise estatística em R

#### 🧮 Integração com R

#### Capítulo 6: Sistema de Gestão Agrícola (`Fase2/Cap 6/`)

Após a coleta e cálculo de dados, uma aplicação em **R** realiza análises estatísticas básicas:- 🏗️ Arquitetura modular em Python

- Médias, desvios-padrão e dispersão- 📦 Módulos: `cultivo_manager`, `sensor_monitor`, `irrigacao_controller`, `estoque_manager`

- Visualizações gráficas- 🗄️ Integração com Oracle Database

- Integração opcional com API meteorológica pública (Open-Meteo) para análise climática- 📄 Persistência de dados em JSON

- 🧪 Suite completa de testes automatizados

#### 🌦️ Ir Além

#### Capítulo 7: Análise de Dados Reais (`Fase2/Cap 7/`)

Usando **R (e não Python)**, é possível conectar-se a uma API meteorológica para coletar dados climáticos e exibir informações meteorológicas diretamente no terminal, promovendo uma integração entre dados agrícolas e variáveis ambientais.- 📊 Dataset com dados de produção agrícola (CONAB/IBGE)

- 📈 Análise estatística completa em R

---- 🌾 35 registros de propriedades por região



### 🤖 Fase 2 – IoT e Sistemas Integrados---



#### 📘 Introdução## 🛠️ Tecnologias Utilizadas



A **Fase 2** avança para a aplicação prática da agricultura digital, com foco em **IoT e automação agrícola**.  - **Python 3.8+** - Gestão de cultivos, análise e backend

A equipe desenvolveu um **sistema de irrigação inteligente** capaz de monitorar variáveis do solo e decidir automaticamente quando irrigar uma plantação.- **R 4.0+** - Análise estatística e visualizações

- **C++/Arduino** - Firmware ESP32

#### ⚙️ Capítulo 1 – Sistema IoT com ESP32 (`Fase2/Cap 1/`)- **Oracle Database 19c** - Banco de dados

- **ESP32** - Microcontrolador IoT

Com base na simulação do ambiente agrícola, foram implementados os seguintes sensores e atuadores:- **Wokwi** - Simulação de hardware



- **Botões (3)** representando sensores de **Nitrogênio (N)**, **Fósforo (P)** e **Potássio (K)**.  ---

- **Sensor LDR (Light Dependent Resistor)** simulando o **pH do solo**, variando entre 0 e 14.  

- **Sensor DHT22** representando a **umidade do solo** (substituindo o sensor real de umidade).  ## 🚀 Como Executar

- **Relé azul** representando uma **bomba de irrigação** real, controlada automaticamente.  

### ✅ Validação Completa

#### 💧 Lógica de Irrigação```powershell

cd testes

O sistema monitora em tempo real os níveis de N, P, K, pH e umidade.  python teste_completo.py

Com base nesses dados, o ESP32 decide se a irrigação deve ser ativada ou não, simulando a operação real de uma lavoura digital.  ```

A lógica de irrigação varia conforme a cultura agrícola escolhida pelo grupo.

### 🐍 Fase 1 - Python App

#### 🌐 Ir Além – Integração com Python e R```powershell

cd Fase1\python_app

- **Integração com API meteorológica (OpenWeather):** permite prever chuva e ajustar a irrigação automaticamente.  python main.py

- **Leitura via Serial Monitor:** permite inserir dados manuais no simulador Wokwi durante execução.  ```

- **Análise estatística em R:** opcionalmente, o sistema pode usar R para decidir quando ativar a bomba de irrigação com base em variáveis climáticas e nutricionais.

### � Fase 1 - Análise R

Essa etapa promove a integração entre **sensoriamento, IoT, Data Science e automação agrícola**, reforçando o conceito de **fazenda inteligente**.```powershell

cd Fase1\r_app

---Rscript analise.R

Rscript clima.R banana

### 🏗️ Capítulo 6 – Sistema de Gestão Agrícola (`Fase2/Cap 6/`)```



#### 📘 Contexto### 🤖 Fase 2 - Simulação ESP32 (Wokwi)

1. Acesse [wokwi.com](https://wokwi.com)

O **agronegócio** é um setor que abrange todas as atividades ligadas à produção, comercialização e distribuição de produtos agrícolas — sendo um dos pilares da economia brasileira.  2. Carregue `Fase2/Cap 1/config/diagram.json`

O sistema de gestão agrícola da FarmTech Solutions foi desenvolvido para integrar **dados operacionais, ambientais e financeiros**, promovendo **tomada de decisão baseada em dados**.3. Cole o código de `Fase2/Cap 1/FarmTech.ino`

4. Execute a simulação

#### ⚙️ Funcionalidades

### 💼 Fase 2 - Sistema de Gestão

- **Arquitetura modular em Python**```powershell

  - `cultivo_manager`: gerenciamento de culturas agrícolas  cd Fase2\Cap 6

  - `sensor_monitor`: integração com sensores físicos ou simulados  python main.py

  - `irrigacao_controller`: controle automatizado de irrigação  ```

  - `estoque_manager`: controle de insumos e recursos agrícolas

- **Banco de dados Oracle Database 19c** para armazenamento centralizado  ---

- **Persistência em JSON** para fácil leitura e backup  

- **Testes automatizados** para validar módulos, entradas e saídas  ## 🧪 Validação e Testes

- **Análise de consistência dos dados** e interface clara no terminal

O projeto inclui um sistema completo de validação automática em `testes/teste_completo.py` que verifica:

#### 🌱 Contextualização do Agronegócio

- ✅ Sintaxe e execução de todas as aplicações Python

O sistema está inserido dentro de um cenário de **transformação digital no agro**, caracterizado por:- ✅ Presença e estrutura de todos os componentes

- Segurança alimentar e sustentabilidade  - ✅ Validação de configurações ESP32 e Wokwi

- Inovação com IoT e análise de dados  - ✅ Verificação de scripts R e datasets

- Redução de desperdícios e otimização de recursos hídricos  

- Uso de **agrotechs** como agentes de digitalização do campo  ---



---## 📚 Documentação



### 📊 Capítulo 7 – Análise de Dados Reais (`Fase2/Cap 7/`)A documentação técnica completa está disponível na pasta `docs/`:



#### 📘 Contexto- 📘 Guia de instalação

- 📗 Instruções de uso

Nesta etapa, o grupo trabalha com **dados reais do agronegócio brasileiro**, obtidos de fontes públicas como:- 📖 Especificações técnicas

- **CONAB** – Companhia Nacional de Abastecimento  

- **IBGE** – Instituto Brasileiro de Geografia e Estatística  ---

- **MAPA** – Ministério da Agricultura  

- **EMBRAPA** – Empresa Brasileira de Pesquisa Agropecuária  ## 👥 Autores

- **CNA Brasil** – Confederação da Agricultura e Pecuária  

**Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo**

#### 📈 Entregáveis

---

- **Base de dados em Excel** com:

  - 30 linhas e 4 colunas  ## 📄 Licença

  - Variável quantitativa discreta  

  - Variável quantitativa contínua  MIT

  - Variável qualitativa nominal  - Abrir https://wokwi.com

  - Variável qualitativa ordinal  - Carregar `Fase2/Cap 1/config/diagram.json`

- **Análise exploratória em R** contendo:- Colar `Fase2/Cap 1/FarmTech.ino` e executar

  - Medidas de tendência central  

  - Medidas de dispersão  Sistema de Gestão (Fase 2 – Cap 6):

  - Medidas separatrizes  ```powershell

  - Análise gráfica de variáveis quantitativas e qualitativas  cd ..\..\Fase2\Cap 6

python main.py

#### 🌾 Objetivo```



Com base nessas análises, a equipe da FarmTech Solutions busca:---

- Entender padrões e comportamentos produtivos regionais  

- Avaliar indicadores de produtividade e sustentabilidade  ## Autores

- Consolidar um painel estatístico com dados de 35 propriedades por região  Phellype Massarente • Carlos Costato • Cesar Azeredo



---## Licença

MIT

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

### 🤖 Fase 2 - Simulação ESP32 (Wokwi)
1. Acesse [wokwi.com](https://wokwi.com)
2. Carregue `Fase2/Cap 1/config/diagram.json`
3. Cole o código de `Fase2/Cap 1/FarmTech.ino`
4. Execute a simulação

### 💼 Fase 2 - Sistema de Gestão
```powershell
cd Fase2\Cap 6
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
