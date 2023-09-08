import numpy as np
import matplotlib.pyplot as plt

def eulers(C, A, v_slutt, plot_result):
    dt=t_slutt/(n)
    #Vektorer/arrays
    a = np.zeros(n)  #akselerasjon
    v = np.zeros(n)  #fart
    y = np.zeros(n)  #posisjon
    t = np.zeros(n)  #tid

    #Initialbetingelser
    v[0] = v_0  #startfart
    y[0] = y_0  #startposisjon
    t[0] = t_0  #starttid
    
    v_98 = v_slutt * 0.98 #98% av terminalhastighet

    #Eulers metode
    for i in range(n-1):
        a[i] = g-((C*p*A)/(2*m))*v[i]**2   #utledet fra Newtons 2. lov
        v[i+1] = v[i] + a[i]*dt
        y[i+1] = y[i] - v[i]*dt
        t[i+1] = t[i] + dt

        if(v[i]<v_98<v[i+1]):
            print(f"Tid før 98% terminalhastighet: {round(i*dt, 1)} s")
            print(f"Meter falt ved 98% terminalhastighet: {round(y[0]-y[i+1], 1)} m")
    
    if (plot_result):
        plotResult(t, y, v, a)

def plotResult(t, y, v, a):
    #plotter akselerasjonsgrafen
    plt.subplot(3,1,1)
    plt.plot(t,a,'b-')
    plt.title('Akselerasjon')
    plt.xlabel('tid/s')
    plt.ylabel('akselerasjon/(m/s^2)')
    plt.grid()

    #plotter fartsgrafen
    plt.subplot(3,1,2)
    plt.plot(t,v,'r-')
    plt.title('Fart')
    plt.xlabel('tid/s')
    plt.ylabel('fart/(m/s)')
    plt.grid()

    #plotter possisjonsgrafen
    plt.subplot(3,1,3)
    plt.plot(t,y,'g-')
    plt.title('Posisjon')
    plt.xlabel('tid/s')
    plt.ylabel('posisjon/m')
    plt.grid()

#fysiske størrelse
g = 9.81  #tyngdeakselerasjon
m = 70   #massen til Alfred og Bjarne
p = 1.23 #lufttettheten

#startverdier
t_0 = 0 #start tiden
v_0 = 0 #start farten
y_0 = 3500 #start høyden

#euler spesifikke verdier
n = 100000 #antall steg
t_slutt = 50 #slutt tiden
    
print("Alfred")
C = 0.7 #Drag koeffisienten
A = 0.17 #Arealet
v_slutt = 96.9 #terminalhastigheten
plott_result = False #om resultatet skal plottes eller ikke

eulers(C, A, v_slutt, plott_result)

print()

print("Bjarne")
C = 1.0 #Drag koeffisienten
A = 1.0 #Arealet
v_slutt = 33.4 #terminalhastigheten
plott_result = False #om resultatet skal plottes eller ikke

eulers(C, A, v_slutt, plott_result)