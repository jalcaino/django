#Imports Django
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import smtplib
from django.shortcuts import render,redirect
from django.conf import settings as conf_setting
from django.db import transaction
import multivende.models as modeloMultivende
import pyodbc
#from PyPDF2 import PdfFileMerger
from django.http import FileResponse
from fpdf import  FPDF


from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader


#Imports tipos de datos
from django.utils.timezone import make_aware
import http.client
import json
from datetime import datetime as datedate
from .import funciones
import datetime as date
from dateutil import tz
from django.conf import settings as conf_setting
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


#Import para validar SKU
from collections import Counter




@login_required
def Home(request):

    listaa3 =funciones.ListaTraslado(request)

    return render (request,'index.html',{'listaa': listaa3})

@login_required
def Boletaspdf(request):
   
  
    FOLIO_PDF = request.GET.get('numero')
    print(f'PARAMETROS: {FOLIO_PDF}')  

  
    path = GeneraMasivaBoletas(FOLIO_PDF) 

    
    if path!="-1":
        path=path + 'invoice.pdf'
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('courier', 'B', 16)
        pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
        pdf.cell(40, 10, '',0,1)
        pdf.set_font('courier', '', 12)
        pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
        pdf.line(10, 30, 150, 30)
        pdf.line(10, 38, 150, 38)

        return FileResponse(open(path, 'rb'), as_attachment=False, content_type='application/pdf')
    
    else:
        return render (request,'boletaspdf.html')


def GeneraMasivaBoletas(N_VENTA_PDF): #GENERACION DE BOLETAS MASIVAS POR FOLIO SEPARADO POR COMA
    
 
    DIRECTORIOS_CONFIG_BOLETAS=conf_setting.DATOS_CONFIG['boletas']
    print(f'CARPETA DE BOLETAS: {DIRECTORIOS_CONFIG_BOLETAS}')  

    
    Lista_Boletas = []
    for N_VENTA in N_VENTA_PDF.split(','):
        Lista_Boletas.append(N_VENTA.strip())
    pdfs = Lista_Boletas
    print(Lista_Boletas)
    #merger = PdfFileMerger()
    merger = PdfMerger()
    
    try:
        for pdf in pdfs:
            try:
                merger.append(f'{DIRECTORIOS_CONFIG_BOLETAS}/{pdf}.pdf') #/var/www/htmlpython/sovosdte
            except:
                continue
        merger.write(f"{DIRECTORIOS_CONFIG_BOLETAS}/invoice.pdf") #/var/www/htmlpython/sovosdte
    except NameError as Ne:
        print(f'ERROR: {Ne}|WARNING')
        return "-1"

    print('SE HA GENERADO EL PDF INVOICE CON EXITO|INFO')
    
    merger.close()
        
    path = f'{DIRECTORIOS_CONFIG_BOLETAS}/'
    
    print(f"PATH: {path}|INFO")
    print('FINALIZA LA GENERACION MASIVA|SUCCESS')
    
    return path


def salir(request):
    logout(request)
    messages.info(request,"Sesion Cerrada")
    return redirect("/")


def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)
def error_500(request, exception):
        data = {}
        return render(request,'500.html', data)