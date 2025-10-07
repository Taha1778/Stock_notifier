def threshold_ind(Stock):
    Binary_dict={}
    for _,row in Stock.iterrows():
        if row['daily_return'] >= 3:
            print(f"Alert: {row['Company']} ({row['Ticker']}) has a big gain with a a daily return of {row['daily_return']}")
            Binary_dict[row['Company']]=True
        elif row['daily_return'] >=1:
            print(f"Notice: {row['Company']} ({row['Ticker']}) has a moderate gain with a daily return of {row['daily_return']}")
            Binary_dict[row['Company']]=True
        elif row['daily_return'] <= -3:
            print(f"Alert: {row['Company']} ({row['Ticker']}) has a big loss with a daily return of {row['daily_return']}")
            Binary_dict[row['Company']]=True
        elif row['daily_return'] <= -1:
            print(f"Notice: {row['Company']} ({row['Ticker']}) has a moderate loss with a daily return of {row['daily_return']}")
            Binary_dict[row['Company']]=True
        else:
            Binary_dict[row['Company']]=False
    return Binary_dict


def message_generator(Stock, Binary_dict):
    Messages=[]
    for _,row in Stock.iterrows():
        if Binary_dict[row['Company']]==True:
            msg=f"{row['Company']} ({row['Ticker']}) had a daily return of {row['daily_return']}% with a price range of {row['price_range']}% and a volatility of {row['volatility']}% on {row['Date']}"
            Messages.append(msg)
    return Messages
    