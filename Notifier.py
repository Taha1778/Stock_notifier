import requests
def send_message(message):
        Token='8301577448:AAHSqE7mBGyNnzb5scBqDlN_dErJEm0dezU'
        Chat_ID="2058609968"
        URL=f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={Chat_ID} &text={message}"
        r=requests.get(URL)
        print(r.json())
        return "Message Sent Successfully"
