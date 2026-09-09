v = (
    ("talvi", 12, 2),
    ("kevät", 3, 5),
    ("kesä", 6, 8),
    ("syksy", 9, 11)
)
luku = int(input("anna kuukausi luku: "))

for nimi, alku, loppu in v:
    if alku <= luku <= loppu:
        print(nimi)