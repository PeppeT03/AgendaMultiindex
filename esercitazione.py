import numpy as np
import pandas as pd

# 1. Creazione delle liste per il prodotto cartesiano
citta = ["Napoli", "Milano"]
prodotti = ["Pizza", "Pasta", "Caffè"]
mesi = ["Gennaio", "Febbraio"]

# 2. Creazione MultiIndex con 12 combinazioni
index = pd.MultiIndex.from_product(
    [citta, prodotti, mesi], 
    names=["Città", "Prodotto", "Mese"]
)

# 3. Generazione dati casuali (12 valori)
np.random.seed(42)
df = pd.DataFrame(
    {"Vendite": np.random.randint(50, 200, size=len(index))}, 
    index=index
)

print("--- DATAFRAME COMPLETO ---")
print(df)

# 4. Aggregazioni sui livelli dell'indice
somma_citta = df.groupby(level="Città").sum()
media_prodotto = df.groupby(level="Prodotto").mean()

print("\n--- SOMMA PER CITTÀ ---")
print(somma_citta)

print("\n--- MEDIA PER PRODOTTO ---")
print(media_prodotto)

# ==============================================================================
# ESERCIZIO 3: MultiIndex a 3 Livelli, .xs(), Swaplevel e Reset Index
# ==============================================================================

# 1. Creazione MultiIndex a 3 livelli e DataFrame
index_3lvl = pd.MultiIndex.from_tuples(
    [
        ("Roma", "Negozio1", "Q1"),
        ("Roma", "Negozio1", "Q2"),
        ("Milano", "Negozio2", "Q1"),
        ("Milano", "Negozio2", "Q2"),
        ("Napoli", "Negozio3", "Q2")
    ],
    names=["Città", "Negozio", "Trimestre"]
)

df_3lvl = pd.DataFrame({"Vendite": [100, 120, 60, 150, 200]}, index=index_3lvl)

# 2. Estrazione delle vendite di Q2
q2_vendite = df_3lvl.xs("Q2", level="Trimestre")

# 3. Scambio livelli Città e Trimestre
df_swapped = df_3lvl.swaplevel("Città", "Trimestre")

# 4. Riportare il livello 'Negozio' a colonna normale
df_reset = df_3lvl.reset_index(level="Negozio")

# 5. Media delle vendite per Città
media_citta = df_3lvl.groupby(level="Città")["Vendite"].mean()

print("--- ESTRAZIONE Q2 ---")
print(q2_vendite)

print("\n--- LIVELLI SCAMBIATI (Trimestre al 1° posto) ---")
print(df_swapped)

print("\n--- NEGOZIO DIVENTATO COLONNA ---")
print(df_reset)

print("\n--- MEDIA PER CITTÀ ---")
print(media_citta)

# 1. Le 4 liste
regioni = ["Nord", "Centro"]
citta = ["Milano", "Roma"]
prodotti = ["Pizza", "Pasta"]
mesi = ["Gennaio", "Febbraio"]

# 2. Indice a 4 livelli
index = pd.MultiIndex.from_product(
    [regioni, citta, prodotti, mesi],
    names=["Regione", "Citta", "Prodotto", "Mese"]
)

# 3. DataFrame con 16 vendite casuali
np.random.seed(42)
df2 = pd.DataFrame({"Vendite": np.random.randint(50, 300, size=len(index))}, index=index)

print(df2.loc['Nord'])

somma_vendite_per_mese = df2.groupby(level="Mese").sum()
print(somma_vendite_per_mese)

totale_citta_prodotto = df2.groupby(level=["Citta","Prodotto"]).sum()
print(totale_citta_prodotto)
prodotto_top = totale_citta_prodotto.groupby(level="Citta").idxmax()
print(prodotto_top)