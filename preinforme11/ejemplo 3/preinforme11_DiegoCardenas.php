<html>
<head>
    <title>Mi documento básico</title>
</head>
<body>
    <form method="POST" action="preinforme11_DiegoCardenas21.php">
        <p>Aerolineas disponibles</p>
        <font size="2">puedes mirar los vuelos del dia, poniendo el dia correspondiente y 0 en las otras casillas</font>
        <br/><br/>
        Dia de la semana <input type="integer" name="dia">
        <br/>
        <font size="2">(1)Lunes (2)Martes (3)Miercoles (4)Jueves (5)Viernes (6)Sabado (7)Dmingo</font>
        <br/><br/>
        Horario <input type="integer" name="hor">
        <br/>
        <font size="2">(1)Mañana o (2)tarde</font>
        <br/><br/>
        Destino <input type="integer" name="dest">
        <br/>
        <font size="2">(1)canada (2)Estados unidos (3)japon</font>
        <br/><br/>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>