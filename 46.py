#"The Hassan Health-Care Center"
clinic_info = ("Hassan Central", "Karnataka", "Room-A")


name = input("Name: ").title()
age = int(input("Age: "))
body_temperature = float(input("Body Temperature: ")) 
weight = float(input("Weight: ")) 

symptoms = []
symptoms.append(input("Enter symptom 1: "))
symptoms.append(input("Enter symptom 2: "))

allergies = {"Dust", "Peanuts"}
allergies.add(input("Enter any additional allergy: ")) 


if body_temperature >= 38.0:
    status = "Alert: Patient has a Fever."
else:
    status = "Temperature: Normal."

if age < 18:
    patient_type = "Minor"
elif age >= 18 and age <= 60:
    patient_type = "Adult"
else:
    patient_type = "Senior Citizen"

bmi = weight / (1.75 ** 2)
print("\n" + "="*40)
print("___The Hassan Health-Care Center___")
print("="*40)
print(f"Clinic and Room: {clinic_info[0]}, {clinic_info[2]}")
print(f"Patient: {name} ({patient_type})")
print(f"Calculated BMI: {bmi}")
print(f"Recorded Symptoms: {symptoms}")
print(f"Updated Allergies: {allergies}")
print(f"Fever Alert Status: {status}")
print("="*40)