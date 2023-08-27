import asyncio
from telethon.sync import TelegramClient
from colorama import Fore, Back, Style
import pandas as pd
import random

def main(phone,api,hash):
    GreenColor = Fore.GREEN
    whiteColor=Fore.WHITE
    try:
        print(GreenColor +f'{phone}', end=' ')
        client = TelegramClient(f"sessions/{phone}", api, hash)
        client.connect()
        if not client.is_user_authorized(): 
            client.send_code_request(phone)
            client.sign_in(phone, input    (Style.BRIGHT + Fore.GREEN + 'Enter the code: '))    
        
        print(whiteColor + 'authenticated properly \U0001F44D')  # Thumbs up emoji
    except:
        pass


def authenticatePhones():
    df = pd.read_csv('phone.csv')
    apiDf=pd.read_csv('Api.csv')

    for index, row in df.iterrows():
        num_rows = len(df)
        random_index = random.randint(0, num_rows - 1)

        selected_row = df.iloc[random_index]
        corresponding_api_row = apiDf.iloc[random_index]
        api = corresponding_api_row['API']
        hash_value = corresponding_api_row['Hash']
        phone=row['Phone']
        main(phone,api,hash_value)



