from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env ファイルを読み込む
load_dotenv()

# 環境変数を取得
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Google Generative AIの設定
if GOOGLE_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        gemini_pro = genai.GenerativeModel("gemini-pro")
        print("Google Generative AI configured successfully.")
    except Exception as e:
        gemini_pro = None
        print(f"Failed to configure Google Generative AI: {e}")
else:
    gemini_pro = None
    print("GOOGLE_API_KEY is not set.")

# Flaskアプリケーションの初期化
app = Flask(__name__)

# LINE APIの情報を確認
if not LINE_CHANNEL_ACCESS_TOKEN or not LINE_CHANNEL_SECRET:
    raise ValueError("環境変数 'LINE_CHANNEL_ACCESS_TOKEN' または 'LINE_CHANNEL_SECRET' が設定されていません")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)

    # デバッグログ
    print(f"Request body: {body}")
    print(f"X-Line-Signature: {signature}")

    if not signature:
        abort(400, "X-Line-Signatureヘッダーが見つかりません")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("InvalidSignatureError: 不正な署名です")
        abort(400, "不正な署名です")

    return 'OK'

# LINEメッセージイベントの処理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text.strip()
    response_text = ""

    try:
        if gemini_pro:
            # Google Generative AIで応答生成
            print("Sending prompt to Google Generative AI...")
            prompt = f"ユーザーからの入力: {user_message}"
            response = gemini_pro.generate_content(prompt)
            print(f"Response from Google Generative AI: {response}")
            response_text = response.get("content", "応答が生成されませんでした。")
        else:
            # Generative AIが未設定の場合の応答
            response_text = f"Google Generative AIが利用できないため、応答を生成できません。\n受け取ったメッセージ: {user_message}"
    except Exception as e:
        # エラー時のログと応答
        print(f"Error during content generation: {e}")
        response_text = f"エラーが発生しました: {str(e)}"

    # LINEに応答
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response_text)
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)