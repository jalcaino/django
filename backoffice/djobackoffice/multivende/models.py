# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aplicacion(models.Model):
    id_app = models.AutoField(db_column='ID_APP', primary_key=True)  # Field name made lowercase.
    desc_app = models.CharField(db_column='DESC_APP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    client_id_app = models.CharField(db_column='CLIENT_ID_APP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secret_client_id_app = models.CharField(db_column='SECRET_CLIENT_ID_APP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email_app = models.CharField(db_column='EMAIL_APP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pass_app = models.CharField(db_column='PASS_APP', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APLICACION'


class BoletaMultivende(models.Model):
    venta_id = models.BigIntegerField(db_column='VENTA_ID', primary_key=True)  # Field name made lowercase.
    boleta_url = models.CharField(db_column='BOLETA_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.
    update_at = models.DateTimeField(db_column='UPDATE_AT')  # Field name made lowercase.
    estado = models.IntegerField(db_column='ESTADO')  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rut = models.CharField(db_column='RUT', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETA_MULTIVENDE'


class CodigoAutorizacion(models.Model):
    id_code = models.AutoField(db_column='ID_CODE', primary_key=True)  # Field name made lowercase.
    desc_code = models.CharField(db_column='DESC_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    disable_code = models.BooleanField(db_column='DISABLE_CODE', blank=True, null=True)  # Field name made lowercase.
    id_app = models.ForeignKey(Aplicacion, models.DO_NOTHING, db_column='ID_APP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CODIGO_AUTORIZACION'


class Configuracion(models.Model):
    configuracion_pk = models.CharField(db_column='CONFIGURACION_PK', primary_key=True, max_length=40)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=100)  # Field name made lowercase.
    valor = models.CharField(db_column='VALOR', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIGURACION'


class EnvioMailBoleta(models.Model):
    venta_id = models.BigIntegerField(db_column='VENTA_ID', primary_key=True)  # Field name made lowercase.
    identificador_orden = models.CharField(db_column='IDENTIFICADOR_ORDEN', max_length=20)  # Field name made lowercase.
    fecha_hora = models.DateTimeField(db_column='FECHA_HORA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENVIO_MAIL_BOLETA'


class EstadosInternos(models.Model):
    estados_internos_pk = models.IntegerField(db_column='ESTADOS_INTERNOS_PK', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADOS_INTERNOS'


class MediosPago(models.Model):
    medio_pago_id = models.CharField(db_column='MEDIO_PAGO_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    medio_pago_label = models.CharField(db_column='MEDIO_PAGO_LABEL', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDIOS_PAGO'


class Token(models.Model):
    id_token = models.BigAutoField(db_column='ID_TOKEN', primary_key=True)  # Field name made lowercase.
    first_token = models.TextField(db_column='FIRST_TOKEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    refresh_token = models.CharField(db_column='REFRESH_TOKEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_exp = models.DateTimeField(db_column='FECHA_EXP', blank=True, null=True)  # Field name made lowercase.
    fecha_cre = models.DateTimeField(db_column='FECHA_CRE', blank=True, null=True)  # Field name made lowercase.
    fecha_upd = models.DateTimeField(db_column='FECHA_UPD', blank=True, null=True)  # Field name made lowercase.
    fecha_exp_refresh = models.DateTimeField(db_column='FECHA_EXP_REFRESH', blank=True, null=True)  # Field name made lowercase.
    disable_token = models.BooleanField(db_column='DISABLE_TOKEN', blank=True, null=True)  # Field name made lowercase.
    id_app = models.ForeignKey(Aplicacion, models.DO_NOTHING, db_column='ID_APP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOKEN'


class TokenLog(models.Model):
    id_log = models.AutoField(db_column='ID_LOG', primary_key=True)  # Field name made lowercase.
    fecha_log = models.DateTimeField(db_column='FECHA_LOG')  # Field name made lowercase.
    estado_log = models.BooleanField(db_column='ESTADO_LOG')  # Field name made lowercase.
    id_app = models.ForeignKey(Aplicacion, models.DO_NOTHING, db_column='ID_APP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOKEN_LOG'


class Usuarios(models.Model):
    username = models.CharField(db_column='USERNAME', primary_key=True, max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIOS'


class Ventas(models.Model):
    venta_id = models.BigAutoField(db_column='VENTA_ID', primary_key=True)  # Field name made lowercase.
    field_id = models.CharField(db_column='_ID', max_length=40)  # Field name made lowercase. Field renamed because it started with '_'.
    numero_venta = models.CharField(db_column='NUMERO_VENTA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    identificador_orden = models.CharField(db_column='IDENTIFICADOR_ORDEN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    code = models.BigIntegerField(db_column='CODE')  # Field name made lowercase.
    origin = models.CharField(db_column='ORIGIN', max_length=15)  # Field name made lowercase.
    total_payment = models.BigIntegerField(db_column='TOTAL_PAYMENT')  # Field name made lowercase.
    discount = models.BigIntegerField(db_column='DISCOUNT')  # Field name made lowercase.
    coupon_code = models.CharField(db_column='COUPON_CODE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discount_description = models.CharField(db_column='DISCOUNT_DESCRIPTION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipo_pago = models.CharField(db_column='TIPO_PAGO', max_length=50)  # Field name made lowercase.
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  # Field name made lowercase.
    boleta_url = models.CharField(db_column='BOLETA_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    venta_estado_id = models.CharField(db_column='VENTA_ESTADO_ID', max_length=2)  # Field name made lowercase.
    sold_at = models.DateTimeField(db_column='SOLD_AT')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT')  # Field name made lowercase.
    numero_tarjeta = models.CharField(db_column='NUMERO_TARJETA', max_length=24, blank=True, null=True)  # Field name made lowercase.
    codigo_autorizador = models.BigIntegerField(db_column='CODIGO_AUTORIZADOR', blank=True, null=True)  # Field name made lowercase.
    auth_resp_cd = models.CharField(db_column='AUTH_RESP_CD', max_length=8, blank=True, null=True)  # Field name made lowercase.
    medio_pago_id = models.CharField(db_column='MEDIO_PAGO_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    delivery_code = models.CharField(db_column='DELIVERY_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warehouse = models.CharField(db_column='WAREHOUSE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre_cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email_cliente = models.CharField(db_column='EMAIL_CLIENTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    procesada = models.IntegerField(db_column='PROCESADA', blank=True, null=True)  # Field name made lowercase.
    in_cod_boletapagocaja = models.BigIntegerField(db_column='IN_COD_BOLETAPAGOCAJA', blank=True, null=True)  # Field name made lowercase.
    in_cod_transaccionpagocaja = models.BigIntegerField(db_column='IN_COD_TRANSACCIONPAGOCAJA', blank=True, null=True)  # Field name made lowercase.
    in_cod_pedidobodega = models.BigIntegerField(db_column='IN_COD_PEDIDOBODEGA', blank=True, null=True)  # Field name made lowercase.
    in_cod_periodocaja = models.BigIntegerField(db_column='IN_COD_PERIODOCAJA', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENTAS'



class VentasTotales(models.Model):
    venta_id = models.BigAutoField(db_column='VENTA_ID', primary_key=True)  # Field name made lowercase.
    field_id = models.CharField(db_column='_ID', max_length=40)  # Field name made lowercase. Field renamed because it started with '_'.
    numero_venta = models.CharField(db_column='NUMERO_VENTA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    identificador_orden = models.CharField(db_column='IDENTIFICADOR_ORDEN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    code = models.BigIntegerField(db_column='CODE')  # Field name made lowercase.
    origin = models.CharField(db_column='ORIGIN', max_length=15)  # Field name made lowercase.
    total_payment = models.BigIntegerField(db_column='TOTAL_PAYMENT')  # Field name made lowercase.
    discount = models.BigIntegerField(db_column='DISCOUNT')  # Field name made lowercase.
    coupon_code = models.CharField(db_column='COUPON_CODE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discount_description = models.CharField(db_column='DISCOUNT_DESCRIPTION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipo_pago = models.CharField(db_column='TIPO_PAGO', max_length=50)  # Field name made lowercase.
    folio = models.IntegerField(db_column='FOLIO', blank=True, null=True)  # Field name made lowercase.
    boleta_url = models.CharField(db_column='BOLETA_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    venta_estado_id = models.CharField(db_column='VENTA_ESTADO_ID', max_length=2)  # Field name made lowercase.
    sold_at = models.DateTimeField(db_column='SOLD_AT')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT')  # Field name made lowercase.
    numero_tarjeta = models.CharField(db_column='NUMERO_TARJETA', max_length=24, blank=True, null=True)  # Field name made lowercase.
    codigo_autorizador = models.BigIntegerField(db_column='CODIGO_AUTORIZADOR', blank=True, null=True)  # Field name made lowercase.
    auth_resp_cd = models.CharField(db_column='AUTH_RESP_CD', max_length=8, blank=True, null=True)  # Field name made lowercase.
    medio_pago_id = models.CharField(db_column='MEDIO_PAGO_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    delivery_code = models.CharField(db_column='DELIVERY_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warehouse = models.CharField(db_column='WAREHOUSE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre_cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email_cliente = models.CharField(db_column='EMAIL_CLIENTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rut_cliente = models.CharField(db_column='RUT_CLIENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    procesada = models.IntegerField(db_column='PROCESADA', blank=True, null=True)  # Field name made lowercase.
    in_cod_boletapagocaja = models.BigIntegerField(db_column='IN_COD_BOLETAPAGOCAJA', blank=True, null=True)  # Field name made lowercase.
    in_cod_transaccionpagocaja = models.BigIntegerField(db_column='IN_COD_TRANSACCIONPAGOCAJA', blank=True, null=True)  # Field name made lowercase.
    in_cod_pedidobodega = models.BigIntegerField(db_column='IN_COD_PEDIDOBODEGA', blank=True, null=True)  # Field name made lowercase.
    in_cod_periodocaja = models.BigIntegerField(db_column='IN_COD_PERIODOCAJA', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    suma_precio = models.IntegerField(db_column='SUMA_PRECIO')  # Field name made lowercase.
    suma_descuento = models.IntegerField(db_column='SUMA_DESCUENTO')  # Field name made lowercase.
    total_real = models.IntegerField(db_column='TOTAL_REAL')  # Field name made lowercase.
    comuna = models.CharField(db_column='COMUNA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre_cliente_despacho = models.CharField(db_column='NOMBRE_CLIENTE_DESPACHO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    calle = models.CharField(db_column='CALLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='CIUDAD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fono = models.CharField(db_column='FONO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numero_venta_acotado = models.CharField(db_column='NUMERO_VENTA_ACOTADO', max_length=10, blank=True, null=True)
    numero = models.CharField(db_column='NUMERO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'VENTAS_TOTALES'





class VentasEstados(models.Model):
    venta_estado_id = models.CharField(db_column='VENTA_ESTADO_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    venta_estado_label = models.CharField(db_column='VENTA_ESTADO_LABEL', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENTAS_ESTADOS'


class VentasProductos(models.Model):
    venta_id = models.BigIntegerField(db_column='VENTA_ID', primary_key=True)  # Field name made lowercase.
    sku = models.CharField(db_column='SKU', max_length=40)  # Field name made lowercase.
    precio = models.IntegerField(db_column='PRECIO')  # Field name made lowercase.
    descuento = models.IntegerField(db_column='DESCUENTO')  # Field name made lowercase.
    cantidad = models.SmallIntegerField(db_column='CANTIDAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENTAS_PRODUCTOS'
        unique_together = (('venta_id', 'sku'),)


class ErrorLog(models.Model):
    fechahora = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    error = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'error_log'
