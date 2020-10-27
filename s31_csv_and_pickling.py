from csv import reader, writer, DictReader, DictWriter

# -------------
# Read CSV file
# -------------

# Read with reader
with open("fighters.csv") as file:
    csv_reader = reader(file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        print(f"{row[0]} is from {row[1]}")

print()

# Read with DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file, delimiter=',')
    for row in csv_reader:
        print(f"{row['Name']} is from {row['Country']}")

# --------------
# Write CSV file
# --------------

# Write with writer
with open("fighters2.csv", "w", newline='') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Character', 'Move'])
    csv_writer.writerow(['Ryu', 'Hadouken'])
    csv_writer.writerow(['Ken', 'Hadouken'])

# Write with DictWriter
with open("fighters2.csv", "w", newline='') as file:
    headers = ['first', 'last']
    csv_writer = DictWriter(file, fieldnames=headers, delimiter=';')
    csv_writer.writeheader()
    csv_writer.writerow({'first': 'Jimi', 'last': 'Hendrix'})
    csv_writer.writerow({'first': 'John', 'last': 'Doe'})