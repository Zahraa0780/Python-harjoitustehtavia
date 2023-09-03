# Pyydä käyttäjältä massa leivisköinä, nauloina ja luoteina
leiviskat = float(input("Anna massa leivisköinä: "))
naulat = float(input("Anna massa nauloina: "))
luodit = float(input("Anna massa luoteina: "))

# Muunna mitat kilogrammoiksi ja grammaiksi
kilogrammat = leiviskat * 20 * 32 * 13.3 / 1000
grammat = (leiviskat * 20 * 32 * 13.3 % 1000) + (naulat * 32 * 13.3) + (luodit * 13.3)

# Tulosta tulos
print("Massa nykymittojen mukaan:")
print(int(kilogrammat), "kilogrammaa ja", grammat, "grammaa.")
