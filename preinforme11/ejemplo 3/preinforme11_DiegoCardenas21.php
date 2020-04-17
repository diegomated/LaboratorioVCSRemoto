<?php
    $destino=array(
    array(array(array("avianca","cosmos"),array("avianca","copa airlines"),array("avianca","easy fly")),array(array("avianca","easy fly"),array("cosmos","copa airlines"),array("cosmos","copa airlines"))),
    array(array(array("avianca","copa airlines"),array("easy fly","cosmos"),array("avianca","easy fly")),array(array("cosmos","copa airlines"),array("cosmos","copa airlines"),array("cosmos","copa airlines"))),
    array(array(array("easy fly","copa airlines"),array("cosmos","copa airlines"),array("cosmos","copa airlines")),array(array("avianca","cosmos"),array("avianca","easy fly"),array("avianca","copa airlines"))),
    array(array(array("avianca","copa airlines"),array("easy fly","copa airlines"),array("avianca","copa airlines")),array(array("easy fly","copa airlines"),array("avianca","copa airlines"),array("cosmos","copa airlines"))),
    array(array(array("easy fly","copa airlines"),array("avianca","copa airlines"),array("cosmos","copa airlines")),array(array("cosmos","copa airlines"),array("avianca","cosmos",),array("cosmos","copa airlines"))),
    array(array(array("avianca","copa airlines"),array("easy fly","cosmos"),array("avianca","easy fly")),array(array("cosmos","copa airlines"),array("cosmos","copa airlines"),array("cosmos","copa airlines"))),
    array(array(array("easy fly","copa airlines"),array("cosmos","copa airlines"),array("avianca","copa airlines")),array(array("avianca","copa airlines"),array("cosmos","copa airlines"),array("easy fly","cosmos"))),
    );
    
    if($_POST['hor']==0 && $_POST['dest']==0){
        for($i=0;$i<2;$i++){
            echo "-----Horario ".($i+1).": "."<br/>";
            for($a=0;$a<3;$a++){
                echo "--Destino ".($a+1).": "."<br/>";
                for($e=0;$e<2;$e++){
                    echo $destino[$_POST['dia']-1][$i][$a][$e].", ";
                }
                echo "<br/>";
            }
            echo "<br/>"."<br/>";
        }
    }
    else{
        echo "Aerolineas disponibles dia ".$_POST['dia'].", horario ".$_POST['hor'].", Destino ".$_POST['dest']."<br/>";
        for($i=0;$i<2;$i++){
            echo $destino[$_POST['dia']-1][$_POST['hor']-1][$_POST['dest']-1][$i].", ";
        }
        
    }
?>
<form method="POST" action="preinforme11_DiegoCardenas.php">
    <input type="submit" value="Atras">
</form>
