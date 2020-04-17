<html>
<head>
    <title>Mi documento básico</title>
</head>
<body>

<?php
    $variable=array($_POST['planeta'],
    array($_POST['masaE'],$_POST['distancia']),
    array($_POST['tamaño'],$_POST['ei']),
    $_POST['campom'],
    $_POST['temp']);
    
    $prob=0;

    if ($variable[0][0]=="r"){
        $prob=$prob+35;
    }
    else{
        $prob=$prob-90;
    }

    $r1=$variable[1][0]-0.24;
    $r2=$r1+0.5;
    if ($variable[1][1]>$r1) {
        if($variable[1][1]<$r2){
            if ($variable[0][0]!="r"){
                $prob=$prob+10;
            }
        }
    }
    else{
        $prob=$prob-45;
    }

    if($variable[2][0]<0.027){
        $prob=$prob-75;
    }
    else{
        $prob=$prob+10;
    }

    if($variable[2][1]=="si"){
        $prob=$prob-25;
    }
    else{
        $prob=$prob+10;
    }

    if($variable[3][0]=="s"){
        $prob=$prob+20;
    }
    else{
        $prob=$prob-60;
    }

    if($variable[4][0]<-3){
        if($variable[4][0]>45){
            $prob=$prob-10;
        }
    }
    else{
        $prob=$prob+20;
    }

    if ($prob<0){
        $prob=0;
    }
    echo "probabilidad de albergar vida: ".$prob."<br/>";
?>
<form method="POST" action="preinforme11L_NombreApellido.php">
    <br/><br/><br/>
    <font size="3">Quiere volver a intentarlo?</font>
    <input type="submit" value="Si">

</body>
</html>