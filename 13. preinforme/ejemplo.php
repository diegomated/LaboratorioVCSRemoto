<?php
    $diccionario=array("Diego" => 17, "Pacho" => 34, "Fernando" => 28, "Karen" => 17, "Elver" => 45);
    
    foreach($diccionario as $nombres => $edad){
        echo $nombres." tiene ".$edad." años "."<br/>";
    }
    
?>