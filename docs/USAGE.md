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

## 💡 Dicas de Uso

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

---

## 📞 Suporte

Consulte [README](../README.md) para mais informações.
