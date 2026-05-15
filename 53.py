#"The Medical AI Triage Engine"
patient_data = {
    "patient_id": "PT-8832",
    "vitals": {
        "temperature": 98.6,
        "heart_rate": 72
    },
    "history": {
        "blood_type": ("O", "Positive"), 
        "allergies": {"Penicillin", "Latex", "Ibuprofen"} 
    },
    "current_symptoms": ["cough", "headache"] 
}
doctor_input=float(input("Current Temperature:"))
patient_data["vitals"]="doctor_input"
doctor_input1=input("New Symptom:")
patient_data["current_symptoms"].append(doctor_input1)
doctor_input2=(input("Medication to Prescribe: "))
if doctor_input2 in patient_data['history']["allergies"]:
    patient_data["triage_status"]="CRITICAL: Allergic Reaction Risk!"
elif doctor_input>=101.0 or "fever" in patient_data["current_symptoms"]:
    patient_data["triage_status"]="WARNING: High Fever. Isolate Patient."
else:
    patient_data["triage_status"]="STABLE: Proceed with standard care."
    patient_data["approved_medication"]=doctor_input2
print(f"The Patient ID:{patient_data["patient_id"]}")
print(f"The Patient's Blood Type:{patient_data["history"]["blood_type"][-1]}")
print(f"The Final Triage Status:{patient_data["triage_status"]}")
print(f"The complete, updated: {patient_data}")