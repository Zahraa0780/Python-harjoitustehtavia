# Pyydä käyttäjältä suorakulmion kannan ja korkeuden
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# Laske suorakulmion piiri
piiri = 2 * (kanta + korkeus)

# Laske suorakulmion pinta-ala
pinta_ala = kanta * korkeus

# Tulosta piiri ja pinta-ala
print("Suorakulmion piiri on:", piiri)
print("Suorakulmion pinta-ala on:", pinta_ala)
