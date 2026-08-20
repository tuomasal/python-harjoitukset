alkugrammat = int(input("Kuinka monta grammaa:"))

kilogrammat = int(alkugrammat // 1000)
massa_grammoina = alkugrammat % 1000

print("Määrä kiloina ja grammoina:", kilogrammat, massa_grammoina)