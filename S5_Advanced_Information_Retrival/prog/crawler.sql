CREATE DATABASE `crawler` ;

use crawler;

CREATE TABLE IF NOT EXISTS `tbl_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link` varchar(1024) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=1 ;
