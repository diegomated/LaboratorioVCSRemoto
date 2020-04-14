<?php

$kellogs=array(27834,23789,30189,30967,32501,32701,31665,17155,4614,834);
$p1=($kellogs[0]+$kellogs[1])/2;
$p2=($kellogs[count($kellogs)-1]+$kellogs[count($kellogs)-2])/2;
$dif=$p1-$p2;
echo "Diferencia de los 2 primeros años a los 2 ultimos años: ".$dif."<br/>";


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

echo "La diferencia de la mayor y menor utilidad es: ".$dif."<br/>";

$acu1=0;
$kellogs2=array(27834,23789,30189,30967,32501,32701,31665,17155,4614,834);
for($i=0;$i<10;$i++){
    for($a=0;$a<9;$a++){
        if($kellogs2[$a]>$kellogs2[$a+1]){
            $acu1=$kellogs2[$a];
            $kellogs2[$a]=$kellogs2[$a+1];
            $kellogs2[$a+1]=$acu1;
        }
    }
}

$m1=count($kellogs2)/2;
$m2=(count($kellogs2)/2)+1;
$mediana=($kellogs2[$m1-1]+$kellogs2[$m2-1])/2;
echo "La mediana es: ".$mediana."<br/>";

$acuD=0;
$prom=0;
for($i=0;$i<10;$i++){
    $acuD=$acuD+$kellogs[$i];
}

for($i=0;$i<10;$i++){
    $act=$i+1;
    echo "Promedio del año: ".$act.": ".round((100*$kellogs[$i])/$acuD,2)."%"."<br/>";
}


?>