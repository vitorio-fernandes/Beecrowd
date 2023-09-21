entrada = int(input())

hora = entrada // 3600
minutos = entrada % 3600
minutos = minutos//60

segundos = entrada%60

print("{}:{}:{}".format(hora,minutos,segundos))
