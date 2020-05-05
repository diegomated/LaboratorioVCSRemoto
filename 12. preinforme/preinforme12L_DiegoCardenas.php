<?php

function menormayor ($a){
    $mm=array(0,0);
    for($i=0;$i<count($a);$i++){
        if ($i==0) {
            $mm[0]=$a[$i];
            $mm[1]=$a[$i];
        }
        elseif ($a[$i]>$mm[0] or $a[$i]<$mm[1]){
            if ($a[$i]>$mm[0]){
                $mm[0]=$a[$i];
            }
            if ($a[$i]<$mm[1]){
                $mm[1]=$a[$i];
            }
        }
    }
    return $mm;
}

function media ($a){
    $acu=0;
    for($i=0;$i<count($a);$i++){
        $acu=$acu+$a[$i];
    }
    return $acu/count($a);
}

function mediana($a){
    $acu=0;
    sort($a, SORT_REGULAR);
    $pm=count($a)/2;
    $median=($a[$pm]+$a[$pm+1])/2;
    return $median;
}

function temperatura($a){
    $temp=array();
    for ($i=0;$i<count($a);$i++){
        $temp[]=(round((($a[$i]*(1/101.3))*510)/(17.16*0.082),2));
    }
    return $temp;
}

function desviacion($a,$b){
    $desv=0;
    for($i=0;$i<count($a);$i++){
        $desv=$desv+(pow($a[$i]-$b,2))/count($a);
    }
    $desv=round(sqrt($desv),2);
    return $desv;
}



$presiones=array(110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85);
$mayormenor=menormayor($presiones);

echo "Diferencia de la mayor y la menor presion: ".($mayormenor[0]-$mayormenor[1]."<br/>");
echo "Promedio: ".round(media($presiones),2)."<br/>";
echo mediana($presiones)."<br/>";
temperatura($presiones);
echo "Desviacion: ".desviacion(temperatura($presiones),media(temperatura($presiones)));



?>
