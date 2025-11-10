# 📊 Fase 3 - Dashboard e Integração Oracle

## 📋 Funcionalidades

- **Níveis de Umidade, P, K e pH**: Gráficos em tempo real dos sensores
- **Status da Irrigação**: Indicadores visuais do sistema de irrigação
- **Sugestões de Irrigação**: Recomendações baseadas em condições climáticas
- **Métricas Climáticas**: Temperatura, umidade do ar, precipitação, vento, pressão
- **Produtividade**: Acompanhamento da produtividade estimada

---

## 🚀 Como Executar

### 1. Instalar Dependências

```powershell
cd Fase3
pip install -r requirements.txt
```

**Nota**: O `oracledb` (nova versão do cx_Oracle) é usado e não requer Oracle Instant Client para conexões básicas.

---

### 2. Configurar Conexão Oracle

**IMPORTANTE**: Configure credenciais usando variáveis de ambiente (recomendado):

#### PowerShell (temporário nesta sessão):
```powershell
$env:ORACLE_USER="RM566826"
$env:ORACLE_PASSWORD="161083"
```

#### Para persistir (user-level):
```powershell
setx ORACLE_USER "RM566826"
setx ORACLE_PASSWORD "161083"
# Abra uma nova janela do PowerShell para ver as variáveis
```

---

### 3. Testar Conexão

```powershell
python scripts\test_connection.py
```

Este script testa a conexão com o banco Oracle. Se der erro de senha, verifique se você colocou a data de nascimento correta.

---

### 4. Executar Dashboard

```powershell
streamlit run scripts\dashboard.py
```

O dashboard será aberto no navegador padrão em `http://localhost:8501`.

---

## 🔧 Configuração do Banco Oracle

- **Usuário**: RM (exemplo: RM566826)
- **Senha**: Sua data de nascimento (DDMMAA - 6 dígitos)
- **Host**: oracle.fiap.com.br
- **Porta**: 1521
- **SID**: ORCL
- **Tabela**: SENSORES

---

## 📊 Estrutura dos Dados

A tabela `SENSORES` contém as seguintes colunas principais:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `DATA` | DATE | Data da leitura |
| `HORA` | NUMBER | Hora da leitura |
| `TEMPERATURA` | NUMBER | Temperatura ambiente (°C) |
| `UMIDADE_SOLO` | NUMBER | Umidade do solo (%) |
| `PH_SOLO` | NUMBER | pH do solo |
| `PRECIPITACAO` | VARCHAR2 | Precipitação (mm) |
| `UMIDADE_AR` | NUMBER | Umidade do ar (%) |
| `VENTO_KMH` | VARCHAR2 | Velocidade do vento (km/h) |
| `PRESSAO_ATMOSFERICA` | NUMBER | Pressão atmosférica (hPa) |
| `NITROGENIO_OK` | VARCHAR2 | Status de Nitrogênio (TRUE/FALSE) |
| `FOSFORO_OK` | VARCHAR2 | Status de Fósforo (TRUE/FALSE) |
| `POTASSIO_OK` | VARCHAR2 | Status de Potássio (TRUE/FALSE) |
| `IRRIGACAO_REALIZADA` | VARCHAR2 | Status da irrigação (TRUE/FALSE) |
| `CULTURA` | VARCHAR2 | Tipo de cultura (Banana, Milho, etc.) |
| `FONTE_DADOS` | VARCHAR2 | Fonte dos dados |
| `PRODUTIVIDADE` | NUMBER | Produtividade estimada (%) |

---

## 💡 Lógica de Sugestões

O sistema analisa as condições atuais e sugere ações baseadas em:

- **Umidade do solo** < 40%: Irrigação recomendada
- **Temperatura** > 30°C: Verificar irrigação
- **Sem precipitação** + **Ar seco**: Irrigação necessária
- **Pressão baixa**: Possível mudança climática
- **Nutrientes baixos**: Recomendar fertilização
- **pH fora do ideal** (6.0-7.0): Correção necessária

---

## 📁 Estrutura de Arquivos

```
Fase3/
├── data/                          # Dados CSV para testes
│   ├── dados_teste_ir_alem2.csv
│   └── demo_dados_r.csv
├── scripts/                       # Scripts Python
│   ├── dashboard.py               # Dashboard Streamlit principal
│   ├── test_connection.py         # Teste de conexão Oracle
│   ├── check_normalization.py     # Verificação de normalização
│   ├── data_load_test.py          # Teste de carga de dados
│   ├── export_evidence.py         # Exportação de evidências
│   └── publish_to_github.ps1      # Script de publicação
├── sql/                           # Scripts SQL
│   └── sql.txt                    # Consultas Oracle
├── requirements.txt               # Dependências Python
└── start_dashboard.bat            # Inicializador Windows
```

---

## 🛠️ Requisitos do Sistema

- **Python 3.8+**
- **Conexão com internet** (para acessar oracle.fiap.com.br)
- **Dependências** (instaladas via `requirements.txt`):
  - `streamlit`
  - `oracledb`
  - `pandas`
  - `plotly`
  - `python-dotenv`

---

## 🐛 Troubleshooting

### Erro de conexão Oracle
- Verifique se as variáveis de ambiente estão definidas corretamente
- Confirme se a senha (data de nascimento) está no formato DDMMAA
- Teste a conectividade: `Test-NetConnection oracle.fiap.com.br -Port 1521`

### Erro DPI-1047
- Certifique-se de que o `oracledb` está instalado corretamente
- Use o modo "thin" (padrão) que não requer Oracle Instant Client

### Dashboard não abre
- Verifique se a porta 8501 está disponível
- Execute: `streamlit run scripts\dashboard.py --server.port 8502`

---

## 📞 Suporte

Para dúvidas ou problemas:
- Execute `python scripts\test_connection.py` para verificar a conexão
- Consulte os logs do Streamlit no terminal
- Verifique a documentação principal em [`docs/README.md`](README.md)

---

**Equipe FarmTech Solutions**  
Phellype Massarente • Carlos Costato • Cesar Azeredo
