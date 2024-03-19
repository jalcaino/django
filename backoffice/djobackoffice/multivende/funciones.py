from datetime import datetime
from xml.dom import xmlbuilder
from django.conf import settings as sett
import datetime
from multivende.models import Ventas, Usuarios, VentasTotales
from barcode import Code128
from barcode.writer import ImageWriter
from os import remove
from django.core.exceptions import ObjectDoesNotExist
from fpdf import FPDF
from django.http import  HttpResponse
import os.path
from pytz import timezone



#NO USAR POR AHORA
def ListaTraslado(request):
    
    listaa = VentasTotales.objects.using('multivende').values('venta_id','discount','field_id','numero_venta','origin','total_payment','tipo_pago','folio','boleta_url','sold_at','created_at','updated_at','numero_tarjeta','codigo_autorizador','delivery_code','nombre_cliente','email_cliente','procesada','in_cod_boletapagocaja','in_cod_transaccionpagocaja','in_cod_pedidobodega','in_cod_periodocaja','cliente','rut_cliente','total_real','comuna','nombre_cliente_despacho','calle','ciudad','fono','numero_venta_acotado','numero').filter(procesada__gte = 1)


    for x in listaa:
        
        #fechax =datetime.datetime.strftime(x['created_at'],'%Y-%m-%d')
        #fechax2 =datetime.datetime.strftime(x['created_at'],'%d-%m-%Y / %H:%M:%S')
        #fechay =datetime.datetime.strftime(x['updated_at'],'%d-%m-%Y')

        total_payment="${:,}".format(x['total_real'])
        total_payment = total_payment.replace(",", ".")
        x['total_payment'] = total_payment
        
        #reemplazamos por ajuste MELI
        x['numero_venta']=x['numero_venta_acotado']

        x['colorestado']=switch_estado_color(x['procesada'])
        x['muestralinkboleta']=x['procesada']
        x['procesada']=switch_estado(x['procesada'])
        x['origin']=switch_canal(x['origin'])
        
        """
        x['sold_at']=datetime.datetime.strftime(x['sold_at'],'%Y-%m-%d / %H:%M:%S')
        x['created_at']=datetime.datetime.strftime(x['created_at'],'%Y-%m-%d / %H:%M:%S')
        x['updated_at']=datetime.datetime.strftime(x['updated_at'],'%Y-%m-%d / %H:%M:%S')
        """
        x['sold_at']=datetime.datetime.strftime(x['sold_at'],'%Y-%m-%d / %H:%M:%S')
        x['created_at']=datetime.datetime.strftime(x['created_at'],'%Y-%m-%d / %H:%M:%S')
        x['updated_at']=datetime.datetime.strftime(x['updated_at'],'%Y-%m-%d / %H:%M:%S')
       
       
        if x['delivery_code'] == '_delivery_type_delivery':
            x['delivery_code']='Despacho a domicilio'
        else:        
            x['delivery_code']='Retiro en tienda'

        #falabella
        if x['tipo_pago'] == '46':
            x['tipo_pago']='Cheque'
        


    return listaa



def switch_estado(estado):
    if estado == 1:
        return "Boleta Generada"
    elif estado == 2:
        return "Pedido Generado"
    elif estado == 3:
        return "Folio Guardado"
    elif estado == 4:
        return "Boleta Descargada"
    elif estado == 5:
        return "Multivende Boleta en Plataforma"
    elif estado == 6:
        return "Mail Enviado"
    elif estado == 7:
        return "En www.palumbostore.cl"
    elif estado == 8:
        return "Envío Shippit"



def switch_estado_color(estado):
    if estado == 1:
        return "bg-dark"
    elif estado == 2:
        return "bg-info"
    elif estado == 3:
        return "bg-primary"
    elif estado == 4:
        return "bg-secondary"
    elif estado == 5:
        return "bg-success"
    elif estado == 6:
        return "bg-warning"
    elif estado == 7:
        return "bg-primary"
    elif estado == 8:
        return "bg-success"



def switch_canal(origen):
    if origen == "fcom":
        return "Falabella"
    elif origen == "jumpseller":
        return "Palumbo Online"
    elif origen == "mercadolibre":
        return "Mercadolibre"
    elif origen == "paris":
        return "Paris"
    elif origen == "ripley":
        return "Ripley"    
    elif origen == "dafiti":
        return "Dafiti"