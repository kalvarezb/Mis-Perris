function checkFecha() {

    var fecha = document.getElementById("fechaNac").value;
    fecha = new Date(fecha.slice(6, 10), fecha.slice(3, 5) - 1, fecha.slice(0, 2));
    fecha2 = new Date(2001, 00, 01);
    //fecha=fecha.getTime();
    //var diff_ms = Date.now()-fecha;
    if (fecha > fecha2) { fechaNac.setCustomValidity('Menor de edad' + fecha + ' - ' + fecha2); return false; }
    fechaNac.setCustomValidity('');
}