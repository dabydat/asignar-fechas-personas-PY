from calendar import monthrange
from datetime import datetime,date
import random

personas = {
    0: {"nombre":'PRUEBA - 1', "fecha": ''},
    1: {"nombre":'PRUEBA - 2', "fecha": ''},
    2: {"nombre":'PRUEBA - 3', "fecha": ''},
    3: {"nombre":'PRUEBA - 4', "fecha": ''},
    4: {"nombre":'PRUEBA - 5', "fecha": ''},
    5: {"nombre":'PRUEBA - 6', "fecha": ''},
    6: {"nombre":'PRUEBA - 7', "fecha": ''},
    7: {"nombre":'PRUEBA - 8', "fecha": ''},
    8: {"nombre":'PRUEBA - 9', "fecha": ''},
    9: {"nombre":'PRUEBA - 10', "fecha": ''},
    10:{"nombre":'PRUEBA - 11', "fecha": ''},
    11:{"nombre":'PRUEBA - 1', "fecha": ''},
    12:{"nombre":'PRUEBA - 13', "fecha": ''},
    13:{"nombre":'PRUEBA - 14', "fecha": ''},
    14:{"nombre":'PRUEBA - 15', "fecha": ''},
    15:{"nombre":'PRUEBA - 16', "fecha": ''},
    16:{"nombre":'PRUEBA - 17', "fecha": ''},
    17:{"nombre":'PRUEBA - 18', "fecha": ''},
    18:{"nombre":'PRUEBA - 19', "fecha": ''},
    19:{"nombre":'PRUEBA - 20', "fecha": ''},
    20:{"nombre":'PRUEBA - 21', "fecha": ''},
    22:{"nombre":'PRUEBA - 22', "fecha": ''},
    23:{"nombre":'PRUEBA - 23', "fecha": ''},
    24:{"nombre":'PRUEBA - 24', "fecha": ''},
    25:{"nombre":'PRUEBA - 25', "fecha": ''},
    26:{"nombre":'PRUEBA - 26', "fecha": ''},
    27:{"nombre":'PRUEBA - 27', "fecha": ''},
    28:{"nombre":'PRUEBA - 28', "fecha": ''},
    29:{"nombre":'PRUEBA - 29', "fecha": ''},
}

# Función que obtiene los dias dado un mes, y un año
def getDays(anio, mes, nuevo_cantidad_dias = 0):
    hoy = date(anio, mes, 1)
    anio = hoy.year
    mes = hoy.month
    cantidad_dias_mes = monthrange(anio, mes)[1]

    dias_del_mes = [date(anio, mes, dia) for dia in range(1, cantidad_dias_mes+1)]
    dias_del_mes = gettingWeekdays(dias_del_mes)

    if nuevo_cantidad_dias != 0:
        dias_del_mes = gettingWeekdays(dias_del_mes)
        finalDays = slice(nuevo_cantidad_dias)
        dias_del_mes = dias_del_mes[finalDays]

    return dias_del_mes

# Funcion que asigna la fecha a la persona seleccionada
def addPerson(j, day, list_days):
    try:
        if day != None:
            personas[j]['fecha'] = day.strftime("%d/%m/%Y")
            if day in list_days:
                list_days.remove(day)
    except Exception as e:
        return e

# Función que escoge un día al azar
def randomDay(days):
    randomDay = random.choice(days)
    return randomDay

# Función que elimina los fines de semana, y retorna los días de semana
def gettingWeekdays(monthDays):
    weekdays = []
    for i in monthDays:
        weekday = i.weekday()
        
        if weekday < 5:
            weekdays.append(i)

    return weekdays

# Función que cuenta la cantidad de personas sin fecha
def getNonDate(dictionary, value):
    counter = 0
    for x, y in dictionary.items():
        if y[value] == "":
            counter = counter + 1
    return counter

#Función que asigna la fecha de forma aleatoria
def assignDate(keysDictList, daysList):
    cantidad = 0
    nuevo_cantidad_dias = 1
    fecha_inicio = daysList[0]
    for i in keysDictList:
        try:
            if daysList != []:
                diaRandom = randomDay(daysList)
                addPerson(i, diaRandom, daysList)
            else:
                if cantidad == 0:
                    cantidad = getNonDate(personas, 'fecha')

                    anio = fecha_inicio.year
                    # Sumarle uno al mes es para que sea una pesona por día, si le quitamos el '+1' asignará personas equitativamente en el mes
                    mes = fecha_inicio.month+1

                    if mes > 12:
                        anio = anio + 1
                        mes = 1
                    # Si no queremos que asigne fechas dada una cantidad de personas, sino aleatoriamente, quitamos la variable cantidad si quitamos el '+1'
                    list_new_days = getDays(anio, mes, cantidad)
        
                new_day = randomDay(list_new_days)
                addPerson(i, new_day, list_new_days)
                
                nuevo_cantidad_dias = nuevo_cantidad_dias + 1
        except Exception as e:
            if e:
                print(e)

# Función para ordenar las personas por fecha
def orderByDate(dictionary, orderValue):
    dictionary_values = list(dictionary.values())
    mylist = sorted(dictionary_values, key = lambda x:datetime.strptime(x[orderValue], '%d/%m/%Y'), reverse=True)
    mylist.reverse()
    return mylist

# Función para obtener las llaves de un diccionario
def getKeysOfDict(dictionary):
    keysListed = list(dictionary.keys())
    random.shuffle(keysListed)
    return keysListed

personasList = getKeysOfDict(personas)
dias_del_mes = getDays(2022, 12)

assignDate(personasList, dias_del_mes)
mylist = orderByDate(personas, 'fecha')
for i in mylist:
    print(i["nombre"] + " ---> Fecha: " + i["fecha"])
