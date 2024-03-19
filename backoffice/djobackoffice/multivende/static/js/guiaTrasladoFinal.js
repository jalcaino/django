var baseurl = "http://172.18.18.27:83";

$(document).ready(function () {
    var ot_orden_transito_numero = $("#ot_orden_transito_numero_guia").val()
    var url = baseurl+'/verGuiaTraslado/guia_traslado' + ot_orden_transito_numero;
    window.open(url, '_blank');
});

$("#btnGuiaFinalVer").click(function () {
    var ot_orden_transito_numero = $("#ot_orden_transito_numero_guia").val()
    var url = baseurl+'/verGuiaTraslado/guia_traslado' + ot_orden_transito_numero;
    window.open(url, '_blank');
});