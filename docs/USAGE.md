# 📖 Guia de Uso - FarmTech Solutions

## 🌱 Fase 1: Análise de Dados

### Python App - Gestão de Cultivos

**Iniciar:**
```bash
cd Fase1/python_app
python main.py
```

**Funcionalidades:**

1. **Entrada de Dados**
   - Escolha cultura (Banana ou Milho)
   - Insira dimensões (comprimento, largura, raio)
   - Sistema calcula área e insumos automaticamente

2. **Visualização de Dados**
   - Exibe registros cadastrados
   - Mostra estatísticas

3. **Saída**
   - Digite 'X' para voltar
   - Dados salvos em CSV automaticamente

---

### R App - Análise Estatística

**Executar:**
```bash
cd Fase1/r_app
Rscript analise.R
```

**Saídas:**
- Estatísticas descritivas no console
- Média, desvio padrão, percentuais
- Análise por tipo geométrico

---

## 🤖 Fase 2: IoT e Sistemas

### Cap 1 - ESP32 IoT

**Wokwi (Online):**
1. Acesse wokwi.com
2. Carregue diagram.json
3. Cole FarmTech.ino
4. Pressione Play
5. Observe Serial Monitor

**Sensores:**
- Botões NPK (3x)
- LDR (pH)
- DHT22 (umidade)
- Relé (irrigação)

**Leitura:**
- Dados atualizados a cada 5 segundos
- Decisão automática de irrigação

---

### Cap 6 - Sistema de Gestão

**Iniciar:**
```bash
cd Fase2/Cap\ 6
python main.py
```

**Menu Principal:**

1. Cadastrar Cultivo
2. Listar Cultivos
3. Monitorar Sensores
4. Verificar Irrigação
5. Gestão de Estoque
6. Relatórios
7. Banco de Dados
8. Sair

**Dados:**
- Persistência em JSON (`data/`)
- Opcional: integração Oracle

---

### Cap 7 - Análise Estatística

**Executar:**
```bash
cd Fase2/Cap\ 7
Rscript analise_R_grupo19.R
```

**Análises:**
- Estatística descritiva
- Distribuições
- Correlações
- Testes de normalidade
- Visualizações (gráficos automáticos)

---

## � Fase 3: Dashboard Oracle/Streamlit

### Executar Dashboard

**Iniciar:**
```powershell
cd Fase3
streamlit run scripts\dashboard.py
```

**Acesso:**
- URL: `http://localhost:8501`
- Abre automaticamente no navegador padrão

---

### Funcionalidades do Dashboard

#### 1️⃣ **Métricas em Tempo Real**
- Temperatura ambiente
- Umidade do solo
- pH do solo
- Pressão atmosférica
- Níveis de NPK (Nitrogênio, Fósforo, Potássio)

#### 2️⃣ **Visualizações Interativas**
- Gráficos de linha (evolução temporal)
- Indicadores de status (irrigação ON/OFF)
- Distribuição de dados
- Correlações entre variáveis

#### 3️⃣ **Sugestões Inteligentes**
O sistema analisa condições e sugere:
- **Irrigação** quando umidade < 40%
- **Verificação** quando temperatura > 30°C
- **Fertilização** quando NPK baixo
- **Correção de pH** quando fora do ideal (6.0-7.0)

#### 4️⃣ **Filtros e Controles**
- Selecionar período de análise
- Filtrar por cultura (Banana, Milho, etc.)
- Ajustar escala de gráficos

---

### Scripts Auxiliares

#### Teste de Conexão
```powershell
python scripts\test_connection.py
```
**Valida:**
- Conexão com Oracle
- Existência da tabela SENSORES
- Estrutura de colunas

#### Verificação de Normalização
```powershell
python scripts\check_normalization.py
```
**Exibe:**
- Medianas antes/depois da normalização
- Ajustes de escala aplicados
- Última leitura normalizada

#### Exportar Evidências
```powershell
python scripts\export_evidence.py
```
**Gera:**
- CSV com amostra de dados
- Relatório de validação

---

### Estrutura de Dados (Tabela SENSORES)

| Coluna | Descrição | Tipo |
|--------|-----------|------|
| `DATA` | Data da leitura | DATE |
| `HORA` | Hora da leitura | NUMBER |
| `TEMPERATURA` | Temperatura (°C) | NUMBER |
| `UMIDADE_SOLO` | Umidade do solo (%) | NUMBER |
| `PH_SOLO` | pH do solo | NUMBER |
| `PRECIPITACAO` | Precipitação (mm) | VARCHAR2 |
| `UMIDADE_AR` | Umidade do ar (%) | NUMBER |
| `VENTO_KMH` | Velocidade do vento | VARCHAR2 |
| `PRESSAO_ATMOSFERICA` | Pressão (hPa) | NUMBER |
| `NITROGENIO_OK` | Status N (TRUE/FALSE) | VARCHAR2 |
| `FOSFORO_OK` | Status P (TRUE/FALSE) | VARCHAR2 |
| `POTASSIO_OK` | Status K (TRUE/FALSE) | VARCHAR2 |
| `IRRIGACAO_REALIZADA` | Status irrigação | VARCHAR2 |
| `CULTURA` | Tipo de cultura | VARCHAR2 |
| `PRODUTIVIDADE` | Produtividade (%) | NUMBER |

---

## �💡 Dicas de Uso

### Python
- Use 'X' para navegar entre menus
- Dados são salvos automaticamente em CSV
- Validação de entrada evita erros

### R
- Gráficos salvos no diretório atual
- Verifique paths de arquivos CSV
- Use RStudio para visualizações interativas

### ESP32
- Ajuste limites de sensores conforme necessário
- Serial Monitor mostra decisões em tempo real
- Simule eventos pressionando botões

### Dashboard (Fase 3)
- Recarregue a página para atualizar dados
- Use filtros para focar em períodos específicos
- Consulte métricas em tempo real na barra lateral
- Exporte dados para análise offline

---

## 📊 Interpretação de Resultados

### Análise Estatística
- **Média**: Tendência central
- **Desvio Padrão**: Variabilidade
- **Correlação**: Relação entre variáveis

### IoT
- **NPK**: Níveis de nutrientes
- **pH**: Acidez/alcalinidade do solo
- **Umidade**: Percentual de água no solo
- **Irrigação**: ON/OFF baseado em limites

---

## 🐛 Problemas Comuns

### "Arquivo não encontrado"
- Verifique o diretório atual
- Use caminhos absolutos se necessário

### "Módulo não encontrado"
- Instale dependências: `pip install <pacote>`
- Para R: `install.packages("<pacote>")`

### "Erro de sintaxe"
- Verifique versão Python/R
- Confira encoding de arquivos (UTF-8)

### "Erro de conexão Oracle" (Fase 3)
- Verifique variáveis de ambiente (`ORACLE_USER`, `ORACLE_PASSWORD`)
- Confirme formato da senha: DDMMAA (6 dígitos)
- Teste conectividade: `Test-NetConnection oracle.fiap.com.br -Port 1521`

### "Tabela SENSORES não encontrada"
- Execute importação de dados no Oracle SQL Developer
- Verifique nome da tabela (deve ser `SENSORES`)
- Execute `test_connection.py` para validar

---

## 📞 Suporte

Consulte [README](../README.md) para mais informações.
