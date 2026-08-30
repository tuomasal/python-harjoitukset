mies_hyva_hg_ylaraja = 195
mies_hyva_hg_alaraja = 134
nainen_hyva_hg_alaraja = 117
nainen_hyva_hg_ylaraja = 175

sukupuoli = input("Oletko mies vai nainen (M/N)?:")
if sukupuoli == "M" or sukupuoli == "N":
    hemoglobiini = int(input("Syötä hemoglobiiniarvosi:"))
    if sukupuoli == "M": 
        if hemoglobiini < mies_hyva_hg_alaraja: print("Hemoglobiinisi on liian alhainen.")
        if hemoglobiini >= mies_hyva_hg_alaraja and hemoglobiini <= mies_hyva_hg_ylaraja: print("Hemoglobiinisi on sopiva.") 
        if hemoglobiini > mies_hyva_hg_ylaraja: print("Hemoglobiinisi on liian korkea.")
    if sukupuoli == "N": 
            if hemoglobiini < nainen_hyva_hg_alaraja: print("Hemoglobiinisi on liian alhainen.")
            if hemoglobiini >= nainen_hyva_hg_alaraja and hemoglobiini <= nainen_hyva_hg_ylaraja: print("Hemoglobiinisi on sopiva.") 
            if hemoglobiini > nainen_hyva_hg_ylaraja: print("Hemoglobiinisi on liian korkea.")
        
else:
    print("Vastaa joko M tai N.")
