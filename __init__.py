# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os
import sys
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'PDF2XLSX' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import requests
import random
import pdftables_api

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "pdftables":
    pdf_file = GetParams("pdf")
    path = GetParams("path")
    api_key = GetParams("apikey")

    if not path.endswith(".xlsx"):
        path += ".xlsx"

    try:
        c = pdftables_api.Client(api_key)
        c.xlsx(pdf_file, path)
    except Exception as e:
        PrintException()
        raise e
