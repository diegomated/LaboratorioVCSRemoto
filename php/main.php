<?php

$num1 = 15;
$nombre = "yeyo";
$bolean = true;
$miprimerarray = array(1,2,3,4,5);
$misegundoarray = array("pito" => 1,"pote" => 2);
$sumita = 23+873;
define("puto","el que lo lea");
echo $nombre.$num1.$bolean.puto."<br/>";
echo $miprimerarray [3]."<br/>";
echo $miprimerarray [4]."<br/>";
echo $misegundoarray ["pote"]."<br/>";
echo $sumita."<br/>";

if ($miprimerarray[0] == $misegundoarray ["pote"])
{
    echo("esto es mentira, 'digo verdad'*");
}elseif($miprimerarray[0] == $misegundoarray ["pito"]){
    echo("esto es mentira, 'digo verdad'*");
}else{
    echo("esto es verdad, 'digo mentirA'*");
}

while($miprimerarray[1]<7){
    echo "puto"."<br/>";
    $miprimerarray[1]++;
}

do{
    echo "desputo"."<br/>";
    $miprimerarray[1]++;
}while($miprimerarray[1]<10);

for($i=0;$i<5;$i++){
    echo "puto de nuevo"."<br/>";
}


?>
