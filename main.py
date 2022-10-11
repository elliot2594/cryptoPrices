from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sqlite3
from datetime import datetime


def main():
    getPrices()


def test():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '60835c74-ff6f-4b5b-8638-697280611453',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)






## Get prices

def getPrices():


    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

    parameters = {
        'slug': 'solana',
        'convert': 'GBP'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '60835c74-ff6f-4b5b-8638-697280611453',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      price = data['data']['5426']['quote']['GBP']['price']

      updateDB(price)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)



def updateDB(price):
    db_file = 'crypto.db'
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    
    
    with sqlite3.connect(db_file) as conn:
        print(date + ': Created the connection!')
        conn.execute("insert into solana (date, price) values (?,?);",(date, price))
        print(date + ': Inserted values into the table!')
        conn.commit()
            
    print(date + ': Automatically closed the connection!')
    

if __name__ == "__main__":
    main()

