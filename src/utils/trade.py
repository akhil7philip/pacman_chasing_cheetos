import logging
import pandas as pd
import json
import time
import datetime as dt

from utils import db_helpers, http
from settings import FMCLOUD_API_KEY

lg = logging.getLogger()


def get_companies_list_fmpcloud(db):
    from models.base_models import Company
    
    stock_list = http.http_requests("https://fmpcloud.io/api/v3/stock/list?apikey=%s"%FMCLOUD_API_KEY)
    if stock_list:
        df = pd.DataFrame(stock_list)
        df = df.set_index('exchange').loc[['National Stock Exchange of India','Bombay Stock Exchange'],'symbol'].reset_index()
        df.rename(columns={'symbol':'name'}, inplace=True)
        values = df.to_dict('records')
        db_helpers.save_values(values, db, Company)
        return values
    

def get_ticker_data_fmpcloud():
    from models.base_models import Company
    
    companies = Company.query.all()
    for company_record in companies:
        ticker_data = http.http_requests(f"https://fmpcloud.io/api/v3/quote/{company_record.name}?apikey={FMCLOUD_API_KEY}")
        lg.info(ticker_data)
        break


def get_companies_list(alice):
    alice.get_contract_master("MCX")
    alice.get_contract_master("NFO")
    alice.get_contract_master("NSE")
    alice.get_contract_master("BSE")
    alice.get_contract_master("CDS")
    alice.get_contract_master("BFO")
    alice.get_contract_master("INDICES")


def get_ticker_data(alice):
    # https://v2api.aliceblueonline.com/websocket
    """
    t - type, tf - tick feed, tk - tick acknowledgement
    e - exchange
    tk - token
    lp - LTP (Last traded price)
    pc - Percentage change
    cv - change value (Absolute change in price)
    v - volume
    o - open
    h - high
    l - low
    c - close
    ap - Average Price
    symbol - Symbol Name
    """

    LTP = 0
    socket_opened = False
    subscribe_flag = False
    subscribe_list = []
    unsubscribe_list = []

    def socket_open():  # Socket open callback function
        lg.info("Connected")
        global socket_opened
        socket_opened = True
        if subscribe_flag:  # This is used to resubscribe the script when reconnect the socket.
            alice.subscribe(subscribe_list)

    def socket_close():  # On Socket close this callback function will trigger
        global socket_opened, LTP
        socket_opened = False
        LTP = 0
        lg.info("Closed")

    def socket_error(message):  # Socket Error Message will receive in this callback function
        global LTP
        LTP = 0
        lg.error("Error :", message)

    def feed_data(message):  # Socket feed data will receive in this callback function
        global LTP, subscribe_flag
        feed_message = json.loads(message)
        if feed_message["t"] == "ck":
            lg.info("Connection Acknowledgement status :%s (Websocket Connected)" % feed_message["s"])
            subscribe_flag = True
            lg.info(f"subscribe_flag : {subscribe_flag}")
            lg.info("-------------------------------------------------------------------------------")
            pass
        elif feed_message["t"] == "tk":
            lg.info("Token Acknowledgement status :%s " % feed_message)
            lg.info("-------------------------------------------------------------------------------")
            pass
        else:
            lg.info(f"Feed : {feed_message}")
            LTP = feed_message['lp'] if 'lp' in feed_message else LTP

    # Socket Connection Request
    alice.start_websocket(socket_open_callback=socket_open, socket_close_callback=socket_close,
                        socket_error_callback=socket_error, subscription_callback=feed_data, 
                        run_in_background=True, market_depth=False)

    time.sleep(5)
    lg.info(f'{socket_opened=}')
    while not socket_opened:
        subscribe_list = [alice.get_instrument_by_symbol("NSE", "RELIANCE")]
        alice.subscribe(subscribe_list)
        lg.info(dt.datetime.now())
        time.sleep(5)