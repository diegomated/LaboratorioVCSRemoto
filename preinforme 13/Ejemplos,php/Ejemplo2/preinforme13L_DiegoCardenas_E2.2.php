<form method="POST" action="preinforme13L_DiegoCardenas_E2.1.php">
<?php
    $cuenta=array("diego" => [3173887502,1001369364],
                    "juan" => [3127836040,1001052814],
                    "marcelo" => [3164291235,1001796716],
                    "karla" => [3154140759,1001094978],
                    "karen" => [3113521883,1001652806]);
    
    echo "Datos de ".$_POST['user']."<br>";
    echo "Telefono: ".$cuenta[$_POST['user']][0]."<br>";
    echo "Cedula: ".$cuenta[$_POST['user']][1]."<br>";
?>
<input type="submit" value="Ok">
</form>