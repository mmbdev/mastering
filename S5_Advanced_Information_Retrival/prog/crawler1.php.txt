<?php
// Web-Crawler - Rolf Assfalg 2012

class Crawler {

  protected $markup = '';
  public $base = '';

  public function __construct($uri) {
    $this->base = $uri;
    $this->markup = $this->getMarkup($uri);

  }

  public function getMarkup($uri) {
    return file_get_contents($uri);
  }

  public function get($type) {
    $method = "_get_{$type}";
    if (method_exists($this, $method)){
      return call_user_method($method, $this);
    }
  }

  protected function _get_images() {
    if (!empty($this->markup)){
      preg_match_all('/<img([^>]+)\/>/i', $this->markup, $images);
      return !empty($images[1]) ? $images[1] : FALSE;
    }
  }

  protected function _get_links() {
    if (!empty($this->markup)){
      //preg_match_all('/<a([^>]+)\>(.*?)\<\/a\>/i', $this->markup, $links);
      preg_match_all('/href=\"(.*?)\"/i', $this->markup, $links);
      return !empty($links[1]) ? $links[1] : FALSE;
    }
  }
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
<html>
  <head>
    <title>Web Crawler</title>
  </head>
  <body>
    <h2>
      Webcrawler auf 
    </h2><?php
      $con = mysql_connect("localhost:3306", "root","");
      mysql_select_db("crawler", $con);
      $queryTemp = mysql_query("DELETE FROM tbl_link", $con);

     $site = 'http://www.dhbw-heidenheim.de/index.php';
     crawlSite($site, $con);

      mysql_close();
    ?><?php

    function crawlSite($uri, $con)
    {
     $crawl = new Crawler($uri);
     $links = $crawl->get('links');
     
      mysql_select_db("crawler", $con);
      
      $pos = strrpos($uri, "/");
      $uriBase = substr($uri, 0, $pos);
      //echo "<font color=\"red\">$uriBase</font><br>";
      
     foreach($links as $l)
     {
      $len = strlen($l);
      if (substr($l, 0, 4) != "http" && (substr($l, $len - 3, 3) == "php" || substr($l, $len - 4, 4) == "html" ))
      {  
       if (substr($l, 0, 1) == '/')
         $l = $uriBase.$l;
       else if (substr($l, 0, 4) == 'http')
           $l = $l;
       else
           $l = $uriBase. '/' . $l;
      
       $query2 = mysql_query("SELECT link FROM tbl_link WHERE link='$l'", $con);
       if (mysql_num_rows($query2) == 0) // Link ist neu
       { 
        echo $uri. " - " . $l ."<br>\n";
        $query = mysql_query("INSERT INTO tbl_link(link) VALUES ('$l')", $con);
        crawlSite($l, $con);
       } else {echo '.';} //Link schon mal da gewesen...      
      }
     }
		}
    ?>
  </body>
</html>
