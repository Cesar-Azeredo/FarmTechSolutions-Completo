# 📦 Guia de Instalação - FarmTech Solutions

## 🛠️ Pré-requisitos

### Software Necessário

- **Python** 3.8 ou superior
- **R** 4.0 ou superior  
- **Git** para controle de versão
- **PlatformIO** (opcional, para ESP32)

---

## 📥 Instalação

### 1. Clone do Repositório

```bash
git clone https://github.com/seu-usuario/FarmTechSolutions-Completo.git
cd FarmTechSolutions-Completo
```

---

## 🐍 Fase 1 - Python

### Python App

```bash
cd Fase1/python_app
python main.py
```

**Nota:** Usa apenas bibliotecas padrão do Python (csv, os, re).

---

## 📊 Fase 1 - R

### R App

```bash
cd Fase1/r_app

# Instalar pacotes necessários
Rscript -e "install.packages(c('readr', 'ggplot2', 'dplyr'))"

# Executar análise
Rscript analise.R
```

---

## 🤖 Fase 2 - ESP32 (Cap 1)

### Opção 1: Simulação Wokwi (Recomendado)

1. Acesse [wokwi.com](https://wokwi.com)
2. Carregue o arquivo `config/diagram.json`
3. Cole o código de `FarmTech.ino`
4. Execute a simulação

### Opção 2: Hardware Real (PlatformIO)

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

## 🗄️ Fase 2 - Sistema de Gestão (Cap 6)

### Instalação

```bash
cd Fase2/Cap\ 6

# Instalar dependências (se necessário)
pip install cx_Oracle

# Executar aplicação
python main.py
```

### Testes

```bash
python test_farmtech.py
```

---

## 📈 Fase 2 - Análise Estatística (Cap 7)

```bash
cd Fase2/Cap\ 7

# Executar análise completa
Rscript analise_R_grupo19.R
```

---

## 📊 Fase 3 - Dashboard Oracle/Streamlit

### Instalação de Dependências

```powershell
cd Fase3
pip install -r requirements.txt
```

**Dependências incluídas:**
- `streamlit` - Framework de dashboard
- `oracledb` - Driver Oracle (não requer Instant Client)
- `pandas` - Manipulação de dados
- `plotly` - Visualizações interativas
- `python-dotenv` - Gerenciamento de variáveis de ambiente

### Configuração Oracle

**Opção 1: Variáveis de Ambiente (Recomendado)**

```powershell
# Temporário (sessão atual)
$env:ORACLE_USER="RM566826"
$env:ORACLE_PASSWORD="161083"

# Persistente (todas as sessões)
setx ORACLE_USER "RM566826"
setx ORACLE_PASSWORD "161083"
```

**Opção 2: Editar arquivo de configuração**

Edite `scripts/dashboard.py` e atualize as credenciais (não recomendado para produção).

### Teste de Conexão

```powershell
python scripts\test_connection.py
```

**Saída esperada:**
- ✅ Conexão estabelecida
- ✅ Tabela SENSORES encontrada
- ✅ Contagem de registros

---

## ✅ Verificação da Instalação

### Checklist

- [ ] Python executa sem erros
- [ ] R scripts rodam corretamente
- [ ] ESP32 compila/simula
- [ ] Sistema de gestão inicia
- [ ] Análise R gera gráficos
- [ ] Dashboard Streamlit conecta ao Oracle
- [ ] Visualizações aparecem corretamente

---

## 🐛 Troubleshooting

### Python

- Verifique a versão: `python --version`
- Instale pip se necessário

### R

- Verifique a versão: `R --version`
- Instale RStudio se preferir interface gráfica

### ESP32

- Verifique drivers USB
- Configure a porta serial correta no PlatformIO

### Oracle/Streamlit (Fase 3)

- **Erro de conexão:** Verifique credenciais (RM e data de nascimento DDMMAA)
- **Erro DPI-1047:** Certifique-se de usar `oracledb` (não `cx_Oracle`)
- **Dashboard não abre:** Verifique se a porta 8501 está disponível
- **Dados não aparecem:** Execute `test_connection.py` para validar tabela SENSORES

---

## 📞 Suporte

Para problemas, consulte o [README principal](../README.md).
