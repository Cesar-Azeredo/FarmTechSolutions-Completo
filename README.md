# 🌾 FarmTech Solutions

> **Sistema inteligente de agricultura de precisão** integrando IoT, análise de dados e machine learning para otimização de cultivos agrícolas.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)
[![ESP32](https://img.shields.io/badge/ESP32-IoT-orange.svg)](https://www.espressif.com/)

---

## 📖 Sobre o Projeto

**FarmTech Solutions** é uma solução completa para **agricultura inteligente**, combinando:

- 🤖 **IoT & Automação** - Sistema de irrigação inteligente com ESP32
- 📊 **Análise de Dados** - Processamento estatístico de dados agrícolas
- 🗄️ **Gestão Completa** - Sistema de gerenciamento com banco de dados Oracle
- 🔬 **Machine Learning** - Modelos preditivos para otimização de cultivos

O sistema monitora **níveis de NPK, pH do solo e umidade** em tempo real, tomando decisões automáticas de irrigação baseadas em dados científicos.

---

## 👥 Autores

<table>
  <tr>
    <td align="center">
      <strong>Phellype Massarente</strong><br>
      <sub>Full Stack Developer</sub>
    </td>
    <td align="center">
      <strong>Carlos Costato</strong><br>
      <sub>Data Scientist</sub>
    </td>
    <td align="center">
      <strong>Cesar Azeredo</strong><br>
      <sub>IoT Engineer</sub>
    </td>
  </tr>
</table>

---

## 🚀 Features

### 🌱 Fase 1: Análise e Predição de Dados

#### Python Application
- ✅ Sistema interativo de cadastro de cultivos (Banana e Milho)
- ✅ Cálculo automático de área plantada (círculo, retângulo, quadrado)
- ✅ Estimativa de insumos necessários por m²
- ✅ Exportação de dados para CSV
- ✅ Validação de entrada e tratamento de erros

#### R Statistical Analysis
- 📊 Análise estatística completa (média, mediana, desvio padrão)
- 📈 Visualizações interativas (histogramas, boxplots)
- 🔍 Distribuição por tipo geométrico e unidade de medida
- 📉 Análise de correlação entre variáveis

---

### 🤖 Fase 2: IoT e Sistemas Integrados

#### Capítulo 1: Sistema IoT com ESP32

**Hardware:**
- ESP32 microcontroller
- Sensores NPK (Nitrogênio, Fósforo, Potássio)
- Sensor de pH do solo (LDR)
- DHT22 (temperatura e umidade)
- Relé para controle de irrigação

**Funcionalidades:**
- ⚡ Leitura de sensores em tempo real
- 🧠 Decisão automática de irrigação
- 📊 Log de dados via Serial Monitor
- 🔧 Calibração baseada em dados científicos (EMBRAPA/IAC)
- 🌐 Suporte para simulação Wokwi

**Projetos Avançados (ir_alem/):**
- 🐍 API Python para comunicação serial com ESP32
- 📈 Modelos preditivos em R para otimização
- 🔗 Integração completa Python + R + ESP32

---

#### Capítulo 6: Sistema de Gestão Agrícola

**Stack Tecnológico:**
- Python 3.8+
- Oracle Database 19c
- Arquitetura modular (MVC)

**Módulos:**
- 🌾 `cultivo_manager` - CRUD de cultivos
- 📡 `sensor_monitor` - Leitura e processamento de sensores
- 💧 `irrigacao_controller` - Lógica de irrigação inteligente
- 📦 `estoque_manager` - Controle de insumos
- 🗄️ `database` - Integração Oracle
- 📄 `file_utils` - Persistência JSON

**Features:**
- ✅ Cadastro completo de cultivos
- ✅ Monitoramento de sensores
- ✅ Decisões automáticas de irrigação
- ✅ Gestão de estoque de insumos
- ✅ Relatórios e exportação de dados
- ✅ Suite completa de testes automatizados

---

#### Capítulo 7: Análise de Dados Reais

**Fonte de Dados:**
- CONAB (Companhia Nacional de Abastecimento)
- IBGE (Instituto Brasileiro de Geografia e Estatística)
- Dados de produção de banana e milho (2024)

**Análises:**
- 📊 Estatística descritiva completa
- 📈 Análise de tendências por região
- 🔍 Testes de normalidade e correlação
- 📉 Visualizações profissionais (ggplot2)
- 📑 Relatórios executivos

---

## 🗂️ Estrutura do Projeto

```
FarmTechSolutions-Completo/
│
├── 📊 Fase1/                       # Análise de Dados
│   ├── python_app/                 # Sistema Python
│   │   ├── main.py                 # App principal
│   │   ├── gerador_exemplos.py    # Gerador de dados de teste
│   │   ├── banana.csv              # Dataset banana
│   │   └── milho.csv               # Dataset milho
│   └── r_app/                      # Análise Estatística R
│       ├── analise.R               # Análise completa
│       └── clima.R                 # Análise climática
│
├── 🤖 Fase2/                       # IoT e Sistemas
│   ├── Cap 1/                      # IoT ESP32
│   │   ├── FarmTech.ino           # Código Arduino
│   │   ├── src/main.cpp           # Código C++
│   │   ├── config/                # Configurações
│   │   │   ├── platformio.ini
│   │   │   ├── wokwi.toml
│   │   │   └── diagram.json
│   │   ├── scripts/               # Scripts auxiliares
│   │   └── ir_alem/               # Projetos avançados
│   │       ├── iralempython/      # API Python
│   │       └── iralemR/           # Modelos ML
│   │
│   ├── Cap 6/                     # Sistema de Gestão
│   │   ├── main.py                # App principal
│   │   ├── test_farmtech.py       # Testes
│   │   ├── modules/               # Módulos
│   │   │   ├── cultivo_manager.py
│   │   │   ├── sensor_monitor.py
│   │   │   ├── irrigacao_controller.py
│   │   │   ├── estoque_manager.py
│   │   │   ├── database.py
│   │   │   └── file_utils.py
│   │   ├── data/                  # Dados JSON
│   │   └── sql/                   # Scripts SQL
│   │
│   └── Cap 7/                     # Análise Estatística
│       ├── analise_R_grupo19.R
│       ├── dados_agronegocio_grupo19.csv
│       └── teste_rapido.R
│
└── 📚 docs/                        # Documentação
    ├── Fase1/                      # Docs Fase 1
    │   ├── INSTALL.md
    │   ├── INSTALL_R.md
    │   ├── TECHNICAL_DOCS.md
    │   └── requirements.txt
    └── Fase2/                      # Docs Fase 2
        ├── Cap1/                   # Docs IoT
        ├── Cap6/                   # Docs Sistema
        └── Cap7/                   # Docs Análise
```

---

## 🛠️ Instalação e Configuração

### Pré-requisitos

- **Python** 3.8 ou superior
- **R** 4.0 ou superior
- **Git** para controle de versão
- **PlatformIO** (opcional, para ESP32)

### Clone do Repositório

```bash
git clone https://github.com/seu-usuario/FarmTechSolutions-Completo.git
cd FarmTechSolutions-Completo
```

---

### 📊 Fase 1 - Setup

#### Python App

```bash
cd Fase1/python_app
python main.py
```

> **Nota:** Sem dependências externas. Usa apenas bibliotecas padrão do Python.

#### R App

```bash
cd Fase1/r_app

# Instalar pacotes R
Rscript -e "install.packages(c('readr', 'ggplot2', 'dplyr', 'tidyverse'))"

# Executar análise
Rscript analise.R
```

---

### 🤖 Fase 2 - Setup

#### Cap 1: IoT ESP32

**Opção 1 - Simulação Online (Wokwi):**

1. Acesse [wokwi.com](https://wokwi.com)
2. Carregue o arquivo `config/diagram.json`
3. Cole o código de `FarmTech.ino`
4. Execute a simulação

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
