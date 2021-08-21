<?php
function makesession($username, $seed){
        $max = strlen($username) - 1;
        #$seed = rand(0, $max);
        $key = "s4lTy_stR1nG_".$username[$seed]."(!528./9890";
        $session_cookie = $username.md5($key);

        return $session_cookie;
    }

echo makesession("paul",0);
echo "\n";
echo makesession("paul",1);
echo "\n";
echo makesession("paul",2);
echo "\n";
echo makesession("paul",3);
echo "\n";
?>

<!--
  "$seed" is a random number between 0 and the length of the username - 1.
  "$key" is hardcoded according to the "$seed" value.
  cookie = "$username" + md5-hash($key)
     P A U L
     0 1 2 3
-->
