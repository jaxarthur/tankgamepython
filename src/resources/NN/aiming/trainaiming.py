import numpy, random, math
from keras.models import Sequential
from keras.layers import Dense, Activation

def creatraindata(amount):
    temp = []
    for i in range(amount):
        temp.append([random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500)])
    return temp

def getclosest(inputs):
    distance = 1000
    maxdist = 10
    x, y, tx, ty = inputs
    while distance > maxdist:
        angle = random.randint(-90,90)
        power = random.randint(0,100)
        distance = simulatebullet(angle, power, (x, y), (tx, ty))
        
    return [power, angle]

def simulatebullet(angle, power, selfpos, enemypos):
    bulletx, bullety = selfpos
    bulletmx = math.sin(math.radians(angle))*power/2
    bulletmy = math.cos(math.radians(angle))*power/2
    alive = True
    
    while alive:
        bulletx = bulletx + bulletmx/5
        bullety = bullety + bulletmy/5
        bulletmy = bulletmy - 1/5
        if bulletx > 1000 or bulletx < 0 or bullety < 0:
            alive = 0
        elif bulletmy < 0 and bullety < enemypos[1]:
            alive = 0

    offsetx = bulletx - enemypos[0]
    offsety = bullety - enemypos[1]
    return(math.sqrt(math.pow(offsetx, 2) + math.pow(offsety, 2)))


def generatetrainigdata(amount):
    tempin = creatraindata(amount)
    tempout = []
    for i, data in enumerate(tempin):
        if i % 10 == 0:
            print(str(int(i/amount*100)) + '%')
        powerraw, angleraw = getclosest(data)
        power = powerraw/100
        angle = (angleraw + 90)/180
        tempout.append([power, angle])

    return tempin, tempout

print("creating test data")
inputs, outputs = generatetrainigdata(10000)

numpyinput = numpy.array(inputs)
numpyoutput = numpy.array(outputs)

print("building model")
model = Sequential()
model.add(Dense(4, input_shape=(4,)))
model.add(Activation('relu'))
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dense(8))
model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('sigmoid'))

model.compile(optimizer='sgd', loss='mse', metrics=['acc'])

print("training")
model.fit(numpyinput, numpyoutput, epochs=150, batch_size=10)

print(model.evaluate(numpyinput, numpyoutput))
model.save("model.h5")