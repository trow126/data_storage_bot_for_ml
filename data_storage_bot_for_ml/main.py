import sys
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

import ccxt
import pandas as pd
from numpy import float64

from datetime import datetime
import time
import pprint

def main():
    args = sys.argv
    
    # args = []
    # args.append('BTC/USDT')
    # args.append('binance')

    symbol = 'BTC/USDT'
    exchange = eval('ccxt.' + args[1] + '()')
    
    date_str = datetime.now().strftime('%Y%m%d')
    
    df_board_col = ['ask_price_0', 'ask_price_1', 'ask_price_2', 'ask_price_3', 'ask_price_4', 'ask_price_5', 'ask_price_6', 'ask_price_7', 'ask_price_8', 'ask_price_9',
                    'ask_size_0', 'ask_size_1', 'ask_size_2', 'ask_size_3', 'ask_size_4', 'ask_size_5', 'ask_size_6', 'ask_size_7', 'ask_size_8', 'ask_size_9',
                    'bid_price_0', 'bid_price_1', 'bid_price_2', 'bid_price_3', 'bid_price_4', 'bid_price_5', 'bid_price_6', 'bid_price_7', 'bid_price_8', 'bid_price_9',
                    'bid_size_0', 'bid_size_1', 'bid_size_2', 'bid_size_3', 'bid_size_4', 'bid_size_5', 'bid_size_6', 'bid_size_7', 'bid_size_8', 'bid_size_9']

    for i in range(10):

        ohlcvs = exchange.fetch_ohlcv(symbol=symbol, timeframe='1m', limit=2)
        ohlcv = ohlcvs[0]
        index = [datetime.fromtimestamp(ohlcv[0]/1000)]
        ohlcv = pd.DataFrame([ohlcv[1:]], index=index, columns=['open', 'high', 'low', 'close', 'volume'])
        
        data_file_path = './data/{}/{}_{}_ohlcv_1m.csv'.format(args[1], date_str, args[1])
        if os.path.isfile(data_file_path):
            ohlcv.to_csv(data_file_path, mode='a', header=False)
        else:
            ohlcv.to_csv(data_file_path, mode='a', header=True)

        orderbook = exchange.fetch_order_book(symbol)
        #ask=buy bid=sell
        df_ask = pd.DataFrame(orderbook['asks'], columns=['ask_price', 'ask_size'])
        df_bid = pd.DataFrame(orderbook['bids'], columns=['bid_price', 'bid_size'])
        df_board_tmp = pd.concat([df_ask.head(10), df_bid.head(10)], axis=1)
        df_board = pd.concat([df_board_tmp['ask_price'], df_board_tmp['ask_size'], df_board_tmp['bid_price'], df_board_tmp['bid_size']], axis=0)
        df_board.reset_index(inplace=True, drop=True)
        df_board = pd.DataFrame(df_board).T
        df_board.columns = df_board_col
        df_board.index = index

        data_file_path = './data/{}/{}_{}_board_1m.csv'.format(args[1], date_str, args[1])
        if os.path.isfile(data_file_path):
            df_board.to_csv(data_file_path, mode='a', header=False)
        else:
            df_board.to_csv(data_file_path, mode='a', header=True)

        time.sleep(60)

if __name__ == '__main__':
    # try:
    #     main()
    # except Exception as e:
    #     print(e)
    main()