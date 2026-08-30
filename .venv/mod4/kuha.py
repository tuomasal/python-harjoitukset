kuhan_pituus = float(input("Anna kuhan pituus sentteinä:"))

if kuhan_pituus < 37:
    puuttuva = 37 - kuhan_pituus
    print("Päästä kuha menemään.")
    print(f"Kuha on {puuttuva} cm alamittainen.")

else:
     print("Kuha on tarpeeksi pitkä.")

                     