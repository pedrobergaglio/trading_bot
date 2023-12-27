from iqoptionapi.stable_api import IQ_Option
import time
import random
I_want_money=IQ_Option("pepobergaglio@gmail.com","Iqliverpool63!")

while True: 
	if I_want_money.check_connect() == False:
		print( 'Upppss, error al conectar....')

		I_want_money.connect()
	else:
		print( '\nConectado con exito!!!')
		break

ACTIVES="EURUSD"
duration=1#minute 1 or 5
amount=1
I_want_money.subscribe_strike_list(ACTIVES,duration)
#get strike_list
print("suscripto")
data=I_want_money.get_realtime_strike_list(ACTIVES, duration)
print("get strike data")
print(data)
"""data
{'1.127100': 
    {  'call': 
            {   'profit': None, 
                'id': 'doEURUSD201811120649PT1MC11271'
            },   
        'put': 
            {   'profit': 566.6666666666666, 
                'id': 'doEURUSD201811120649PT1MP11271'
            }	
    }............
} 
"""
#get price list
price_list=list(data.keys())
#random choose Strategy
choose_price=price_list[random.randint(0,len(price_list)-1)]
#get instrument_id
instrument_id=data[choose_price]["call"]["id"]
#get profit
profit=data[choose_price]["call"]["profit"]
print("choose you want to buy")
print("price:",choose_price,"side:call","instrument_id:",instrument_id,"profit:",profit)
#put instrument_id to buy
buy_check,id=I_want_money.buy_digital(amount,instrument_id)
polling_time=5
if buy_check:
    print("wait for check win")
    #check win
    while True:
        check_close,win_money=I_want_money.check_win_digital_v2(id,polling_time)
        if check_close:
            if float(win_money)>0:
                win_money=("%.2f" % (win_money))
                print("you win",win_money,"money")
            else:
                print("you loose")
            break
    I_want_money.unsubscribe_strike_list(ACTIVES,duration)
else:
    print("fail to buy,please run again")