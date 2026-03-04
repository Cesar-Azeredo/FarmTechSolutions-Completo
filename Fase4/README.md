# Fase 4 - Machine Learning e Previsões Inteligentes na Agricultura

A Fase 4 marca a consolidação do conhecimento técnico adquirido ao longo das fases anteriores, aplicando **Inteligência Artificial** diretamente sobre os dados agrícolas coletados, estruturados e armazenados.

## Estrutura da Fase 4

### 📁 Sklearn/
**Atividade: Classificação de Grãos com Machine Learning**

Introdução ao aprendizado de máquina supervisionado através da classificação de variedades de grãos de trigo usando o **Seeds Dataset**.

**Conteúdo:**
- `wheat_classification.ipynb` - Notebook com análise completa do dataset
- `seeds_dataset.txt` - Dataset com 210 amostras de grãos (Kama, Rosa, Canadian)

**Objetivos:**
1. Análise e pré-processamento de dados
2. Implementação de múltiplos algoritmos de classificação:
   - K-Nearest Neighbors (KNN)
   - Support Vector Machine (SVM)
   - Random Forest
   - Naive Bayes
   - Logistic Regression
3. Otimização de modelos com Grid Search/Randomized Search
4. Interpretação e visualização de resultados

**Metodologia:** CRISP-DM (Cross Industry Standard Process for Data Mining)

---

### 📁 Dados/
**Atividade: Previsão Inteligente e Dashboard Agrícola**

Integração completa de Machine Learning com dados reais/simulados de sensores IoT para criar um sistema de previsão agrícola inteligente.

**Conteúdo principal:**
- `database/` - Modelos do banco de dados para armazenar dados de sensores
- `cursotiaor/` - Aplicações de integração e processamento
- `logs_irrigacao_api.json` - Exemplo de dados de irrigação
- `git-fase4.txt` - Documentação de configuração

**Objetivos:**

#### PARTE 1 - Integração de ML com Streamlit
- Pipeline completo de ML com Scikit-Learn
- Dashboard interativo em Streamlit
- Visualização de métricas, correlações e previsões em tempo real
- Acesso por gestores agrícolas

#### PARTE 2 - Algoritmos Preditivos
- Treinamento de modelos de regressão (linear, múltipla, não-linear)
- Previsões sobre:
  - Volume de irrigação
  - Necessidade de fertilização
  - Estimativa de rendimento
- Avaliação com métricas: MAE, MSE, RMSE, R²
- Documentação e visualizações de resultados

#### IR ALÉM 1 - Integração IoT com Banco de Dados
- Modelo de banco de dados scalable
- Ingestão automática de dados de sensores reais ou Wokwi
- Arquitetura baseada em Cognitive Data Science

#### IR ALÉM 2 - Dashboard Analítico Interativo
- Dashboard visual com previsões interativas
- Gráficos de correlação e tendências
- Interface amigável para decisões agrícolas
- Alternativas: Streamlit, Power BI ou React Native

---

## Tecnologias Utilizadas

### Machine Learning
- **Scikit-Learn** - Modelos de classificação e regressão
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Matplotlib/Seaborn** - Visualizações estáticas

### Dashboard & Interface
- **Streamlit** - Dashboard interativo
- **Plotly** - Gráficos interativos (opcional)
- **React Native** (IR ALÉM) - Interface mobile

### Banco de Dados
- **SQL** - Armazenamento estruturado de dados agrícolas
- **SQLAlchemy** - ORM para Python

### IoT & Integração
- **Wokwi** - Simulação de sensores
- **Arduino/C++** - Lógica de sugestões de ação
- **API REST** - Integração entre componentes

---

## Fluxo de Dados

```
Sensores (Real/Wokwi) 
    ↓
Banco de Dados Agrícola
    ↓
Pré-processamento (Pandas)
    ↓
Modelos ML (Scikit-Learn)
    ↓
Previsões & Recomendações
    ↓
Dashboard Streamlit
    ↓
Gestor Agrícola (Decisões)
```

---

## Critérios de Avaliação

### Avaliação Principal (10 pontos)
- **Qualidade da integração** ML + Dashboard Streamlit (3 pts)
- **Aplicação correta** de modelos de regressão (3 pts)
- **Clareza na apresentação** de resultados e métricas (2 pts)
- **Domínio técnico** na demonstração em vídeo (2 pts)

### Avaliação IR ALÉM
- **Funcionalidade** e coerência da integração (sensores → BD → IA)
- **Criatividade** e relevância para o contexto agrícola
- **Usabilidade** e estética das interfaces
- **Clareza técnica** nas demonstrações

---

## Próximas Passos

1. **Executar análise exploratória** do Seeds Dataset em `Sklearn/`
2. **Treinar múltiplos modelos** e comparar desempenho
3. **Otimizar hiperparâmetros** dos modelos
4. **Integrar dados reais** do banco de dados em `Dados/`
5. **Desenvolver dashboard** em Streamlit
6. **Gerar previsões** e recomendações agrícolas
7. **Documentar e apresentar** resultados em vídeo

---

## Documentação Adicional

- Veja `DOCUMENTACAO_TECNICA.md` para detalhes técnicos completos
- Consulte `SPRINT3_DOCUMENTACAO_ATIVIDADES.md` para contexto das fases anteriores
- Referências em `docs/` para setup e uso

---

**Objetivo Final:** Consolidar conhecimento técnico, demonstrando como Inteligência Artificial, IoT e análise de dados transformam a agricultura em um setor mais inteligente, eficiente e sustentável.
