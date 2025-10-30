# 🌾 FarmTech Solutions - Projeto Completo

## 📋 Sobre o Projeto

**FarmTech Solutions** é um projeto completo de **agricultura inteligente e de precisão** desenvolvido para a FIAP, integrando IoT, análise de dados, sistemas de gestão e estatística aplicada ao agronegócio brasileiro.

O projeto abrange **duas fases** distintas e complementares, cada uma focando em diferentes aspectos da tecnologia agrícola moderna:

- **Fase 1**: Análise de dados e predições com Python e R
- **Fase 2**: IoT com ESP32, gestão com banco de dados e análise estatística de dados reais

### 👥 Equipe - Grupo 19 FIAP

**Integrantes:**
- **RM566826** - Phellype Matheus Giacoia Flaibam Massarente
- **RM567659** - Maria Luísa Rodrigues Nascimento
- **RM567005** - Carlos Alberto Florindo Costato
- **RM568140** - Cesar Martinho de Azeredo
- **RM568457** - Guilherme Paes Barreto Didier Garcia

**Período:** Setembro a Outubro 2025

---

## 🗂️ Estrutura do Projeto

```
FarmTechSolutions-Completo/
│
├── Fase1/                          # 📊 FASE 1 - Análise de Dados
│   ├── python_app/                 # Aplicação Python
│   │   ├── main.py                 # Sistema principal interativo
│   │   ├── gerador_exemplos.py    # Gerador de dados de teste
│   │   ├── banana.csv              # Base de dados banana
│   │   └── milho.csv               # Base de dados milho
│   │
│   └── r_app/                      # Aplicação R
│       ├── analise.R               # Análise estatística completa
│       └── clima.R                 # Análise climática
│
├── Fase2/                          # 🌱 FASE 2 - IoT e Sistemas
│   ├── Cap 1/                      # IoT com ESP32
│   │   ├── FarmTech.ino            # Código Arduino principal
│   │   ├── src/                    # Código-fonte C++
│   │   │   └── main.cpp
│   │   ├── config/                 # Arquivos de configuração
│   │   │   ├── platformio.ini      # Config PlatformIO
│   │   │   ├── wokwi.toml          # Config Wokwi
│   │   │   ├── diagram.json        # Diagrama circuito
│   │   │   └── .gitignore
│   │   ├── scripts/                # Scripts opcionais
│   │   │   ├── opcional_python_api.py
│   │   │   └── opcional_analise_r.R
│   │   ├── docs/                   # Resultados e documentação
│   │   │   └── resultados_analise_irrigacao.csv
│   │   └── ir_alem/                # Projetos avançados
│   │       ├── iralempython/       # Integração Python
│   │       └── iralemR/            # Modelos preditivos R
│   │
│   ├── Cap 6/                      # Sistema de Gestão Python
│   │   ├── main.py                 # Aplicação principal
│   │   ├── test_farmtech.py        # Suite de testes
│   │   ├── modules/                # Módulos organizados
│   │   │   ├── cultivo_manager.py
│   │   │   ├── database.py         # Integração Oracle
│   │   │   ├── estoque_manager.py
│   │   │   ├── file_utils.py
│   │   │   ├── irrigacao_controller.py
│   │   │   └── sensor_monitor.py
│   │   ├── data/                   # Arquivos JSON
│   │   │   ├── cultivos.json
│   │   │   ├── estoque.json
│   │   │   ├── irrigacoes.json
│   │   │   └── sensores.json
│   │   └── sql/                    # Scripts SQL
│   │       ├── create_tables.sql
│   │       └── seed_data.sql
│   │
│   └── Cap 7/                      # Análise Estatística R
│       ├── analise_R_grupo19.R     # Análise completa
│       ├── dados_agronegocio_grupo19.csv
│       ├── RESUMO_EXECUTIVO.md     # Relatório executivo
│       └── teste_rapido.R          # Testes rápidos
│
└── docs/                           # 📚 DOCUMENTAÇÃO TÉCNICA
    ├── Fase1/                      # Docs Fase 1
    │   ├── INSTALL.md              # Guia instalação Python
    │   ├── INSTALL_R.md            # Guia instalação R
    │   ├── EXEMPLOS_R.md           # Exemplos práticos R
    │   ├── TECHNICAL_DOCS.md       # Docs técnicas Python
    │   ├── TECHNICAL_DOCS_R.md     # Docs técnicas R
    │   ├── requirements.txt        # Dependências Python
    │   └── requirements_r.txt      # Dependências R
    │
    └── Fase2/                      # Docs Fase 2
        ├── Cap1/                   # Docs IoT ESP32
        │   ├── CALIBRACAO_LDR_WOKWI.md
        │   ├── GUIA_RAPIDO_SCREENSHOTS.md
        │   ├── RELACAO_NPK_PH.md
        │   ├── RESUMO_v2.0.md
        │   ├── TABELA_LUX_PH_COMPORTAMENTO.md
        │   └── images/             # Diagramas e screenshots
        │
        ├── Cap6/                   # Docs Sistema Gestão
        │   ├── INSTALACAO_ORACLE.md
        │   ├── INTEGRACAO_ESP32.md
        │   ├── LOGICA_IRRIGACAO.md
        │   ├── REQUISITOS_NPK.md
        │   └── requirements.txt    # Dependências Python
        │
        └── Cap7/                   # Docs Análise Estatística
            ├── FONTES_DADOS_REAIS.md
            └── GUIA_INSTALACAO_R.md
```

---

## 🚀 FASE 1 - Análise e Predição de Dados Agrícolas

### 📊 Python App - Sistema Interativo de Gestão

**Objetivo:** Sistema completo para cadastro, análise e gestão de dados agrícolas de **banana** e **milho**.

#### Funcionalidades:
- ✅ Entrada de dados interativa com validação
- ✅ Cálculo automático de área (círculo, retângulo, quadrado)
- ✅ Cálculo de quantidade de insumos baseado em área
- ✅ Exportação para CSV
- ✅ Visualização de estatísticas
- ✅ Interface amigável com sistema de navegação

#### Tecnologias:
- Python 3.6+
- Bibliotecas: `csv`, `os`, `re`

#### Como Executar:
```bash
cd Fase1/python_app
python main.py
```

#### Exemplo de Uso:
1. Selecione `1. Entrada de dados`
2. Escolha cultura (Banana ou Milho)
3. Insira medidas (comprimento, largura, raio)
4. Sistema calcula área e insumos automaticamente
5. Dados salvos em `banana.csv` ou `milho.csv`

---

### 📈 R App - Análise Estatística Avançada

**Objetivo:** Análise estatística completa dos dados exportados pelo Python.

#### Funcionalidades:
- ✅ Cálculo de média e desvio padrão
- ✅ Análise de distribuição por tipo geométrico
- ✅ Análise de percentuais por unidade de medida
- ✅ Estatísticas de área e insumos
- ✅ Visualizações gráficas (histogramas, boxplots)

#### Tecnologias:
- R 4.0+
- Pacotes: `readr`, `ggplot2`, `dplyr`

#### Como Executar:
```bash
cd Fase1/r_app
Rscript analise.R
```

---

## 🌱 FASE 2 - IoT, Gestão e Análise de Dados Reais

### Cap 1 - IoT com ESP32 e Sensores

**Objetivo:** Sistema de **irrigação inteligente** baseado em sensores NPK, pH e umidade do solo.

#### 🔧 Hardware (Simulação Wokwi):
- **ESP32** - Microcontrolador principal
- **3 Botões Verdes** - Simulam sensores NPK (Nitrogênio, Fósforo, Potássio)
- **LDR** - Simula sensor de pH (0-14)
- **DHT22** - Sensor de temperatura e umidade do solo
- **Relé Azul** - Controla bomba d'água para irrigação

#### 🧠 Lógica de Decisão:
1. Lê sensores NPK e pH do solo
2. Monitora umidade do solo via DHT22
3. Compara valores com limites ideais para cada cultura
4. **Liga/desliga irrigação automaticamente**
5. Exibe dados no Serial Monitor a cada 5 segundos

#### 📊 Dados Científicos:
- Baseado em pesquisas **EMBRAPA** e **IAC**
- Tabelas de dosagem NPK para banana e milho
- Limites de pH e umidade por cultura

#### Como Simular:
1. Acesse [Wokwi.com](https://wokwi.com)
2. Abra o arquivo `diagram.json`
3. Carregue `FarmTech.ino` ou `src/main.cpp`
4. Execute a simulação
5. Pressione botões NPK e observe relé de irrigação

#### 🔗 Projetos Avançados (ir_alem/):
- **Python API** - Comunicação serial com ESP32
- **Modelos Preditivos R** - Machine learning para otimização de irrigação
- **Integração completa** - Python + R + ESP32

---

### Cap 6 - Sistema de Gestão Agrícola com Oracle

**Objetivo:** Sistema Python completo para gestão de **cultivos**, **sensores**, **irrigação** e **estoque** com banco de dados Oracle.

#### 💡 Funcionalidades:
- ✅ **Cadastro de Cultivos** - Nome, área, tipo, data de plantio
- ✅ **Monitoramento de Sensores** - Simulação de leituras NPK, pH, umidade
- ✅ **Controle de Irrigação** - Decisão automática baseada em regras
- ✅ **Gestão de Estoque** - Controle de insumos agrícolas
- ✅ **Relatórios** - Exportação JSON e relatórios consolidados
- ✅ **Integração Oracle** - Conexão com banco de dados corporativo
- ✅ **Suite de Testes** - Testes automatizados para cada módulo

#### 🏗️ Arquitetura:
```
main.py                 # Interface principal
├── modules/
│   ├── cultivo_manager.py       # CRUD cultivos
│   ├── sensor_monitor.py        # Leitura de sensores
│   ├── irrigacao_controller.py  # Lógica de irrigação
│   ├── estoque_manager.py       # Gestão de estoque
│   ├── database.py              # Integração Oracle
│   └── file_utils.py            # Utilitários arquivos
└── data/                        # Persistência JSON
```

#### Tecnologias:
- Python 3.8+
- Oracle Database 19c
- Bibliotecas: `json`, `datetime`, `cx_Oracle`

#### Como Executar:
```bash
cd Fase2/Cap\ 6
python main.py
```

#### Como Testar:
```bash
python test_farmtech.py
```

---

### Cap 7 - Análise Estatística de Dados Reais do Agronegócio

**Objetivo:** Análise estatística completa de dados reais de **produção de banana e milho** por região brasileira.

#### 📊 Fontes de Dados:
- **CONAB** - Companhia Nacional de Abastecimento
- **IBGE** - Instituto Brasileiro de Geografia e Estatística
- Dados de 2024 consolidados

#### 🔬 Análises Realizadas:

**1. Variáveis Quantitativas:**
- Área plantada (hectares)
- Produção (toneladas)
- Produtividade (ton/ha)

**2. Variáveis Qualitativas:**
- Distribuição por cultura
- Distribuição por região
- Análise de safras

**3. Métodos Estatísticos:**
- Média, mediana, moda
- Desvio padrão e variância
- Quartis e amplitude
- Coeficiente de variação
- Teste de normalidade
- Análise de correlação

#### 📈 Visualizações:
- Histogramas
- Boxplots
- Gráficos de barras
- Gráficos de dispersão
- Tabelas de frequência

#### Como Executar:
```bash
cd Fase2/Cap\ 7
Rscript analise_R_grupo19.R
```

#### Relatório:
Veja `RESUMO_EXECUTIVO.md` para insights e conclusões.

---

## 📦 Instalação e Dependências

### Fase 1 - Python

```bash
cd Fase1/python_app
# Sem dependências externas - usa apenas bibliotecas padrão do Python
python main.py
```

### Fase 1 - R

```bash
cd Fase1/r_app
# Instalar pacotes necessários
Rscript -e "install.packages(c('readr', 'ggplot2', 'dplyr'))"
Rscript analise.R
```

### Fase 2 - Cap 1 (ESP32)

**Opção 1 - Simulação Wokwi:**
- Acesse [wokwi.com](https://wokwi.com)
- Carregue `diagram.json`
- Execute online

**Opção 2 - PlatformIO:**
```bash
cd Fase2/Cap\ 1
pio run
pio device monitor
```

### Fase 2 - Cap 6 (Sistema Python)

```bash
cd Fase2/Cap\ 6
# Ver docs/Fase2/Cap6/requirements.txt para dependências
pip install cx_Oracle
python main.py
```

### Fase 2 - Cap 7 (Análise R)

```bash
cd Fase2/Cap\ 7
# Ver docs/Fase2/Cap7/GUIA_INSTALACAO_R.md
Rscript analise_R_grupo19.R
```

---

## 📚 Documentação Completa

Toda a documentação técnica está organizada na pasta `docs/`:

### Fase 1:
- **INSTALL.md** - Guia de instalação Python
- **INSTALL_R.md** - Guia de instalação R
- **TECHNICAL_DOCS.md** - Documentação técnica Python
- **TECHNICAL_DOCS_R.md** - Documentação técnica R
- **EXEMPLOS_R.md** - Exemplos práticos em R

### Fase 2:
- **Cap1/** - Calibração sensores, guias de uso, tabelas NPK/pH
- **Cap6/** - Instalação Oracle, integração ESP32, lógica de irrigação
- **Cap7/** - Fontes de dados, guia de instalação R

---

## 🛠️ Tecnologias Utilizadas

### Linguagens:
- **Python** 3.6+ (análise, IoT, gestão)
- **R** 4.0+ (estatística, visualizações)
- **C++** (Arduino/ESP32)
- **SQL** (Oracle Database)

### Frameworks e Ferramentas:
- **PlatformIO** - Desenvolvimento ESP32
- **Wokwi** - Simulação de circuitos
- **Oracle Database 19c** - Banco de dados corporativo
- **Arduino IDE** - Programação ESP32

### Bibliotecas Python:
- `csv`, `os`, `re` - Manipulação de dados
- `json`, `datetime` - Persistência e tempo
- `cx_Oracle` - Conexão Oracle

### Pacotes R:
- `readr` - Leitura de dados
- `ggplot2` - Visualizações
- `dplyr` - Manipulação de dados
- `tidyverse` - Ecossistema completo

### Hardware IoT:
- ESP32 (microcontrolador)
- Sensores NPK simulados
- Sensor pH (LDR)
- DHT22 (temperatura/umidade)
- Relé (controle irrigação)

---

## 🎯 Resultados e Impacto

### Fase 1:
✅ Sistema completo de cadastro e análise de cultivos  
✅ Análise estatística automatizada  
✅ Exportação e visualização de dados  
✅ Base para decisões agrícolas

### Fase 2:
✅ Irrigação inteligente e automatizada  
✅ Sistema de gestão completo com Oracle  
✅ Análise de dados reais do agronegócio brasileiro  
✅ Integração IoT + Cloud + Analytics

### Aprendizados:
- Aplicação prática de IoT na agricultura
- Análise estatística de dados reais
- Integração de múltiplas tecnologias
- Desenvolvimento de sistemas completos

---

## 👨‍💻 Desenvolvimento e Contribuição

### Estrutura de Branches:
- `main` - Versão estável e funcional
- `develop` - Desenvolvimento ativo

### Padrões de Código:
- Python: PEP 8
- R: tidyverse style guide
- C++: Arduino style guide

---

## 📄 Licença

Projeto acadêmico desenvolvido para FIAP - Faculdade de Informática e Administração Paulista.

**Grupo 19** - 1º ano • 2025/2  
Todos os direitos reservados aos autores.

---

## 📞 Contato

**FIAP - Grupo 19**

Para dúvidas, sugestões ou contribuições, entre em contato com os membros do grupo através do portal FIAP.

---

## 🙏 Agradecimentos

- **FIAP** - Pela infraestrutura e suporte acadêmico
- **EMBRAPA** - Dados técnicos sobre cultivos
- **CONAB/IBGE** - Dados estatísticos reais
- **Comunidade Open Source** - Bibliotecas e ferramentas

---

**🌾 FarmTech Solutions - Tecnologia a serviço da agricultura brasileira! 🇧🇷**

## 🗂️ Estrutura do Projeto

```
FarmTechSolutions-Completo/
├── Fase1/               # Primeira fase - Análise de dados e predições
│   ├── python_app/      # Aplicação Python para análise
│   │   ├── main.py
│   │   ├── gerador_exemplos.py
│   │   ├── requirements.txt
│   │   └── *.csv (dados de cultivos)
│   └── r_app/           # Aplicação R para modelagem estatística
│       ├── analise.R
│       ├── clima.R
│       └── requirements_r.txt
│
├── Fase2/               # Segunda fase - IoT e Sistema Completo
│   ├── Cap 1/           # IoT com ESP32 e sensores
│   │   ├── FarmTech.ino
│   │   ├── platformio.ini
│   │   ├── src/main.cpp
│   │   └── ir_alem/     # Projetos avançados
│   ├── Cap 6/           # Sistema Python com banco de dados Oracle
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── requirements.txt
│   │   └── data/        # Arquivos JSON
│   └── Cap 7/           # Análise estatística de dados do agronegócio
│       ├── analise_R_grupo19.R
│       ├── dados_agronegocio_grupo19.csv
│       └── graficos/
│
└── docs/                # Documentação técnica completa
    ├── Fase1/           # Guias de instalação e uso
    │   ├── INSTALL.md
    │   ├── INSTALL_R.md
    │   ├── EXEMPLOS_R.md
    │   ├── TECHNICAL_DOCS.md
    │   └── TECHNICAL_DOCS_R.md
    └── Fase2/           # Documentação por capítulo
        ├── Cap1/        # Calibração, guias, tabelas
        ├── Cap6/        # Instalação Oracle, integrações
        └── Cap7/        # Fontes de dados, instalação R
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
