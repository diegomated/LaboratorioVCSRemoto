<?php
    $libros=array(array("Mi isla","La magia de ser sofia","Fuimos canciones","valeria en el espejo","un recuerdo perfecto"),
    array("El año del diluvio","Una comedia ligera","Sin noticias de Gurb","La ciudad de los prodigios","El rey recibe"),
    array("Cien años de soledad","La hojarasca","El otoño del patriarca","Vivir para contarla","La mala hora"),
    array("Ficciones","Labyrinths","El libro de la arena","El hacedor","La biblioteca de babel"),
    array("Tiempo de amar","Starship Troopers","Puerto del verano","Amos de titeres","Viernes")
    );
    $autor=array("Elisabet Benavent","Eduardo Mendoza","Gabriel Garcia Marquez","Jorge Luis Borges","Robert A. Heinlein");
    echo "autor: ".$autor[$_POST['autor']-1]."<br/>";
    $cont=1;
    for($i=0;$i<5;$i++){
        echo "Libro ".$cont.": ".$libros[$_POST['autor']-1][$i]."<br/>";
        $cont=$cont+1;
    }
?>