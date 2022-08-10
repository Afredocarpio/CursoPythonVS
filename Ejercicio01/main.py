"""Al realizar una consulta en un registro hemos obtenido una cadena de texto al revés. Al parecer contiene el nombre de un alumno, la nota de un exámen y la materia. Realiza lo siguiente:

Voltea la cadena y guárdala en una variable llamada cadena_volteada. Puedes devolver una cadena volteada usando un tercer índice negativo con slicing tal que así: cadena[::-1]

Extrae el nombre y apellido del alumno y almacénalos en una variable llamada nombre.

Extrae la nota y almacénala en una variable llamada nota.

Extrae la materia y almacénala en una variable llamada materia.

Genera exactamente la siguiente estructura formateando las anteriores variables en una cadena llamada cadena_formateada donde NOMBRE, APELLIDO, NOTA y MATERIA hacen referencia a las variables extraídas:

NOMBRE APELLIDO ha sacado un NOTA en MATERIA
Notas y consejos:

Todas las variables del enunciado deben existir y contener el valor correcto para pasar las pruebas.

Utiliza slicing para extraer las porciones de la cadena que te interesan.

Crea tantas variables como necesites para hacerlo más sencillo.

Utiliza el formateo de variables todo lo que puedas."""



cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

cadena_volteada = cadena_corrupta[::-1]

print (cadena_volteada)

nombre = cadena_volteada[0:12]
nota = cadena_volteada[13:16]
materia = cadena_volteada[17:]

print (f'{nombre} ha sacado un {nota} en {materia}')

