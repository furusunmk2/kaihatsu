from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
from dotenv import load_dotenv

try:
    import google.generativeai as genai
    genai_available = True
except ImportError as e:
    print(f"Google Generative AI module not found: {e}")
    genai_available = False

# Load .env file
load_dotenv()

# Get environment variables
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if genai_available and GOOGLE_API_KEY:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        gemini_pro = genai.GenerativeModel("gemini-pro")
        print("Google Generative AI configured successfully.")
    except Exception as e:
        gemini_pro = None
        print(f"Failed to configure Google Generative AI: {e}")
else:
    gemini_pro = None

app = Flask(__name__)

if not LINE_CHANNEL_ACCESS_TOKEN or not LINE_CHANNEL_SECRET:
    raise ValueError("Missing LINE_CHANNEL_ACCESS_TOKEN or LINE_CHANNEL_SECRET")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)

    print(f"Request body: {body}")
    print(f"X-Line-Signature: {signature}")

    if not signature:
        abort(400, "Missing X-Line-Signature header")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("InvalidSignatureError: Invalid signature")
        abort(400, "Invalid signature")

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text.strip()
    response_text = ""
    prompt = f"""以下の文章を敬語表現に変換してください。
元の文章:
「{user_message}」
敬語表現:
"""
    print(f"Generated Prompt: {prompt}")  # プロンプトをデバッグ出力

    try:
        # Google Generative AIで応答を生成
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"{prompt}")
        print(f"GenerateContentResponse: {response}")  # レスポンス全体をデバッグ出力

        # レスポンスが存在し、候補が含まれている場合に処理を続行
        # 応答候補が存在する場合
        if response and response.candidates:
            # 最初の候補のテキスト部分を取得
            first_candidate = response.candidates[0]
            response_text = first_candidate.content.parts[0].text  # ここで属性を利用
            print(f"First Candidate: {first_candidate}")  # 候補を詳細にデバッグ
            # parts配列から最初のテキストを取得
            response_text = first_candidate.content.parts[0].text
            print(f"Generated Text: {response_text}")  # 応答テキストをデバッグ出力
        else:
            print("No candidates found in the response.")  # 応答が空の場合
            response_text = "AIからの応答が生成されませんでした。"
    except AttributeError as e:
        print(f"AttributeError in response handling: {e}")
        response_text = "AI応答の処理中にエラーが発生しました。"
    except Exception as e:
        print(f"Unexpected error during AI content generation: {e}")
        response_text = f"AI応答の生成中にエラーが発生しました: {str(e)}"

    # 最終的な応答をデバッグ出力
    print(f"Final Response Text: {response_text}")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response_text)
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)