import matplotlib.pyplot as plt



def graficar_aptos(aptos,menosApto,promedio):
    x1=[]
    y1=[]
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    i = 1
    for apto in aptos:
        x1.append(i)
        i = i+1
        y1.append(apto.aptitud)
    i = 1
    for apto in menosApto:
        x2.append(i)
        i = i+1
        y2.append(apto.aptitud)
    i = 1
    for prom in promedio:
        x3.append(i)
        i = i+1
        y3.append(prom)
    plt.title('Evolucion del individuo mas apto a traves de las generaciones',color='red',size=10, family='arial')


    plt.plot(x1,y1,linestyle='solid',color='blue',label="mas aptos")
    plt.plot(x1,y1,'o',color='black')
    plt.plot(x2,y2,linestyle='solid',color='red',label="menos apto")
    plt.plot(x2,y2,'o',color='black')
    plt.plot(x3,y3,linestyle='solid',color='green',label="promedio")
    plt.plot(x3,y3,'o',color='black')
    plt.legend(loc ="upper left")
    plt.xlabel('Numero de la generacion')
    plt.ylabel('Aptitud')
    plt.show()
