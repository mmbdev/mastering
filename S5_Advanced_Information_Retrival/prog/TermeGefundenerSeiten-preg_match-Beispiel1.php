<?php
 $con = mysql_connect("localhost:3306", "root","");
mysql_select_db("crawler", $con);
    
      $result_id = mysql_query("SELECT * FROM tbl_link");  
    
            $num = mysql_numrows($result_id);
   
            for($i1 = 0; $i1 < $num; $i1++) {
                            $row = mysql_fetch_array($result_id);
                $link = $row["link"];
                                $id = $row["id"];
                //Links
                echo "link: $link - id: $id";
                echo "<hr>";
                $handle = fopen($link,"r");
                if($handle){
                    while (($zeile = fgets($handle)) != false){
                        $pureTxt = strip_tags($zeile);
                        //echo $pureTxt;
                        preg_match_all('/[a-zA-Z0-9][a-zA-Z0-9\-\_]*[a-zA-Z0-9]/i', $pureTxt, $terms);
                        foreach ($terms[0] as $wort){
                        echo $wort;
                        echo "<br>";
                        }
                    }
                }
                fclose($handle);
       }       
?>