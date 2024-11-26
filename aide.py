import patient
import random


patient_num = input()
         
for i in range(8):
    if patient.patient[i].startswith(patient_num):
        print(patient.patient[i])

        print(patient.patient_data[i][0][int(random.randint(0, len(patient.patient_data[i])))])
        print(patient.patient_data[i][1][int(random.randint(0, len(patient.patient_data[i])))])
        print(patient.patient_data[i][2][int(random.randint(0, len(patient.patient_data[i])))])
        print(patient.patient_data[i][3][int(random.randint(0, len(patient.patient_data[i])))])