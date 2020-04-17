<?php
    $hab=array(
    array(array(3,2),array(3,3),array(1,1),array(3,2),array(2,4),array(2,1),array(3,2)),
    array(array(2,2),array(2,3),array(2,2),array(3,3),array(2,1),array(5,1),array(2,3)),
    array(array(4,2),array(4,2),array(3,4),array(4,1),array(1,4),array(2,3),array(4,3)),
    array(array(2,2),array(2,4),array(1,2),array(2,2),array(1,2),array(4,2),array(5,6)),
    array(array(3,2),array(2,2),array(2,3),array(2,5),array(2,3),array(1,4),array(3,3)),
    array(array(4,2),array(1,2),array(3,2),array(3,2),array(4,2),array(2,2),array(6,5)),
    array(array(2,2),array(4,4),array(2,1),array(4,3),array(2,1),array(2,4),array(7,4)),
    );
    
    echo "En la habitacion ".$_POST['piso']."0".$_POST['hab']." hay: "."<br/>";
    echo $hab[$_POST['piso']-1][$_POST['hab']-1][0]." hombres viviendo"."<br/>";
    echo $hab[$_POST['piso']-1][$_POST['hab']-1][1]." mujeres viviendo";
?>