v = (
    ("talvi", 12, 2),
    ("kevät", 3, 5),
    ("kesä", 6, 8),
    ("syksy", 9, 11)
)

luku = int(input("Anna kuukausiluku: "))

for nimi, alku, loppu in v:
    if alku <= loppu:
        if alku <= luku <= loppu:
            print(nimi)
    else:
        if luku >= alku or luku <= loppu:
            print(nimi)