var count = 0;
var codtiendaPDF = "";
var tiendaPDF = "";
var codcajaPDF = "";
var datePDF = "";
var pre1PDF = "";
var pre2PDF = "";
var baseurl = "http://172.18.18.27:83";

$(document).ready(function () {
  $('#alertTienda').hide();
  $("#codtienda").focus();
  TimeNow();
  AjaxTiendasLista();
});

function TimeNow() {
  function zero(n) {
    return (n > 9 ? '' : '0') + n;
  }
  var dateNow = new Date();
  var time = dateNow.getFullYear() + "-" + zero(dateNow.getMonth() + 1) + "-" + zero(dateNow.getDate());
  $('#date').val(time)
};

function AjaxTiendas() {
  var codtienda = $('#codtienda').val();
  $.ajax({
    url: baseurl+'/obtenerTienda/' + codtienda,
    type: "GET",
    dataType: "json",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
    success: (data) => {
      console.log(data);
      $('#tienda').val(data['nombre_tienda']);
      $("#codcaja").prop("disabled", false);
      $("#codcaja").focus();
    },
    error: (error) => {
      $('#alertTienda').show();
      $('#codtienda').val("")
      $('#tienda').val("")
      $("#codcaja").prop("disabled", true);
      $("#codtienda").focus();
    }
  });
};

function AjaxTiendasLista() {
  $.ajax({
    url: baseurl+'/obtenerListaJquery/',
    type: "GET",
    dataType: "json",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
    success: (data) => {
      console.log(data);
      var availableTags = data['listaCodTienda'];
      $("#codtienda").autocomplete({
        source: availableTags,
        select: function (event, ui) {
          $('#codtienda').val(ui.item.label);
          AjaxTiendas();
        }
      });
      var availableTags2 = data['listaCodCajas'];
      $("#codcaja").autocomplete({
        source: availableTags2,
        select: function (event, ui) {
          $("#pre1").prop("disabled", false);
          $("#pre2").prop("disabled", false);
          $("#pre1").focus();
        }
      });
    },
    error: (error) => {
      console.log(error);
    }
  });
};

$("#btnAlertTienda").click(function () {
  $('#alertTienda').hide()
});

$("#codtienda").keyup(function () {
  var lengthCodTienda = $("#codtienda").val().length;
  if (lengthCodTienda > 3) {
    AjaxTiendas()
  }
  if (lengthCodTienda > 0) {
    $('#alertTienda').hide()
  }
});

$('#codcaja').keyup(function (){
  this.value = (this.value + '').replace(/[^0-9 ]/g, '');
});

$("#codcaja").keydown((e) => {
  if (e.keyCode == 8) {
    e.preventDefault();
    var d = $("#codcaja").val();
    $("#codcaja").val(d.slice(0, -2));
  }
});

$("#codcaja").keypress(function () {
  var lengthCodCaja = $("#codcaja").val().length;
  var valorCodCaja = $("#codcaja").val();
  if (lengthCodCaja < 7 && lengthCodCaja > 0) {
    valorCodCaja = valorCodCaja + ' ';
    $("#codcaja").val(valorCodCaja);
  }
});

$("#codcaja").keyup(function () {
  var lengthCodCaja2 = $("#codcaja").val().length;
  if (lengthCodCaja2 > 5) {
    $("#pre1").prop("disabled", false);
    $("#pre2").prop("disabled", false);
    $("#pre1").focus();
  }
});

$("#pre2").keyup(function () {
  var lengthPre1 = $("#pre1").val().length;
  if (lengthPre1 > 4) {
    var lengthPre2 = $("#pre2").val().length;
    if (lengthPre2 > 4) {
      $("#addGuia").prop("disabled", false);
    }
  }
});

$("#addGuia").click(function () {
  if ($(".Lguia").length < 4) {
    valorMargin = $("#con-tainer").css("margin-top");
    valorMarginTop = parseInt(valorMargin) - 20
    valorMarginTopFinal = valorMarginTop.toString() + 'px'
    $("#con-tainer").css("margin-top", valorMarginTopFinal);
  }
  count = count + 1;
  var codtienda = $("#codtienda").val();
  var tienda = $("#tienda").val();
  var codcaja = $("#codcaja").val();
  var date = $("#date").val();
  var pre1 = $("#pre1").val();
  var pre2 = $("#pre2").val();

  $("#Guias").append(
    '<div class="input-group mb-2 Lguia" id="guiasDivs' + count +
    '"><input type="text" class="form-control codtiendaPDF" value="' + codtienda +
    '" disabled readonly style="text-transform: uppercase;"><input type="text" class="form-control tiendaPDF" value="' +
    tienda +
    '" disabled readonly><input type="text" class="form-control codcajaPDF" value="' + codcaja +
    '" disabled readonly><input type="text" class="form-control datePDF" value="' + date +
    '" disabled readonly><input type="text" class="form-control pre1PDF" value="' + pre1 +
    '" disabled readonly><input type="text" class="form-control pre2PDF" value="' + pre2 +
    '" disabled readonly><button class="btn btn-outline-danger form-control" type="button" onclick="deleteGuia(' +
    count + ')"><i class="bi bi-dash-square-fill"></i></button></div>'
  );

  if ($(".Lguia").length > 0) {
    $("#createPdf").removeClass("hiddenCreatePdf");
  } else {
    $("#createPdf").addClass("hiddenCreatePdf");
  }

  $('#codtienda').val("")
  $('#tienda').val("")
  $("#tienda").prop("disabled", true);
  $('#codcaja').val("")
  $("#codcaja").prop("disabled", true);
  $('#date').val(date)
  $('#pre1').val("")
  $("#pre1").prop("disabled", true);
  $('#pre2').val("")
  $("#pre2").prop("disabled", true);
  $("#addGuia").prop("disabled", true);
  $("#codtienda").focus();
});

function deleteGuia(ccguiasDivs) {
  $("#guiasDivs" + ccguiasDivs).remove();
  if ($(".Lguia").length == 0) {
    $("#createPdf").addClass("hiddenCreatePdf");
  }
};

$("#createPdf").click(function () {
  $(".codtiendaPDF").each(function () {
    codtiendaPDF = codtiendaPDF + "|" + $(this).val().toUpperCase();
  });

  $(".tiendaPDF").each(function () {
    tiendaPDF = tiendaPDF + "|" + $(this).val();
  });
  $(".codcajaPDF").each(function () {
    codcajaPDF = codcajaPDF + "|" + $(this).val();
  });

  $(".datePDF").each(function () {
    datePDF = datePDF + "|" + $(this).val();
  });
  $(".pre1PDF").each(function () {
    pre1PDF = pre1PDF + "|" + $(this).val();
  });

  $(".pre2PDF").each(function () {
    pre2PDF = pre2PDF + "|" + $(this).val();
  });
  var PDF = codtiendaPDF + "@@" + tiendaPDF + "@@" + codcajaPDF + "@@" + datePDF + "@@" + pre1PDF + "@@" +
    pre2PDF
  var ResponsablePDF = $('#Responsable').val()
  var PDF_FINAL = PDF + '~' + ResponsablePDF
  var encodedString = $.base64.encode(PDF_FINAL)
  $('#GuiaFinal').val(encodedString)
  console.log(PDF_FINAL);
  codtiendaPDF = ""
  tiendaPDF = ""
  codcajaPDF = ""
  datePDF = ""
  pre1PDF = ""
  pre2PDF = ""
  $("#guiaForm").submit();
});