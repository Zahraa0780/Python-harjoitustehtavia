import random

# Kolmenumeroinen koodi (0..9)
kolmenumeroinen_koodi = ""
for i in range(3):
    kolmenumeroinen_koodi += str(random.randint(0, 9))

# Nelinumeroinen koodi (1..6)
nelinumeroinen_koodi = ""
for i in range(4):
    nelinumeroinen_koodi += str(random.randint(1, 6))

# Tulosta koodit
print("Kolmenumeroinen koodi:", kolmenumeroinen_koodi)
print("Nelinumeroinen koodi:", nelinumeroinen_koodi)
