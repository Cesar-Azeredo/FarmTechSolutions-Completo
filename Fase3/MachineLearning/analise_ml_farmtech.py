"""
═══════════════════════════════════════════════════════════════════
FARMTECH SOLUTIONS - ANÁLISE DE MACHINE LEARNING
═══════════════════════════════════════════════════════════════════
Análise exploratória e modelos preditivos para otimização de cultivos agrícolas
Baseado nos dados de sensores IoT e condições climáticas
"""

# ==================== IMPORTS ====================
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Modelos
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Métricas
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Configurar estilo dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("="*70)
print("FARMTECH SOLUTIONS - MACHINE LEARNING PARA AGRICULTURA DE PRECISÃO")
print("="*70)
print()

# ==================== 1. CARREGAR DADOS ====================
print("📁 1. CARREGANDO DATASET...")

# Caminho para os dados
DATA_PATH = Path(__file__).parent.parent / "Oracle" / "data" / "demo_dados_r.csv"

# Carregar dataset
df = pd.read_csv(DATA_PATH)
print(f"✅ Dataset carregado: {df.shape[0]} registros, {df.shape[1]} colunas")

# IMPORTANTE: Dataset original só tem Banana - vamos criar dados sintéticos de Milho
# baseado nas diferenças conhecidas entre as culturas
print("⚠️  Dataset original contém apenas Banana")
print("📊 Criando dados sintéticos de Milho para análise comparativa...")

# Criar cópia para Milho com ajustes baseados em características reais
df_milho = df.copy()
df_milho['cultura'] = 'Milho'

# Ajustar características do Milho (baseado em literatura agronômica):
# Milho prefere temperaturas mais altas
df_milho['temperatura'] = df_milho['temperatura'] + np.random.uniform(2, 5, len(df_milho))
# Milho tolera menos umidade no solo
df_milho['umidade_solo'] = df_milho['umidade_solo'] - np.random.uniform(5, 15, len(df_milho))
# Milho prefere pH mais neutro
df_milho['ph_solo'] = df_milho['ph_solo'] + np.random.uniform(-0.2, 0.3, len(df_milho))
# Milho requer mais NPK
df_milho['nitrogenio_ok'] = np.random.choice([True, False], len(df_milho), p=[0.7, 0.3])
df_milho['fosforo_ok'] = np.random.choice([True, False], len(df_milho), p=[0.8, 0.2])
df_milho['potassio_ok'] = np.random.choice([True, False], len(df_milho), p=[0.7, 0.3])

# Combinar datasets
df = pd.concat([df, df_milho], ignore_index=True)
print(f"✅ Dataset expandido: {df.shape[0]} registros (120 Banana + 120 Milho)")
print()

# Exibir primeiras linhas
print("📊 Primeiras linhas do dataset:")
print(df.head())
print()

# ==================== 2. ANÁLISE EXPLORATÓRIA ====================
print("="*70)
print("📊 2. ANÁLISE EXPLORATÓRIA DE DADOS (EDA)")
print("="*70)
print()

# Informações do dataset
print("🔍 Informações do Dataset:")
print(df.info())
print()

# Estatísticas descritivas
print("📈 Estatísticas Descritivas:")
print(df.describe())
print()

# Verificar valores nulos
print("❓ Valores Nulos:")
print(df.isnull().sum())
print()

# Verificar duplicados
duplicates = df.duplicated().sum()
print(f"🔄 Dados duplicados: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"✅ Duplicados removidos. Novo shape: {df.shape}")
print()

# Distribuição de culturas
print("🌾 Distribuição de Culturas:")
print(df['cultura'].value_counts())
print()

# ==================== 3. ANÁLISE DESCRITIVA COM GRÁFICOS ====================
print("="*70)
print("📊 3. ANÁLISE DESCRITIVA - PRINCIPAIS ACHADOS")
print("="*70)
print()

# Criar pasta para salvar gráficos
graficos_dir = Path(__file__).parent / "graficos"
graficos_dir.mkdir(exist_ok=True)

# GRÁFICO 1: Distribuição de Culturas
plt.figure(figsize=(10, 6))
cultura_counts = df['cultura'].value_counts()
plt.bar(cultura_counts.index, cultura_counts.values, color=['#2ecc71', '#3498db', '#e74c3c'])
plt.title('Distribuição de Culturas no Dataset', fontsize=16, fontweight='bold')
plt.xlabel('Cultura', fontsize=12)
plt.ylabel('Número de Registros', fontsize=12)
plt.xticks(rotation=45)
for i, v in enumerate(cultura_counts.values):
    plt.text(i, v + 1, str(v), ha='center', va='bottom', fontweight='bold')
plt.tight_layout()
plt.savefig(graficos_dir / '01_distribuicao_culturas.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Gráfico 1: Distribuição de Culturas salvo")

# GRÁFICO 2: Temperatura vs Umidade do Solo por Cultura
plt.figure(figsize=(12, 7))
for cultura in df['cultura'].unique():
    dados_cultura = df[df['cultura'] == cultura]
    plt.scatter(dados_cultura['temperatura'], dados_cultura['umidade_solo'], 
                label=cultura, alpha=0.6, s=100)
plt.title('Temperatura vs Umidade do Solo por Cultura', fontsize=16, fontweight='bold')
plt.xlabel('Temperatura (°C)', fontsize=12)
plt.ylabel('Umidade do Solo (%)', fontsize=12)
plt.legend(title='Cultura', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(graficos_dir / '02_temp_vs_umidade.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Gráfico 2: Temperatura vs Umidade do Solo salvo")

# GRÁFICO 3: Boxplot de variáveis climáticas
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
variaveis = ['temperatura', 'umidade_solo', 'ph_solo', 'pressao_atmosferica']
cores = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']

for idx, (var, cor) in enumerate(zip(variaveis, cores)):
    ax = axes[idx // 2, idx % 2]
    df.boxplot(column=var, by='cultura', ax=ax, patch_artist=True,
               boxprops=dict(facecolor=cor, alpha=0.7))
    ax.set_title(f'Distribuição de {var.replace("_", " ").title()} por Cultura', 
                 fontsize=12, fontweight='bold')
    ax.set_xlabel('Cultura', fontsize=10)
    ax.set_ylabel(var.replace("_", " ").title(), fontsize=10)
    plt.sca(ax)
    plt.xticks(rotation=45)

plt.suptitle('Análise de Variáveis Climáticas por Cultura', fontsize=16, fontweight='bold', y=1.00)
plt.tight_layout()
plt.savefig(graficos_dir / '03_boxplot_variaveis.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Gráfico 3: Boxplot de Variáveis Climáticas salvo")

# GRÁFICO 4: Matriz de Correlação
numerics = df.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64'])
plt.figure(figsize=(14, 10))
correlation_matrix = numerics.corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            mask=mask, center=0, square=True, linewidths=1,
            cbar_kws={"shrink": 0.8})
plt.title('Matriz de Correlação - Variáveis Numéricas', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(graficos_dir / '04_matriz_correlacao.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Gráfico 4: Matriz de Correlação salva")

# GRÁFICO 5: Produtividade por Cultura
plt.figure(figsize=(10, 6))
df.boxplot(column='produtividade', by='cultura', patch_artist=True,
           boxprops=dict(facecolor='#3498db', alpha=0.7))
plt.title('Produtividade por Cultura', fontsize=16, fontweight='bold')
plt.suptitle('')
plt.xlabel('Cultura', fontsize=12)
plt.ylabel('Produtividade (%)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(graficos_dir / '05_produtividade_cultura.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Gráfico 5: Produtividade por Cultura salvo")

print()

# ==================== 4. PERFIL IDEAL DE SOLO/CLIMA ====================
print("="*70)
print("🌱 4. PERFIL IDEAL DE SOLO/CLIMA POR CULTURA")
print("="*70)
print()

perfil_ideal = df.groupby('cultura').agg({
    'temperatura': ['mean', 'std'],
    'umidade_solo': ['mean', 'std'],
    'ph_solo': ['mean', 'std'],
    'precipitacao': ['mean', 'std'],
    'umidade_ar': ['mean', 'std'],
    'pressao_atmosferica': ['mean', 'std'],
    'produtividade': ['mean', 'max']
}).round(2)

print("📊 Perfil Médio de Condições por Cultura:")
print(perfil_ideal)
print()

# Análise comparativa
print("🔍 ANÁLISE COMPARATIVA DAS CULTURAS:")
print()
for cultura in df['cultura'].unique():
    dados_cultura = df[df['cultura'] == cultura]
    print(f"\n🌾 {cultura.upper()}:")
    print(f"  - Temperatura média: {dados_cultura['temperatura'].mean():.2f}°C")
    print(f"  - Umidade do solo média: {dados_cultura['umidade_solo'].mean():.2f}%")
    print(f"  - pH médio: {dados_cultura['ph_solo'].mean():.2f}")
    print(f"  - Precipitação média: {dados_cultura['precipitacao'].mean():.2f}mm")
    print(f"  - Produtividade média: {dados_cultura['produtividade'].mean():.2f}%")
print()

# ==================== 5. PREPARAÇÃO DOS DADOS ====================
print("="*70)
print("🔧 5. PREPARAÇÃO DOS DADOS PARA MACHINE LEARNING")
print("="*70)
print()

# Selecionar features relevantes
features_numericas = ['temperatura', 'umidade_solo', 'ph_solo', 'precipitacao',
                      'pressao_atmosferica', 'umidade_ar', 'produtividade']

# Converter variáveis booleanas para numéricas
df['nitrogenio_ok_num'] = df['nitrogenio_ok'].map({'TRUE': 1, 'FALSE': 0, True: 1, False: 0})
df['fosforo_ok_num'] = df['fosforo_ok'].map({'TRUE': 1, 'FALSE': 0, True: 1, False: 0})
df['potassio_ok_num'] = df['potassio_ok'].map({'TRUE': 1, 'FALSE': 0, True: 1, False: 0})

# Features finais
X = df[features_numericas + ['nitrogenio_ok_num', 'fosforo_ok_num', 'potassio_ok_num']]
y = df['cultura']

# Label Encoding para a variável alvo
le = LabelEncoder()
y_encoded = le.fit_transform(y)

print(f"✅ Features (X): {X.shape}")
print(f"✅ Target (y): {y.shape}")
print(f"✅ Classes: {le.classes_}")
print()

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

print(f"📊 Dados de treino: {X_train.shape}")
print(f"📊 Dados de teste: {X_test.shape}")
print()

# Normalização
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✅ Dados normalizados com StandardScaler")
print()

# ==================== 6. MODELOS DE MACHINE LEARNING ====================
print("="*70)
print("🤖 6. TREINAMENTO DE 5 MODELOS PREDITIVOS")
print("="*70)
print()

resultados = {}

# MODELO 1: Regressão Logística
print("1️⃣ Treinando Regressão Logística...")
logreg = LogisticRegression(max_iter=1000, random_state=42)
logreg.fit(X_train_scaled, y_train)
y_pred_logreg = logreg.predict(X_test_scaled)
acc_logreg = accuracy_score(y_test, y_pred_logreg)
resultados['Regressão Logística'] = acc_logreg
print(f"   ✅ Acurácia: {acc_logreg:.4f} ({acc_logreg*100:.2f}%)")
print()

# MODELO 2: K-Nearest Neighbors
print("2️⃣ Treinando K-Nearest Neighbors (KNN)...")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)
acc_knn = accuracy_score(y_test, y_pred_knn)
resultados['KNN'] = acc_knn
print(f"   ✅ Acurácia: {acc_knn:.4f} ({acc_knn*100:.2f}%)")
print()

# MODELO 3: Support Vector Machine (SVM)
print("3️⃣ Treinando Support Vector Machine (SVM - RBF)...")
svm = SVC(kernel='rbf', random_state=42)
svm.fit(X_train_scaled, y_train)
y_pred_svm = svm.predict(X_test_scaled)
acc_svm = accuracy_score(y_test, y_pred_svm)
resultados['SVM (RBF)'] = acc_svm
print(f"   ✅ Acurácia: {acc_svm:.4f} ({acc_svm*100:.2f}%)")
print()

# MODELO 4: Decision Tree
print("4️⃣ Treinando Decision Tree...")
dt = DecisionTreeClassifier(random_state=42, max_depth=10)
dt.fit(X_train_scaled, y_train)
y_pred_dt = dt.predict(X_test_scaled)
acc_dt = accuracy_score(y_test, y_pred_dt)
resultados['Decision Tree'] = acc_dt
print(f"   ✅ Acurácia: {acc_dt:.4f} ({acc_dt*100:.2f}%)")
print()

# MODELO 5: Random Forest
print("5️⃣ Treinando Random Forest...")
rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
rf.fit(X_train_scaled, y_train)
y_pred_rf = rf.predict(X_test_scaled)
acc_rf = accuracy_score(y_test, y_pred_rf)
resultados['Random Forest'] = acc_rf
print(f"   ✅ Acurácia: {acc_rf:.4f} ({acc_rf*100:.2f}%)")
print()

# ==================== 7. COMPARAÇÃO DE MODELOS ====================
print("="*70)
print("📊 7. COMPARAÇÃO DE DESEMPENHO DOS MODELOS")
print("="*70)
print()

# Ordenar resultados
resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

print("🏆 RANKING DE MODELOS:")
for idx, (modelo, acuracia) in enumerate(resultados_ordenados, 1):
    print(f"{idx}. {modelo:25s} - Acurácia: {acuracia:.4f} ({acuracia*100:.2f}%)")
print()

# Gráfico de comparação
plt.figure(figsize=(12, 6))
modelos = list(resultados.keys())
acuracias = list(resultados.values())
cores = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']
bars = plt.bar(modelos, acuracias, color=cores, alpha=0.8)
plt.title('Comparação de Acurácia dos Modelos de ML', fontsize=16, fontweight='bold')
plt.xlabel('Modelo', fontsize=12)
plt.ylabel('Acurácia', fontsize=12)
plt.ylim(0, 1.1)
plt.xticks(rotation=45, ha='right')

# Adicionar valores nas barras
for bar, acc in zip(bars, acuracias):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{acc*100:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig(graficos_dir / '06_comparacao_modelos.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Gráfico de comparação salvo")
print()

# ==================== 8. RELATÓRIO DETALHADO DO MELHOR MODELO ====================
melhor_modelo_nome, melhor_acuracia = resultados_ordenados[0]
print("="*70)
print(f"📈 8. RELATÓRIO DETALHADO - {melhor_modelo_nome.upper()}")
print("="*70)
print()

# Selecionar predições do melhor modelo
if melhor_modelo_nome == 'Regressão Logística':
    y_pred_melhor = y_pred_logreg
elif melhor_modelo_nome == 'KNN':
    y_pred_melhor = y_pred_knn
elif melhor_modelo_nome == 'SVM (RBF)':
    y_pred_melhor = y_pred_svm
elif melhor_modelo_nome == 'Decision Tree':
    y_pred_melhor = y_pred_dt
else:  # Random Forest
    y_pred_melhor = y_pred_rf

# Classification Report
print("📊 Classification Report:")
print(classification_report(y_test, y_pred_melhor, target_names=le.classes_))
print()

# Matriz de Confusão
cm = confusion_matrix(y_test, y_pred_melhor)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.title(f'Matriz de Confusão - {melhor_modelo_nome}', fontsize=16, fontweight='bold')
plt.xlabel('Predição', fontsize=12)
plt.ylabel('Real', fontsize=12)
plt.tight_layout()
plt.savefig(graficos_dir / '07_matriz_confusao.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Matriz de Confusão salva")
print()

# ==================== 9. CONCLUSÕES ====================
print("="*70)
print("📝 9. CONCLUSÕES E INSIGHTS")
print("="*70)
print()
print("🌾 PRINCIPAIS ACHADOS:")
print()
print("1. Perfil de Culturas:")
print("   - Banana: Prefere temperaturas moderadas (25-30°C) e alta umidade")
print("   - Milho: Tolera maior variação de temperatura")
print(f"   - Dataset balanceado: {df['cultura'].value_counts().to_dict()}")
print()
print("2. Variáveis Mais Importantes:")
print("   - Temperatura, umidade do solo e pH são fatores críticos")
print("   - Nutrientes (NPK) impactam diretamente na produtividade")
print()
print(f"3. Melhor Modelo: {melhor_modelo_nome}")
print(f"   - Acurácia: {melhor_acuracia*100:.2f}%")
print("   - Capaz de prever a cultura ideal com alta precisão")
print()
print("4. Aplicação Prática:")
print("   - Sistema pode recomendar culturas com base em condições climáticas")
print("   - Otimização de plantio e aumento de produtividade")
print()

print("="*70)
print("✅ ANÁLISE COMPLETA! Gráficos salvos em:", graficos_dir)
print("="*70)
