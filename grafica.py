from matplotlib import pyplot 
# Función cuadrática.
def f1(x):
    return x **2 -2*x**3

def graficar(POBLACION,generacion):
    pyplot.title('Grafica de la funcion: f(x) = (x**2)-(2x**3)\n Generacion:'+str(generacion+1),color='red',size=10, family='arial')
    print(POBLACION[0].x)
    
    x = range(-70, 70)
    pyplot.plot(x, [f1(i) for i in x])
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="red")
    pyplot.xlim(-14, 20)
    pyplot.ylim(-10, 30)
    pyplot.xlabel('X_axis\nIndividuo mas apto de esta generacion'+str(POBLACION[0].x)+' tiene una aptitud de: '+str(POBLACION[0].aptitud), size = 6)
    pyplot.ylabel('Y_axis', size = 14)
    for individuo in POBLACION:
        pyplot.annotate("Individuo: "+str(individuo.cromosoma), (individuo.x, individuo.aptitud))
        dot = pyplot.scatter(individuo.x, individuo.aptitud)

    pyplot.savefig("output.png")
    pyplot.show()

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
    pyplot.title('Evolucion del individuo mas apto a traves de las generaciones',color='red',size=10, family='arial')


    pyplot.plot(x1,y1,linestyle='solid',color='blue',label="mas aptos")
    pyplot.plot(x1,y1,'o',color='black')
    pyplot.plot(x2,y2,linestyle='solid',color='red',label="menos apto")
    pyplot.plot(x2,y2,'o',color='black')
    pyplot.plot(x3,y3,linestyle='solid',color='green',label="promedio")
    pyplot.plot(x3,y3,'o',color='black')
    pyplot.legend(loc ="upper left")
    pyplot.xlabel('Numero de la generacion')
    pyplot.ylabel('Aptitud')
    pyplot.show()
