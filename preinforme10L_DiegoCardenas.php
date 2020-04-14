<?php

$kellogs=array(27834,23789,30189,30967,32501,32701,31665,17155,4614,834);
$acu=0;
for($i=0;$i<10;$i++){
    $acu=$acu+$kellogs[$i];
}
echo "El promedio es: ".$acu."<br/>";

$menor=0;
$mayor=0;
for($i=0;$i<10;$i++){
    if ($i==0){
        $mayor=$kellogs[0];
    }elseif($kellogs[$i]>$mayor){
        $mayor=$kellogs[$i];
    }
    if ($i==0){
        $menor=$kellogs[0];
    }elseif($kellogs[$i]<$menor){
        $menor=$kellogs[$i];
    }
}
$dif=$mayor-$menor;
echo "la diferencia de la mayor y menor utilidad es: ".$dif;

?>