def guardar_registro(tipo_solicitud, datos):
    """Guarda los datos de las solicitudes, a su vez genera un ID por cada registro"""
    ruta = "data/" + tipo_solicitud + ".txt"
    lineas_existentes = leer_lineas_archivo(ruta)
  
# Id
    nuevo_id = 1
    if len(lineas_existentes) > 0:
        ultima_linea = lineas_existentes[-1].strip()
        partes = ultima_linea.split(";")
        nuevo_id = int(partes[0]) + 1

    linea_a_guardar = str(nuevo_id)

    for valor in datos.values():
        linea_a_guardar = linea_a_guardar + ";" + str(valor)

    linea_a_guardar = linea_a_guardar + "\n"

# Conservar tildes
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(linea_a_guardar)

    return nuevo_id

def leer_lineas_archivo(ruta):
    """Lee el archivo y devuelve una lista de líneas"""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        # Si no se crea el archivo
        return []

def leer_registros(tipo_solicitud, llaves):
    """Lee el registro"""
    ruta = "data/" + tipo_solicitud + ".txt"
    lineas = leer_lineas_archivo(ruta)

    lista_registros = []

    for linea in lineas:
        linea_limpia = linea.strip()
        partes = linea_limpia.split(";")

        if len(partes) > 0:
            registro = {}
            registro["id"] = partes[0]

            i = 1
            while i < len(partes) and i <= len(llaves):
                registro[llaves[i-1]] = partes[i]
                i += 1

            lista_registros.append(registro)

    return lista_registros

def actualizar_registro(tipo_solicitud, id_buscar, llaves, datos_nuevos):
    """Actualiza el registro y busca cada uno con su ID"""
    ruta = "data/" + tipo_solicitud + ".txt"
    lineas = leer_lineas_archivo(ruta)
    nuevas_lineas = []

    encontrado = False
    i = 0

    while i < len(lineas):
        linea_limpia = lineas[i].strip()
        partes = linea_limpia.split(";")

        if len(partes) > 0 and partes[0] == str(id_buscar):
            nueva_linea = str(id_buscar)

            for llave in llaves:
                nueva_linea = nueva_linea + ";" + str(datos_nuevos[llave])

            nueva_linea = nueva_linea + "\n"

            nuevas_lineas.append(nueva_linea)
            encontrado = True
        else:
            nuevas_lineas.append(lineas[i])

        i += 1

    if encontrado:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.writelines(nuevas_lineas)

    return encontrado
