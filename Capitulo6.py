from iqoptionapi.stable_api import IQ_Option
from datetime import datetime, timedelta
import sys, getpass, stdiomask
import time


def Martingale(valor, payout):
	lucro_esperado = valor * payout
	perdida = float(valor)	
		
	while True:
		if round(valor * payout, 2) > round(abs(perdida) + lucro_esperado, 2):
			return round(valor, 2)
			break
		valor += 0.01

def Payout(par):
	API.subscribe_strike_list(par, 1)
	while True:
		d = API.get_digital_current_profit(par, 1)
		if d != False:
			d = round(int(d) / 100, 2)
			break
		time.sleep(1)
	API.unsubscribe_strike_list(par, 1)
	
	return d



Email = input('EMAIL IQ:  ')
passw = stdiomask.getpass(' INGRESE SU PASSWORD :: ', mask='0')
print('Conectando su cuenta ...')
API = IQ_Option(Email, passw)
API.connect()


API.change_balance('PRACTICE') # PRACTICE / REAL


def stop(lucro, gain, loss):
	if lucro <= float('-' + str(abs(loss))):
		print('Stop Loss Alcanzado!')
		sys.exit()
		
	if lucro >= float(abs(gain)):
		print('Stop Win Alcanzado!')
		sys.exit()


while True: 
	if API.check_connect() == False:
		print( 'Upppss, error al conectar....')

		API.connect()
	else:
		print( '\nConectado con exito!!!')
		break


par = input(' Indique el par para operar: ').upper()
valor_entrada = float(input(' Indique um valor para entrar: '))
valor_entrada_b = float(valor_entrada)
martingale = int(input(' Indique cantidad de martingales: '))
martingale += 1
stop_loss = float(input(' Indique valor de Stop Loss: '))
stop_gain = float(input(' Indique valor de Stop Win: '))

timeframe = 1

velas = API.get_candles(par, (int(timeframe) * 60), 20,	 time.time())
ultimo = round(velas[0]['close'], 4)
primero = round(velas[-1]['close'], 4)

diferenca = abs( round( ( (ultimo - primero) / primero ) * 100, 3) )
tendencia = "CALL" if ultimo < primero and diferenca > 0.01 else "PUT" if ultimo > primero and diferenca > 0.01 else False
print(f' La tendencia es {tendencia} !\n')

lucro = 0
payout = Payout(par)
while True:
	minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
	entrar = True if (minutos >= 4.58 and minutos <= 5)  and minutos >= 9.58	else False
	print('Hora de entrar?',entrar,'/ Minutos:',minutos, end='\r')
	if entrar:
		print('\n\nIniciando operacion!')
		dir = False
		print('Verificando colores..', end='')
		velas = API.get_candles(par, 60, 3, time.time())	

		
		velas[0] = 'g' if velas[0]['open'] < velas[0]['close'] else 'r' if velas[0]['open'] > velas[0]['close'] else 'd'
		velas[1] = 'g' if velas[1]['open'] < velas[1]['close'] else 'r' if velas[1]['open'] > velas[1]['close'] else 'd'
		velas[2] = 'g' if velas[2]['open'] < velas[2]['close'] else 'r' if velas[2]['open'] > velas[2]['close'] else 'd'
		
		colores = velas[0] + ' ' + velas[1] + ' ' + velas[2]		
		print(colores)
	
		if colores.count('g') > colores.count('r') and colores.count('d') == 0 and tendencia =="PUT" : dir = 'put'
		if colores.count('r') > colores.count('g') and colores.count('d') == 0 and tendencia =="CALL": dir = 'call'
		if dir:
			print('Direcion:',dir)
			valor_entrada = valor_entrada_b
            for i in range(martingale):
                status,id = API.buy_digital_spot(par, valor_entrada, dir, 1)
                
                if status:
                
                    while True:
                        status,valor = API.check_win_digital_v2(id)
                        
                        if status:
                            valor = valor if valor > 0 else float('-' + str(abs(valor_entrada)))
                            lucro += round(valor, 2)
                            print('Resultado : ', end='')
                            print('WIN /' if valor > 0 else 'LOSS /' , round(valor, 2) ,'/', round(lucro, 2),('/ '+str(i)+ ' MG' if i > 0 else '' ))	
                            valor_entrada = Martingale(valor_entrada, payout)
                            stop(lucro, stop_gain, stop_loss)
                            

                            break
                    if valor > 0 : break
                else:
                    print('\nERROR AL REALIZAR OPERACION\n\n')
				
	time.sleep(0.5)		   