
par ='EURUSD'
entrada_base = 5
soros_lucro = 0.0
soros_porcentage = round(80 / 100, 2 )
soros_nivel = 1
soros_actual = 0




while True:
    entrada = float(entrada_base)
    if soros_lucro > 0.0:
        if soros_actual <= soros_nivel :
            entrada = round(entrada_base + (soros_lucro * soros_porcentage), 2)
            
        else:
            soros_lucro = 0.0
            soros_actual = 0
            
        

    status,id = API.buy_digital_spot(par, valor_entrada, dir, 1)
    if status:
        print('Entrada Realizada')
        status = False
    
        while status = False:
            status,valor = API.check_win_digital_v2(id)
            
            if status:
                valor = round(valor, 2)
                print('Soros Nivel : ', soros_actual)
                print('Resultado', end='')	
                if valor > 0:
                    soros_lucro = valor
                    soros_actual += 1 
                    print('WIN  ', valor)
                    
                elif valor < 0:
                    soros_lucro = 0.0
                    soros_actual = 0 
                    print('Loss  ', valor)
                    
                else:
                    print('EMPATE')
