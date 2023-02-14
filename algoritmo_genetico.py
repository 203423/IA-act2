import random
import itertools
import math
import grafica
import graf_aptos
from tkinter import *
import tkinter as tk
from numpy import mean

class Individuo:
    def __init__(self,cromosoma,x,aptitud,id,cromosomaBinario):
        self.cromosoma = cromosoma
        self.x = x
        self.aptitud = aptitud
        self.id = id
        self.cromosomaBinario = cromosomaBinario

class Genes():
    def __init__(self,id,gen,probMuta,muta):
        self.gen = gen
        self.probMuta = probMuta
        self.id = id
        self.muta = muta


class Pareja:
    def __init__(self,idParejas,probCruza):
        self.idParejas = idParejas
        self.probCruza = probCruza



#Metodo de seleccion
def seleccion_par(pob):
    masApto = pob[0]
    parejas = []
    for i in range(1,len(pob)):
        pareja = (masApto,pob[i])
        parejas.append(pareja)


    listID = []
    for x in range(0,len(pob)):
        listID.append(pob[x].cromosoma)
    parejas = list(itertools.combinations(listID, 2))
    return parejas
    
 
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

def binario_a_decimal(binario):
    return int(binario, 2)

def calcularX(xmin,i,intervalo):
    return xmin + i * intervalo

# Función cuadrática.
def f1(x):
    return x **2 -2*x**3

def porcentaje():
    valor = random.randint(0,100)
    valor = valor/100
    return valor



#ESTOS METODOS SE ESTARAN REPITIENDO HASTA QUE EL ALGORITMO RECIBA SU VALOR PARA PARAR
def nuevosIndividuos(POBLACION, numBits, xmin, xinterval,xmax,id_ind,PMAX):
    #AQUI EMPIEZA LA CRUZA
    #Seleccion de parejas que pueden cruzar
    PC = 0.60
    parejas = seleccion_par(POBLACION) #todas las posibles parejas para cruza
    print(str(parejas))

    paresCruzas = []
    for x in parejas:
        probCruza = porcentaje()
        if probCruza <= PC:
            temp = list(tuple(x))
            paresCruzas.extend(temp) #Aqui se almacenan las parejas que si van a poder cruzarse

    print("ARR: ParesCruza:")
    print(paresCruzas)
    #Cruza
    cruzBin = []
    for x in paresCruzas:
        for i in range(0,len(POBLACION)):
            if x == POBLACION[i].cromosoma:
                cruzBin.append(POBLACION[i].cromosomaBinario) #CONVIERTE A BINARIO EL VALOR DE LOS INDIVIDUO A CRUZAR
                break
    print("CRUZBIN")
    print(cruzBin)

    #Se define el punto de cruza de todos los individuos que se cruzaran
    puntoCruza =  round(5/2)
    newPob = []
    #Se generan los nuevos individuos, que pasaran a la mutacion
    for x in range(0,len(cruzBin),2):
        val1 = cruzBin[x]
        val2 = cruzBin [x+1]
        cruzBin[x] = val1
        cruzBin[x+1] = val2
        newVal1 = val1[0:puntoCruza] + val2[puntoCruza:]
        newVal2 = val2[0:puntoCruza] + val1[puntoCruza:]
        newPob.append(newVal1)
        newPob.append(newVal2)

    print("Poblacion antes de mutar:")
    print(newPob)

    #MUTACION
    PMI = 0.60
    PMG = 0.50

    ##MUTA EL INDIVIDUO?
    arrGenes = []

    for x in range(0,len(newPob)):
        PMI_ind = porcentaje()
        print("PROBABILIDAD QUE MUTE EL INDIVIDUO:"+str(PMI_ind))
        if PMI_ind <=  PMI:
            genes = newPob[x]
            print("El valor "+newPob[x]+" mutara")
            newPob[x]='x'
            for i in range(0,len(genes)):
                PMG_ind = porcentaje()
                muta = False
                if PMG_ind <= PMG:
                    muta = True 
                arrGenes.append(Genes(x,genes[i], PMG_ind,muta))
            #MUTA POR GEN

    individuoNuevo = 0
    genmutado = ''
    genesmutados = []
    
    for gen in arrGenes:
        genmutado = genmutado+gen.gen
        if len(genmutado) == numBits:
            genesmutados.append(genmutado)
            genmutado = ''
    print(genesmutados)
    print('-------------------------LINEA DE DEBUG -------------------------------')

    newGenes = []
    for cadena in genesmutados:
        index = 0
        temp = []
        print('-------------------------CADENA ANTES DE MUTAR --------------------')
        print(cadena)
        for caracter in cadena:
            temp.append(caracter)
        print(temp)
        for caracter in temp:
            if porcentaje() <= PMG:
                replaceI = random.randint(0,len(temp)-1)
                print('Index:'+str(index)+'caracter'+str(caracter)+'intercambiara lugar con la posicion'+str(replaceI))
                cambio = temp[replaceI]
                temp[replaceI] = caracter
                temp[index] = cambio
            index = index + 1
        index = 0
        print('-------------------------CADENA DESPUES DE MUTAR --------------------')
        print(temp)
        newGenes.append(''.join(map(str,temp)))
    print('ARREGLO DE CARACTERES MUTADOS')
    print(newGenes)
    print('ARREGLO DE LA POBLACION')
    print(newPob)        

    y = 0
    print("NEWPOB")
    print(newPob)
    print("GENESMUTADOS")
    print(newGenes)
    for x in range(0,len(newPob)):
        if newPob[x] == 'x':
            newPob[x] = newGenes[y]
            y = y+1
    y = 0
    print("poblacion despues de mutar")
    print(newPob)

    PoblacionNueva = []
    for x in newPob:
        cromosoma = binario_a_decimal(x)
        xPob = calcularX(xmin, cromosoma, xinterval)
        funcion = f1(xPob)
        if xPob < xmin or xPob>xmax:
            xPob = "OUT"
            funcion = "OUT"
        PoblacionNueva.append(Individuo(cromosoma,xPob,funcion,id_ind,x)) 
        id_ind = id_ind +1

    print("POSIBLES POBLADORES NUEVOS")
    for poblador in PoblacionNueva:
        print("Individuo "+str(poblador.cromosoma) + " x del individuo "+str(poblador.x)+" Ind en binario "+str(poblador.cromosomaBinario)+ " y su aptitud es de:"+str(poblador.aptitud))
        if poblador.x != "OUT":
            POBLACION.append(poblador)
            

    print("POBLACION DESPUES DE AGREGAR LOS NUEVOS INDIVIDUOS")

    POBLACION = sorted(POBLACION,key=lambda poblador: poblador.aptitud, reverse=True)
    for poblador in POBLACION:
        print("ID:"+str(poblador.id)+"| Individuo "+str(poblador.cromosoma) + " x del individuo "+str(poblador.x)+" Ind en binario "+str(poblador.cromosomaBinario)+ " y su aptitud es de:"+str(poblador.aptitud))

    #PODA
    numero_a_podar = len(POBLACION) - PMAX
    for i in range(numero_a_podar):
        if len(POBLACION) > PMAX:
            POBLACION.pop(random.randint(0,len(POBLACION)-1))
    print("Nueva poblacion despues de la poda")
    for poblador in POBLACION:
        print("Individuo "+str(poblador.cromosoma) + " x del individuo "+str(poblador.x)+" Ind en binario "+str(poblador.cromosomaBinario)+ " y su aptitud es de:"+str(poblador.aptitud))
    
    return POBLACION







#CONFIGURAACIONES INICIALES DEL ALGORITMO

def main(pobmax,generaciones,min,max):
    id_ind = 0
    PMAX = int(pobmax)
    numGeneraciones = int(generaciones)
    PINICIAL = (random.randint(2,5))
    xmin = int(min)
    xmax = int(max)
    rango = xmax - xmin
    xinterval = 1
    numpuntos = (rango/xinterval) + 1
    numPuntosBi = str(decimal_a_binario(numpuntos))
    numBits = len(numPuntosBi)
    POBLACION = []


    for x in range(PINICIAL):
        POBLACION.append(Individuo(random.randint(0,10),0,0,id_ind,''))
        id_ind = id_ind + 1
    print("El rango es = "+str(rango))
    print("La cantidad de puntos es = "+ str(numpuntos))
    print("La cantidad de bits es = "+ str(numBits))
    print("Poblacion Inicial: "+str(PINICIAL))
    print('La poblacion maxima es:'+str(PMAX))


#IMPRIME EL CROMOSOMA DE LOS INDIVIDUOS
    for x in range(0,len(POBLACION)):
        print("EL cromosoma del individuo "+str(POBLACION[x].id) +" es: "+str(POBLACION[x].cromosoma))

#SE CALCULA X DE LOS INDIVIDUOS, SU APTITUD Y SU BINARIO
    for i in range(0,len(POBLACION)):
        x = calcularX(xmin, POBLACION[i].cromosoma, xinterval)
        POBLACION[i].x = x
        POBLACION[i].aptitud = f1(POBLACION[i].x)
        POBLACION[i].cromosomaBinario = decimal_a_binario(POBLACION[i].cromosoma)
        while len(POBLACION[i].cromosomaBinario) < numBits:
            POBLACION[i].cromosomaBinario = "0"+ POBLACION[i].cromosomaBinario
        print("Individuo:"+str(POBLACION[i].id)+"Con cromosoma:" +str(POBLACION[i].cromosoma)+"- x: "+str(POBLACION[i].x)+" su aptitud es "+str(POBLACION[i].aptitud)+" y su binario es "+str(POBLACION[i].cromosomaBinario))

#AQUI EMPIEZA LA CRUZA
    masApto = []
    menosApto = []
    promedio = []
    aptitudes = []
    for generacion in range(numGeneraciones):
        POBLACION = nuevosIndividuos(POBLACION, numBits, xmin, xinterval,xmax,id_ind,PMAX)
        masApto.append(POBLACION[0])
        menosApto.append(POBLACION[len(POBLACION)-1])
        aptitudes = []
        for ind in POBLACION:
            aptitudes.append(ind.aptitud)
        promedio.append(mean(aptitudes))
        grafica.graficar(POBLACION,generacion)
    for apto in masApto:
        print(apto.x)
    
    graf_aptos.graficar_aptos(masApto,menosApto,promedio)
    
def send_data():
  global total
  min_info = min.get()
  max_info = max.get()
  pobMax_info = pobMax.get()
  generaciones_info = generaciones.get()

 
  total = 3000
  main(pobMax_info,generaciones_info,min_info,max_info)

if __name__ == "__main__": 
    ventana = Tk()
    ventana.geometry("1200x600")
    ventana.title("Algoritmo génetico canonico")
    ventana.resizable(False,False)
    frame_izquierda = tk.Frame(ventana, width=700, height=750, pady=10, padx=5)
    frame_derecha = tk.Frame(ventana, width=700, height=750, pady=10, padx=5)
    frame_derecha.pack(side="right")
    frame_izquierda.pack(side="left")
    ventana.config(background = "#FFFFFF")
    max_label = Label(frame_izquierda, text = "xmax")
    max_label.place(x = 22, y = 190)
    min_label = Label(frame_izquierda, text = "xmin")
    min_label.place(x = 22, y = 250)
    pobMax_label = Label(frame_izquierda, text = "POB MAX")
    pobMax_label.place(x = 22, y = 310)
    generaciones_label = Label(frame_izquierda, text = "Numero de generaciones")
    generaciones_label.place(x = 22, y = 370)
    max = StringVar()
    min = StringVar()
    pobMax = StringVar()
    generaciones = StringVar()
    max_entry = Entry(frame_izquierda, textvariable = max, width = 40,)
    min_entry = Entry(frame_izquierda, textvariable = min, width = 40,)
    pobMax_entry = Entry(frame_izquierda, textvariable = pobMax, width = 40)
    generaciones_entry = Entry(frame_izquierda, textvariable = generaciones, width = 40)
    max_entry.place(x = 22, y = 220)
    min_entry.place(x = 22, y = 280)
    pobMax_entry.place(x = 22, y = 340)
    generaciones_entry.place(x = 22, y = 400)
    submit_btn = Button(frame_izquierda, text="Continuar", command = send_data)
    submit_btn.place(x = 22, y = 480)
    ventana.mainloop()






