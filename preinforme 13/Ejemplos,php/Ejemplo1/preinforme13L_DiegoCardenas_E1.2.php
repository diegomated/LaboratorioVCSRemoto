<form method="POST" action="preinforme13L_DiegoCardenas_E1.1.php">
<?php
    $cuenta=array("diegomated" => [8764,"diego"],"pepito" => [1234,"pepe"]);
    $var=false;
    $var2=false;
    foreach ($cuenta as $usuario => $contra){
        if($_POST['user']==$usuario and $_POST['contra']==$contra[0]){
            echo "Bienvenido ".$contra[1]."<br>";
            $var=true;
        }
        elseif($var!=true and $var2!=true){
            echo "Usuario incorrecto";
            $var2=true;
        }
    }
?>
<input type="submit" value="Ok">
</form>