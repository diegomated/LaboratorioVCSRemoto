<?php

$kellogs=array(27834,23789,30189,30967,32501,32701,31665,17155,4614,834);
$acu=0;
for($i=0;$i<10;$i++){
    $acu=$acu+$kellogs[$i];
}
echo "El promedio es: ".$acu;
?>