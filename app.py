from flask import Flask, request, jsonify
import random
import patient

app = Flask(__name__)

@app.route('/')
def kirokukun():
    # URLクエリパラメータから値を取得
    patient_num = request.args.get('patient_num', '')
    response_data = []

    if patient_num == "きずな":
        for k in range(4):
            patient_info = {"name": patient.patient[k], "data": []}
            for j in range(len(patient.patient_data[k])):
                random_data = random.choice(patient.patient_data[k][j])
                patient_info["data"].append(random_data)
            response_data.append(patient_info)

    elif patient_num == "つなぐ":
        for k in range(4, 9):
            patient_info = {"name": patient.patient[k], "data": []}
            for j in range(len(patient.patient_data[k])):
                random_data = random.choice(patient.patient_data[k][j])
                patient_info["data"].append(random_data)
            response_data.append(patient_info)

    else:
        for i in range(8):
            if patient.patient[i].startswith(patient_num):
                patient_info = {"name": patient.patient[i], "data": []}
                for j in range(len(patient.patient_data[i])):
                    random_data = random.choice(patient.patient_data[i][j])
                    patient_info["data"].append(random_data)
                response_data.append(patient_info)

    # JSON形式でデータを返す
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
