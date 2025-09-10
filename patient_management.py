class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease


def search_patients(patients, disease):
    return [p.name for p in patients if p.disease.lower() == disease.lower()]



patients = []
num_patients = int(input("Enter number of patients: "))

for _ in range(num_patients):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter patient disease: ")
    patients.append(Patient(name, age, disease))

# Search
search_disease = input("\nEnter disease to search: ")
found_patients = search_patients(patients, search_disease)

# Output
if found_patients:
    print(f"\nPatients with {search_disease}: {found_patients}")
else:
    print(f"\nNo patients found with {search_disease}.")
