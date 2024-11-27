import patient
import random


patient_num = input()
         
for i in range(8):
    if patient.patient[i].startswith(patient_num):
        print(patient.patient[i])
        for j in range(len(patient.patient_data[i])):
            print(patient.patient_data[i][j][int(random.randint(0, len(patient.patient_data[i][j])-1))])
