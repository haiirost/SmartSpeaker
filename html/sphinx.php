<?php
    echo "<p>Sphinx.php start...";

    //exec("rec -r 16k -e signed-integer -b 16 -c 1 ps_file.raw </dev/null >/dev/null 2>&1 &");

    $path = getcwd();
    chdir('/var/www/sphinx/');
    exec("rec -r 16k -e signed-integer -b 16 -c 1 /tmp/ps_file.raw </dev/null >/dev/null 2>&1 &");
    echo "<p>Rec!";
    sleep(2);
    exec("pkill rec");
    echo "<p>Stop rec.";
    
    $out = exec("./ps_file");

    chdir($path);
    echo "<p>";
    echo $out;
    
?>
