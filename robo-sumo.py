counter = 0
def control(inputs):
    global counter
    chaoEsq = inputs["front-left"]
    chaoDir = inputs["front-right"]
    distance_right = inputs["distance-right"]
    distance_left  = inputs["distance-left"]

    leftSpeed = 0
    rightSpeed = 0
    if (distance_right < 300 and distance_left == 300) or chaoEsq  > 0.25 or chaoDir > 0.25:
        # oponente a direita ou chao a esquerda => vire a direita
        leftSpeed  = 12;
        rightSpeed = 10;
    elif (distance_right==300 and distance_left<300) or chaoDir > 0.25 or chaoEsq > 0.25:
        # oponente a esquerda ou chao a direita => vire a esquerda
        leftSpeed  = -10;
        rightSpeed = -12;
    elif distance_right<300 and distance_left<300:
        # oponente a frente => acelere
        leftSpeed  = 20;
        rightSpeed = -20;
        if chaoDir > 0.25 and chaoEsq > 0.25:
            #se encontrar a borda vire
            leftSpeed  = -30;
            rightSpeed = 30;
    elif distance_right==300 and distance_left==300:
        # oponente fora da vista => gire a procura dele
        leftSpeed  =  5;
        rightSpeed =  5;
        if chaoDir > 0.25 or chaoEsq > 0.25:
            counter = 2
            leftSpeed =  -30
            rightSpeed = +30
            
    return {
        'leftSpeed':  leftSpeed + 10,
        'rightSpeed': rightSpeed - 10,
        'log': [
            { 'name': 'Right', 'value': chaoDir, 'min': -1.1, 'max': 1.1 },
            { 'name': 'Left', 'value': chaoEsq, 'min': -1.1, 'max': 1.1 },
            { 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 },
            { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        ]
    }