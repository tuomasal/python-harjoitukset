
luodit = float(input("Anna luotien lukumäärä:"))
naulat = float(input("Anna naulojen lukumäärä:"))
leiviskat = float(input("Anna leiviskoiden lukumäärä:"))

luoti_grammoina = 13.3
naula_grammoina = 13.3 * 32
leiviskat_grammoina = naula_grammoina * 20

leiviskojen_paino = leiviskat_grammoina * leiviskat
naulojen_paino = naula_grammoina * naulat
luotien_paino = luoti_grammoina * luodit
massa_grammoina = leiviskojen_paino + naulojen_paino + luotien_paino

kilogrammat = int(massa_grammoina // 1000)
grammat = massa_grammoina % 1000

print("Yhteenlaskettu massa on:", kilogrammat, "kiloa ja", grammat, "grammaa")