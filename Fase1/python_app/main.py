#grupo 59 FIAP
#rm566826 - Phellype Matheus Giacoia Flaibam Massarente
#rm567659 - Maria Luísa Rodrigues Nascimento
#rm567005 - Carlos Alberto Florindo Costato
#rm568140 - Cesar Martinho de Azeredo
#rm568457 - Guilherme Paes Barreto Didier Garcia

import csv
# to work with csv files
import os
# read/write files
import re
# search --> p/ tratar caracteres especiais na entrada de números

def parse_float(text):
    """
    Função global para converter texto para float.
    Remove vírgulas e substitui por pontos.
    """
    match = re.search(r"[\d,.]+", text)
    if match:
        return float(match.group(0).replace(",", "."))
    else:
        raise ValueError("Valor numérico inválido!")

def get_numeric_input(prompt, input_type="float"):
    """
    Função auxiliar para obter entrada numérica com validação de erro.
    Permite 'X' para sair.
    Retorna None se o usuário digitar 'X'.
    """
    while True:
        entrada = input(prompt).strip()
        if entrada.upper() == 'X':
            return None
        try:
            if input_type == "float":
                return parse_float(entrada)
            elif input_type == "int":
                return int(entrada)
        except ValueError:
            print("Valor inválido. Digite um número válido ou X para sair.")
            continue

def carregar_csv_banana():
    if os.path.exists('banana.csv'):
        with open('banana.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [
                {k: float(v) if k in ['comprimento','largura','qtd_insumo','area'] and v != '' else (None if v == '' else v) for k, v in row.items()}
                for row in reader
            ]
    return []

def carregar_csv_milho():
    if os.path.exists('milho.csv'):
        with open('milho.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [
                {k: float(v) if k in ['raio','comprimento','largura','qtd_insumo','area'] and v != '' else (None if v == '' else v) for k, v in row.items()}
                for row in reader
            ]
    return []

dados_banana = carregar_csv_banana()
dados_milho = carregar_csv_milho()
print(f"Carregados {len(dados_banana)} registros de banana e {len(dados_milho)} de milho")


# Função para gerar exemplos e salvar nos CSV
import random
def gerar_exemplos():
    figuras = ['1', '2', '3']
    insumos = ["Fosfato", "Nitrogênio", "Potássio", "sulfato de amônio", "Herbicida", "Inseticida"]
    unidades = ["mL", "L", "kg", "g"]
    banana = []
    milho = []
    for i in range(20):
        figura = random.choice(figuras)
        insumo = random.choice(insumos)
        unidade = random.choice(unidades)
        if figura == '1':
            comprimento = random.randint(5, 50)
            largura = random.randint(5, 50)
            area = comprimento * largura
            raio = None
        elif figura == '2':
            comprimento = random.randint(5, 50)
            largura = random.randint(5, 50)
            area = (comprimento * largura) / 2
            raio = None
        else:
            raio = random.randint(3, 25)
            area = 3.1416 * raio ** 2
            comprimento = raio * 2
            largura = raio * 2
        qtd_insumo = round(random.uniform(10, 500), 2)
        banana.append({'comprimento': comprimento, 'largura': largura, 'insumo': insumo, 'qtd_insumo': qtd_insumo, 'unidade': unidade, 'area': area, 'figura': figura})
    for i in range(20):
        figura = random.choice(figuras)
        insumo = random.choice(insumos)
        unidade = random.choice(unidades)
        if figura == '1':
            comprimento = random.randint(5, 50)
            largura = random.randint(5, 50)
            area = comprimento * largura
            raio = None
        elif figura == '2':
            comprimento = random.randint(5, 50)
            largura = random.randint(5, 50)
            area = (comprimento * largura) / 2
            raio = None
        else:
            raio = random.randint(3, 25)
            area = 3.1416 * raio ** 2
            comprimento = raio * 2
            largura = raio * 2
        qtd_insumo = round(random.uniform(10, 500), 2)
        milho.append({'raio': raio, 'comprimento': comprimento, 'largura': largura, 'insumo': insumo, 'qtd_insumo': qtd_insumo, 'unidade': unidade, 'area': area, 'figura': figura})
    # Salvar nos CSV
    with open('banana.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=banana[0].keys())
        writer.writeheader()
        writer.writerows(banana)
    with open('milho.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=milho[0].keys())
        writer.writeheader()
        writer.writerows(milho)
    print('20 exemplos de cada cultura gerados e salvos nos CSV.')
# Aplicação FarmTech Solutions
# Suporte a duas culturas: Soja (retângulo) e Milho (círculo)

culturas = ['Banana', 'Milho']

def menu():
    os.system('cls')
    print("\n--- Menu FarmTech Solutions ---")
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Sair")
    return input("Escolha uma opção: ")
# Função para exportar dados para CSV
import csv

def salvar_dados():
    # Salva dados_banana
    if dados_banana:
        with open('banana.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['comprimento', 'largura', 'insumo', 'qtd_insumo', 'unidade', 'area', 'figura'])
            writer.writeheader()
            writer.writerows(dados_banana)
    # Salva dados_milho
    if dados_milho:
        with open('milho.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['raio', 'comprimento', 'largura', 'insumo', 'qtd_insumo', 'unidade', 'area', 'figura'])
            writer.writeheader()
            writer.writerows(dados_milho)

def exportar_csv():
    # Exporta dados_banana
    if dados_banana:
        with open('banana.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['comprimento', 'largura', 'insumo', 'qtd_insumo', 'unidade', 'area', 'figura'])
            writer.writeheader()
            writer.writerows(dados_banana)
        print('Dados de Banana exportados para banana.csv')
    else:
        print('Nenhum dado de Banana para exportar.')
    # Exporta dados_milho
    if dados_milho:
        with open('milho.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['raio', 'comprimento', 'largura', 'insumo', 'qtd_insumo', 'unidade', 'area', 'figura'])
            writer.writeheader()
            writer.writerows(dados_milho)
        print('Dados de Milho exportados para milho.csv')
    else:
        print('Nenhum dado de Milho para exportar.')


def entrada_dados():
    os.system('cls')
    print("\nEscolha a cultura:")
    print("1. Banana")
    print("2. Milho")
    print("X. Sair")
    op = input("Opção: ")
    if op.upper() == 'X':
        return
    
    os.system('cls')
    print("\nEscolha a figura geométrica para o cálculo da área:")
    print("1. Retângulo")
    print("2. Triângulo")
    print("3. Círculo")
    print("X. Sair")
    figura = input("Opção: ")
    if figura.upper() == 'X':
        return
    if figura == '1':
        comprimento = get_numeric_input("Comprimento do terreno (m) ou X para sair: ")
        if comprimento is None:
            return
        largura = get_numeric_input("Largura do terreno (m) ou X para sair: ")
        if largura is None:
            return
        area = comprimento * largura
    elif figura == '2':
        base = get_numeric_input("Base do terreno (m) ou X para sair: ")
        if base is None:
            return
        altura = get_numeric_input("Altura do terreno (m) ou X para sair: ")
        if altura is None:
            return
        area = (base * altura) / 2
        comprimento = base
        largura = altura
    elif figura == '3':
        raio = get_numeric_input("Raio do terreno (m) ou X para sair: ")
        if raio is None:
            return
        area = 3.1416 * raio ** 2
        comprimento = raio * 2
        largura = raio * 2
    else:
        print("Opção de figura inválida.")
        input("Pressione Enter para continuar...")
        return
    os.system('cls')
    # Menu de insumos (após metragem)
    os.system('cls')
    insumos_exemplo = [
        "Fosfato",
        "Nitrogênio",
        "Potássio",
        "sulfato de amônio",
        "Herbicida",
        "Inseticida",
        "Outro (digite manualmente)"
    ]
    print("\nEscolha o insumo:")
    for idx, nome in enumerate(insumos_exemplo, 1):
        print(f"{idx}. {nome}")
    print("X. Sair")
    escolha_insumo = input("Opção: ")
    if escolha_insumo.upper() == 'X':
        return
    if escolha_insumo.isdigit() and 1 <= int(escolha_insumo) <= len(insumos_exemplo):
        if int(escolha_insumo) == len(insumos_exemplo):
            os.system('cls')
            insumo = input("Digite o nome do insumo: ")
        else:
            insumo = insumos_exemplo[int(escolha_insumo)-1]
    else:
        print("Opção de insumo inválida.")
        input("Pressione Enter para continuar...")
        return
    os.system('cls')
    print("\nEscolha a unidade de medida da quantidade de insumo:")
    unidades = ["mL", "L", "kg", "g", "Outro (digite manualmente)"]
    for idx, u in enumerate(unidades, 1):
        print(f"{idx}. {u}")
    print("X. Sair")
    escolha_unidade = input("Opção: ")
    if escolha_unidade.upper() == 'X':
        return
    if escolha_unidade.isdigit() and 1 <= int(escolha_unidade) <= len(unidades):
        if int(escolha_unidade) == len(unidades):
            os.system('cls')
            unidade = input("Digite a unidade: ")
        else:
            unidade = unidades[int(escolha_unidade)-1]
    else:
        print("Opção de unidade inválida.")
        input("Pressione Enter para continuar...")
        return
    qtd = get_numeric_input(f"Quantidade de insumo por metro quadrado ({unidade}) ou X para sair: ")
    if qtd is None:
        return
    dados_banana.append({'comprimento': comprimento, 'largura': largura, 'insumo': insumo, 'qtd_insumo': qtd, 'unidade': unidade, 'area': area, 'figura': figura})
    # Bloco para milho
    if op == '2':
        figura = input("Opção: ")
        if figura.upper() == 'X':
            return
        if figura == '1':
            comprimento = get_numeric_input("Comprimento do terreno (m) ou X para sair: ")
            if comprimento is None:
                return
            largura = get_numeric_input("Largura do terreno (m) ou X para sair: ")
            if largura is None:
                return
            area = comprimento * largura
            raio = None
        elif figura == '2':
            base = get_numeric_input("Base do terreno (m) ou X para sair: ")
            if base is None:
                return
            altura = get_numeric_input("Altura do terreno (m) ou X para sair: ")
            if altura is None:
                return
            area = (base * altura) / 2
            comprimento = base
            largura = altura
            raio = None
        elif figura == '3':
            raio = get_numeric_input("Raio do terreno (m) ou X para sair: ")
            if raio is None:
                return
            area = 3.1416 * raio ** 2
            comprimento = raio * 2
            largura = raio * 2
        else:
            print("Opção de figura inválida.")
            input("Pressione Enter para continuar...")
            return
        # Menu de insumos (após metragem)
        os.system('cls')
        insumos_exemplo = [
            "Fosfato",
            "Nitrogênio",
            "Potássio",
            "sulfato de amônio",
            "Herbicida",
            "Inseticida",
            "Outro (digite manualmente)"
        ]
        print("\nEscolha o insumo:")
        for idx, nome in enumerate(insumos_exemplo, 1):
            print(f"{idx}. {nome}")
        print("X. Sair")
        escolha_insumo = input("Opção: ")
        if escolha_insumo.upper() == 'X':
            return
        if escolha_insumo.isdigit() and 1 <= int(escolha_insumo) <= len(insumos_exemplo):
            if int(escolha_insumo) == len(insumos_exemplo):
                os.system('cls')
                insumo = input("Digite o nome do insumo: ")
            else:
                insumo = insumos_exemplo[int(escolha_insumo)-1]
        else:
            print("Opção de insumo inválida.")
            input("Pressione Enter para continuar...")
            return
        os.system('cls')
        print("\nEscolha a unidade de medida da quantidade de insumo:")
        unidades = ["mL", "L", "kg", "g", "Outro (digite manualmente)"]
        for idx, u in enumerate(unidades, 1):
            print(f"{idx}. {u}")
        print("X. Sair")
        escolha_unidade = input("Opção: ")
        if escolha_unidade.upper() == 'X':
            return
        if escolha_unidade.isdigit() and 1 <= int(escolha_unidade) <= len(unidades):
            if int(escolha_unidade) == len(unidades):
                os.system('cls')
                unidade = input("Digite a unidade: ")
            else:
                unidade = unidades[int(escolha_unidade)-1]
        else:
            print("Opção de unidade inválida.")
            input("Pressione Enter para continuar...")
            return
        qtd = get_numeric_input(f"Quantidade de insumo por metro quadrado ({unidade}) ou X para sair: ")
        if qtd is None:
            return
        dados_milho.append({'raio': raio, 'comprimento': comprimento, 'largura': largura, 'insumo': insumo, 'qtd_insumo': qtd, 'unidade': unidade, 'area': area, 'figura': figura})
    # Salvar dados no CSV após entrada
    salvar_dados()

def saida_dados():
    print("\n--- Dados Banana ---")
    print(f"Total de registros banana: {len(dados_banana)}")
    for i, d in enumerate(dados_banana):
        try:
            total_insumo = d['area'] * d['qtd_insumo']
            figuras = {'1': 'Retângulo', '2': 'Triângulo', '3': 'Círculo'}
            print(f"[{i}] Geométria: {figuras.get(d['figura'], 'N/A')} | Área: {d['area']:.2f} m² | Insumo: {d['insumo']} | Unidade: {d['unidade']} | Total: {total_insumo:.2f} {d['unidade']}")
        except Exception as e:
            print(f"Erro no registro {i}: {e}")
            print(f"Dados: {d}")
    print("\n--- Dados Milho ---")
    print(f"Total de registros milho: {len(dados_milho)}")
    for i, d in enumerate(dados_milho):
        try:
            total_insumo = d['area'] * d['qtd_insumo']
            figuras = {'1': 'Retângulo', '2': 'Triângulo', '3': 'Círculo'}
            print(f"[{i}] Geométria: {figuras.get(d['figura'], 'N/A')} | Área: {d['area']:.2f} m² | Insumo: {d['insumo']} | Unidade: {d['unidade']} | Total: {total_insumo:.2f} {d['unidade']}")
        except Exception as e:
            print(f"Erro no registro {i}: {e}")
            print(f"Dados: {d}")
    
    input("\nPressione Enter para voltar ao menu...")

def atualizar_dados():
    os.system('cls')
    print("\nAtualizar dados de qual cultura?")
    print("1. Banana")
    print("2. Milho")
    print("X. Sair")
    op = input("Opção: ")
    if op.upper() == 'X':
        return
    
    if op == '1' and dados_banana:
        print("\n--- Dados Banana ---")
        figuras = {'1': 'Retângulo', '2': 'Triângulo', '3': 'Círculo'}
        for i, d in enumerate(dados_banana, 1):
            try:
                total_insumo = d['area'] * d['qtd_insumo']
                print(f"[{i}] Geométria: {figuras.get(str(d['figura']), 'N/A')} | Área: {d['area']:.2f} m² | Insumo: {d['insumo']} | Unidade: {d['unidade']} | Total: {total_insumo:.2f} {d['unidade']}")
            except Exception as e:
                print(f"[{i}] Erro: {e} | Dados: {d}")
        idx_input = input(f"Índice (1 a {len(dados_banana)}) ou X para sair: ")
        if idx_input.upper() == 'X':
            return
        try:
            idx = int(idx_input) - 1
        except ValueError:
            print("Valor inválido. Digite um número ou X para sair.")
            return
        if 0 <= idx < len(dados_banana):
            d = dados_banana[idx]
            os.system('cls')
            print(f"\nAtualizando Banana (registro {idx+1}):")
            print("Escolha a figura geométrica para o cálculo da área:")
            print("1. Retângulo")
            print("2. Triângulo")
            print("3. Círculo")
            print("X. Sair")
            figura = input("Opção: ")
            if figura.upper() == 'X':
                return
            if figura == '1':
                comprimento = get_numeric_input("Novo comprimento do terreno (m) ou X para sair: ", "float")
                if comprimento is None:
                    return
                largura = get_numeric_input("Nova largura do terreno (m) ou X para sair: ", "float")
                if largura is None:
                    return
                area = comprimento * largura
            elif figura == '2':
                base = get_numeric_input("Nova base do terreno (m) ou X para sair: ", "float")
                if base is None:
                    return
                altura = get_numeric_input("Nova altura do terreno (m) ou X para sair: ", "float")
                if altura is None:
                    return
                area = (base * altura) / 2
                comprimento = base
                largura = altura
            elif figura == '3':
                raio = get_numeric_input("Novo raio do terreno (m) ou X para sair: ", "float")
                if raio is None:
                    return
                area = 3.1416 * raio ** 2
                comprimento = raio * 2
                largura = raio * 2
            else:
                print("Opção de figura inválida.")
                return
            insumos_exemplo = [
                "Fosfato",
                "Nitrogênio",
                "Potássio",
                "sulfato de amônio",
                "Herbicida",
                "Inseticida",
                "Outro (digite manualmente)"
            ]
            print("\nEscolha o insumo:")
            for idx2, nome in enumerate(insumos_exemplo, 1):
                print(f"{idx2}. {nome}")
            print("X. Sair")
            escolha_insumo = input("Opção: ")
            if escolha_insumo.upper() == 'X':
                return
            if escolha_insumo.isdigit() and 1 <= int(escolha_insumo) <= len(insumos_exemplo):
                if int(escolha_insumo) == len(insumos_exemplo):
                    insumo = input("Digite o nome do insumo: ")
                else:
                    insumo = insumos_exemplo[int(escolha_insumo)-1]
            else:
                print("Opção de insumo inválida.")
                input("Pressione Enter para continuar...")
                return
            print("\nEscolha a unidade de medida da quantidade de insumo:")
            unidades = ["mL", "L", "kg", "g", "Outro (digite manualmente)", "Sair"]
            for idx_unidade, u in enumerate(unidades, 1):
                print(f"{idx_unidade}. {u}")
            escolha_unidade = input("Opção: ")
            if escolha_unidade.isdigit() and 1 <= int(escolha_unidade) <= len(unidades):
                if int(escolha_unidade) == len(unidades):
                    return
                elif int(escolha_unidade) == len(unidades) - 1:
                    unidade = input("Digite a unidade: ")
                else:
                    unidade = unidades[int(escolha_unidade)-1]
            else:
                print("Opção de unidade inválida.")
                input("Pressione Enter para continuar...")
                return
            qtd = get_numeric_input(f"Nova quantidade de insumo por metro quadrado ({unidade}) ou X para sair: ")
            if qtd is None:
                return
            dados_banana[idx] = {'comprimento': comprimento, 'largura': largura, 'insumo': insumo, 'qtd_insumo': qtd, 'unidade': unidade, 'area': area, 'figura': figura}
        else:
            print("Índice inválido.")
            input("Pressione Enter para continuar...")
            
    elif op == '2' and dados_milho:
        print("\n--- Dados Milho ---")
        figuras = {'1': 'Retângulo', '2': 'Triângulo', '3': 'Círculo'}
        for i, d in enumerate(dados_milho, 1):
            try:
                total_insumo = d['area'] * d['qtd_insumo']
                print(f"[{i}] Geométria: {figuras.get(str(d['figura']), 'N/A')} | Área: {d['area']:.2f} m² | Insumo: {d['insumo']} | Unidade: {d['unidade']} | Total: {total_insumo:.2f} {d['unidade']}")
            except Exception as e:
                print(f"[{i}] Erro: {e} | Dados: {d}")
        idx_input = input(f"Índice (1 a {len(dados_milho)}) ou X para sair: ")
        if idx_input.upper() == 'X':
            return
        try:
            idx = int(idx_input) - 1
        except ValueError:
            print("Valor inválido. Digite um número ou X para sair.")
            return
        if 0 <= idx < len(dados_milho):
            d = dados_milho[idx]
            os.system('cls')
            print(f"\nAtualizando Milho (registro {idx+1}):")
            print("Escolha a figura geométrica para o cálculo da área:")
            print("1. Retângulo")
            print("2. Triângulo")
            print("3. Círculo")
            print("X. Sair")
            figura = input("Opção: ")
            if figura.upper() == 'X':
                return
            if figura == '1':
                comprimento = get_numeric_input("Novo comprimento do terreno (m) ou X para sair: ", "float")
                if comprimento is None:
                    return
                largura = get_numeric_input("Nova largura do terreno (m) ou X para sair: ", "float")
                if largura is None:
                    return
                area = comprimento * largura
                raio = None
            elif figura == '2':
                base = get_numeric_input("Nova base do terreno (m) ou X para sair: ", "float")
                if base is None:
                    return
                altura = get_numeric_input("Nova altura do terreno (m) ou X para sair: ", "float")
                if altura is None:
                    return
                area = (base * altura) / 2
                comprimento = base
                largura = altura
                raio = None
            elif figura == '3':
                raio = get_numeric_input("Novo raio do terreno (m) ou X para sair: ", "float")
                if raio is None:
                    return
                area = 3.1416 * raio ** 2
                comprimento = raio * 2
                largura = raio * 2
            else:
                print("Opção de figura inválida.")
                return
            insumos_exemplo = [
                "Fosfato",
                "Nitrogênio",
                "Potássio",
                "sulfato de amônio",
                "Herbicida",
                "Inseticida",
                "Outro (digite manualmente)"
            ]
            print("\nEscolha o insumo:")
            for idx2, nome in enumerate(insumos_exemplo, 1):
                print(f"{idx2}. {nome}")
            print("X. Sair")
            escolha_insumo = input("Opção: ")
            if escolha_insumo.upper() == 'X':
                return
            if escolha_insumo.isdigit() and 1 <= int(escolha_insumo) <= len(insumos_exemplo):
                if int(escolha_insumo) == len(insumos_exemplo):
                    insumo = input("Digite o nome do insumo: ")
                else:
                    insumo = insumos_exemplo[int(escolha_insumo)-1]
            else:
                print("Opção de insumo inválida.")
                return
            print("\nEscolha a unidade de medida da quantidade de insumo:")
            unidades = ["mL", "L", "kg", "g", "Outro (digite manualmente)", "Sair"]
            for idx_unidade, u in enumerate(unidades, 1):
                print(f"{idx_unidade}. {u}")
            escolha_unidade = input("Opção: ")
            if escolha_unidade.isdigit() and 1 <= int(escolha_unidade) <= len(unidades):
                if int(escolha_unidade) == len(unidades):
                    return
                elif int(escolha_unidade) == len(unidades) - 1:
                    unidade = input("Digite a unidade: ")
                else:
                    unidade = unidades[int(escolha_unidade)-1]
            else:
                print("Opção de unidade inválida.")
                return
            qtd = get_numeric_input(f"Nova quantidade de insumo por metro quadrado ({unidade}) ou X para sair: ")
            if qtd is None:
                return
            dados_milho[idx] = {'raio': raio, 'comprimento': comprimento, 'largura': largura, 'insumo': insumo, 'qtd_insumo': qtd, 'unidade': unidade, 'area': area, 'figura': figura}
        else:
            print("Índice inválido.")
    else:
        print("Opção inválida ou sem dados.")
    
    # Salvar dados no CSV após atualização
    salvar_dados()

def deletar_dados():
    os.system('cls')
    print("\nDeletar dados de qual cultura?")
    print("1. Banana")
    print("2. Milho")
    print("X. Sair")
    op = input("Opção: ")
    if op.upper() == 'X':
        os.system('cls')
        return
    if op == '1' and dados_banana:
        idx_input = input(f"Índice (0 a {len(dados_banana)-1}) ou X para sair: ")
        if idx_input.upper() == 'X':
            os.system('cls')
            return
        try:
            idx = int(idx_input)
        except ValueError:
            print("Valor inválido. Digite um número ou X para sair.")
            return
        if 0 <= idx < len(dados_banana):
            dados_banana.pop(idx)
        else:
            print("Índice inválido.")
    elif op == '2' and dados_milho:
        idx_input = input(f"Índice (0 a {len(dados_milho)-1}) ou X para sair: ")
        if idx_input.upper() == 'X':
            os.system('cls')
            return
        try:
            idx = int(idx_input)
        except ValueError:
            print("Valor inválido. Digite um número ou X para sair.")
            return
        if 0 <= idx < len(dados_milho):
            dados_milho.pop(idx)
        else:
            print("Índice inválido.")
    else:
        print("Opção inválida ou sem dados.")
    
    # Salvar dados no CSV após deleção
    salvar_dados()

# Limpar tela ao iniciar o programa
os.system('cls')

# Loop principal
while True:
    op = menu()
    if op == '1':
        os.system('cls')
        entrada_dados()
    elif op == '2':
        saida_dados()
    elif op == '3':
        os.system('cls')
        atualizar_dados()
    elif op == '4':
        os.system('cls')
        deletar_dados()
    elif op == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
