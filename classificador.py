import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# ============================================================
# 1. Dados e Treinamento do Robô
# ============================================================
espessura_marajoara = [5.0, 5.2, 4.8, 5.5, 5.1]
ferro_marajoara = [4.5, 4.8, 4.2, 5.0, 4.6]

espessura_santarem = [9.0, 9.5, 10.0, 8.8, 9.2]
ferro_santarem = [1.5, 1.2, 1.8, 1.0, 1.4]

tabela_ceramicas = pd.DataFrame({
    'espessura_mm': espessura_marajoara + espessura_santarem,
    'teor_ferro': ferro_marajoara + ferro_santarem,
    'cultura': ['Marajoara']*5 + ['Santarem']*5
})

X = tabela_ceramicas[['espessura_mm', 'teor_ferro']]
y = tabela_ceramicas['cultura']

robo = DecisionTreeClassifier()
robo.fit(X, y)

# ============================================================
# 2. Interação com o Usuário (Digitação no Terminal)
# ============================================================
print("==================================================")
print("   SISTEMA DE CLASSIFICAÇÃO CERÂMICA ARQUEOLÓGICA   ")
print("==================================================")
print("Digite os dados do caco encontrado na escavação:\n")

# O float() garante que o número digitado possa ter casas decimais (ex: 5.4)
espessura_usuario = float(input("Digite a espessura do caco em mm (ex: 5.2): "))
ferro_usuario = float(input("Digite o teor de ferro % (ex: 4.5): "))

# Montamos a lista com os dados que o usuário acabou de digitar
caco_usuario = [[espessura_usuario, ferro_usuario]]

# O robô analisa e dá o palpite
previsao = robo.predict(caco_usuario)

print("\n--------------------------------------------------")
print(f"RESULTADO: O caco analisado pertence à cultura {previsao[0]}!")
print("--------------------------------------------------")