from flask import Flask, request, abort, jsonify
import random
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import patient

app = Flask(__name__)

# 環境変数からLINE APIの情報を取得
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

if not LINE_CHANNEL_ACCESS_TOKEN or not LINE_CHANNEL_SECRET:
    raise ValueError("環境変数 'LINE_CHANNEL_ACCESS_TOKEN' または 'LINE_CHANNEL_SECRET' が設定されていません")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # X-Line-Signatureヘッダーを取得
    signature = request.headers.get('X-Line-Signature')
    if not signature:
        abort(400, "X-Line-Signatureヘッダーが見つかりません")

    # リクエストボディを取得
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400, "不正な署名です")

    return 'OK'

# LINEメッセージイベントの処理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    patient_num = event.message.text.strip()  # ユーザーの入力を取得
    response_text = ""

    if patient_num == "きずな":
        response_text = generate_patient_response(range(4))
    elif patient_num == "つなぐ":
        response_text = generate_patient_response(range(4, 9))
    else:
        matched = False
        for i in range(8):
            if patient.patient[i].startswith(patient_num):
                response_text = generate_patient_response([i])
                matched = True
                break
        if not matched:
            response_text = "該当するデータが見つかりません。"

    # ユーザーに返信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response_text)
    )

def generate_patient_response(indices):
    """
    患者情報を生成する関数
    """
    response_data = []
    for k in indices:
        patient_info = {"name": patient.patient[k], "data": []}
        for j in range(len(patient.patient_data[k])):
            random_data = random.choice(patient.patient_data[k][j])
            patient_info["data"].append(random_data)
        response_data.append(patient_info)

    # テキスト形式に変換
    response_text = "\n".join([
        f"{info['name']}: {', '.join(info['data'])}" for info in response_data
    ])
    return response_text

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
