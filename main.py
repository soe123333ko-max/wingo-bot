import telebot
import time
import random
from datetime import datetime

# ၁။ မင်းရဲ့ တကယ့် Bot Token ကို ထည့်ပါ
TOKEN = '8729983442:AAGOKgerRys_MxWK-aVFLMUVqTcHD3dbpRw'

# ၂။ ⚠️ စာပို့မယ့် Telegram Group ရဲ့ Username ကို အမှန်ပြင်ထည့်ပါ (ဥပမာ - '@my_group')
CHAT_ID = '@TRX1Min1Bot'

bot = telebot.TeleBot(TOKEN)
print("Auto Bot (အမှား/အမှန်စနစ်ပါဝင်သော) စတင်အလုပ်လုပ်နေပါပြီ...")

# ပြီးခဲ့တဲ့အလှည့်က အချက်အလက်တွေကို မှတ်ထားဖို့အတွက် variable
last_period_id = None
last_prediction = None

while True:
    try:
        current_time = datetime.now()
        period_id = current_time.strftime("%Y%m%d%H%M")
        
        # --- အဆင့် (၁) ပြီးခဲ့တဲ့အလှည့်အတွက် အမှား/အမှန် ရလဒ်အရင်ထုတ်ပေးခြင်း ---
        if last_period_id is not None:
            # တကယ့်ဂိမ်းရလဒ်နေရာမှာ (လောလောဆယ် ကွန်ပျူတာက Random စနစ်နဲ့ မှန်/မှား စစ်ပေးမှာဖြစ်ပါတယ်)
            actual_result = random.choice(["BIG", "SMALL"])
            
            if last_prediction == actual_result:
                status_text = "🎯 RESULT: WIN ✅"
            else:
                status_text = "🎯 RESULT: LOSE ❌"
                
            result_message = f"""
🔔 <b>PERIOD ရလဒ်အဖြေထွက်ပါပြီ</b>
_______________

🆔 PERIOD : {last_period_id}
✨ ကိုယ်တွက်ခဲ့သည် : <b>{last_prediction}</b>
🎲 တကယ်ထွက်သည် : <b>{actual_result}</b>
_______________

📊 {status_text}
"""
            bot.send_message(CHAT_ID, result_message, parse_mode='HTML')
            time.sleep(2) # စာနှစ်စောင် ထပ်မသွားအောင် ၂ စက္ကန့် ခဏခြားပေးတာပါ
        
        # --- အဆင့် (၂) အလှည့်အသစ်အတွက် Signal အသစ် ထပ်မံခန့်မှန်းခြင်း ---
        game_options = ["BIG", "SMALL"]
        prediction = random.choice(game_options)
        
        new_signal_message = f"""
🛰 <b>TRX WINGO 1M SIGNAL</b>
_______________

🆔 PERIOD : {period_id}
🎯 PREDICT : <b>{prediction}</b>
💎 METHOD : PREMIUM AI
_______________

📝 NOTE: 8စောင်ပြီးမှဆော့ပါ ‼️
👤 DEV : Bကော့💫
"""
        
        bot.send_message(CHAT_ID, new_signal_message, parse_mode='HTML')
        print(f"Period {period_id} အတွက် Signal ပို့ပြီး၊ အဟောင်းကို အမှားအမှန်စစ်ပြီးပါပြီ။")
        
        # ယခုအလှည့်တွေကို နောက်တစ်မိနစ်မှာ ပြန်စစ်ဖို့ သိမ်းထားလိုက်တယ်
        last_period_id = period_id
        last_prediction = prediction
        
    except Exception as e:
        print("Error တစ်ခုခုတက်သွားပါတယ်၊ ဂရုနာမည် စစ်ပေးပါရန်။")
    
    # ၁ မိနစ် (စက္ကန့် ၆၀) ပြည့်အောင် စောင့်ပါတယ်
    time.sleep(60)
