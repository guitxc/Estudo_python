'''
CONSTANTE = "variavel" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''
velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGER = 1 # A distancia onde o radar pega

# Letras maiusculas para coisas que não vão mudar, ou não 
# se deve mudar a variavel

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGER) and \
    local_carro  <= (LOCAL_1 - RADAR_RANGER)


if vel_carro_passou_radar_1:
    print('A velocidade passou do radar 1')

if local_carro >= (LOCAL_1 + RADAR_RANGER) and \
    local_carro (LOCAL_1 - RADAR_RANGER) and \
        velocidade > RADAR_1:
    print('carro multado em radar 1')

