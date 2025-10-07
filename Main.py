from Data_fetcher import *
from Alert_Manager import threshold_ind, message_generator
from Notifier import *
from Automation_function import *
import json
with open('config.json', 'r') as f:
        config = json.load(f)
companies=config['tickers']
set_time=config['schedule_time']

def Total_function(companies):
    Stock=fetch_data(companies)
    Binary_dict=threshold_ind(Stock)
    Messages=message_generator(Stock, Binary_dict)
    for msg in Messages:
        send_message(msg)
    return "All Messages Sent Successfully"
Automation_function(Total_function,companies,set_time)