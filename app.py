import patient
import random
kizuna = "きずな"

patient_num = input()

if patient_num == "きずな":
    for k in range(4):
        print(patient.patient[k])
        for j in range(len(patient.patient_data[k])):
            print(patient.patient_data[k][j][int(random.randint(0, len(patient.patient_data[k][j])-1))])
elif patient_num == "つなぐ":
     for k in range(4,9):
        print(patient.patient[k])
        for j in range(len(patient.patient_data[k])):
            print(patient.patient_data[k][j][int(random.randint(0, len(patient.patient_data[k][j])-1))])
else:   
    for i in range(8):
        if patient.patient[i].startswith(patient_num):
            print(patient.patient[i])
            for j in range(len(patient.patient_data[i])):
                print(patient.patient_data[i][j][int(random.randint(0, len(patient.patient_data[i][j])-1))])
