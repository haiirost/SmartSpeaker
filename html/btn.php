<?php
    if (isset($_POST['startRadioRock'])){ 
        echo "Радио запущено"; 
        exec("mplayer -slave -quiet http://online-radioroks2.tavrmedia.ua/RadioROKS_NewRock </dev/null >/dev/null 2>&1 &");
    }
    
    if (isset($_POST['startRadioLink'])){
        echo "Радио запущено по ссылке";
        exec("mplayer -slave -quiet " . $_POST['radioLink'] . " </dev/null >/dev/null 2>&1 &");
    }
    if (isset($_POST['stopRadio'])){
        // делаете что угодно
        echo "Процесс радио убит";
        exec("pkill mplayer");
    }
    
?>
