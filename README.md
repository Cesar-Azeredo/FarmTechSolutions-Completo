# 🌾 FarmTech Solutions

Sistema de agricultura de precisão com IoT, análise de dados e automação de irrigação.

---

## 📋 Sobre o Projeto

FarmTech Solutions é um sistema completo para agricultura inteligente que combina:

- 🤖 **IoT com ESP32** - Monitoramento e controle automático de irrigação
- 📊 **Análise de Dados** - Processamento estatístico em Python e R
- 🗄️ **Gestão Completa** - Sistema de gerenciamento com banco de dados Oracle

---

## 📂 Estrutura do Projeto

### 🌱 Fase 1: Gestão de Cultivos e Análise de Dados

#### Python Application (`Fase1/python_app/`)
- ✅ Sistema interativo de gestão para 2 culturas (Banana e Milho)
- ✅ Menu CRUD completo: entrada, saída, atualização e deleção de dados
- ✅ Cálculo automático de área plantada (retângulo, trapézio, círculo)
- ✅ Cálculo de manejo de insumos (Fosfato, Nitrogênio, Potássio, Herbicida, Inseticida)
- ✅ Exportação de dados para CSV
- ✅ Dados organizados em vetores com rotinas de loop e decisão

#### R Statistical Analysis (`Fase1/r_app/`)
- 📈 Análise estatística completa: média, mediana, desvio padrão
- 📊 Análise de distribuição por tipo geométrico e unidade
- 🌦️ Integração com API Open-Meteo para dados meteorológicos (Ir Além)

### 🤖 Fase 2: IoT e Sistemas Integrados

#### Capítulo 1: Sistema IoT com ESP32 (`Fase2/Cap 1/`)
- 🟢 Monitoramento de sensores NPK (Nitrogênio, Fósforo, Potássio) via botões
- 💡 Sensor de pH do solo simulado com LDR
- 🌡️ Sensor de umidade DHT22
- 💧 Controle automático de irrigação via relé
- 🧠 Lógica de decisão baseada em necessidades das culturas
- 🔧 Simulação disponível no Wokwi
- 🚀 Projetos Ir Além: API Python para comunicação serial e análise estatística em R

#### Capítulo 6: Sistema de Gestão Agrícola (`Fase2/Cap 6/`)
- 🏗️ Arquitetura modular em Python
- 📦 Módulos: `cultivo_manager`, `sensor_monitor`, `irrigacao_controller`, `estoque_manager`
- 🗄️ Integração com Oracle Database
- 📄 Persistência de dados em JSON
- 🧪 Suite completa de testes automatizados

#### Capítulo 7: Análise de Dados Reais (`Fase2/Cap 7/`)
- 📊 Dataset com dados de produção agrícola (CONAB/IBGE)
- 📈 Análise estatística completa em R
- 🌾 35 registros de propriedades por região

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Gestão de cultivos, análise e backend
- **R 4.0+** - Análise estatística e visualizações
- **C++/Arduino** - Firmware ESP32
- **Oracle Database 19c** - Banco de dados
- **ESP32** - Microcontrolador IoT
- **Wokwi** - Simulação de hardware

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

### � Fase 1 - Análise R
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

**Phellype Massarente** • **Carlos Costato** • **Cesar Azeredo**

---

## 📄 Licença

MIT
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

