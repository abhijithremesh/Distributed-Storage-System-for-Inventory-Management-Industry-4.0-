
CREATE DATABASE `inventorylog`;

CREATE TABLE `inventorylog`. `datalog` (
  `time` varchar(45) NOT NULL,
  `scale_id` varchar(45) NOT NULL,
  `article_number` int(11) NOT NULL,
  `unit_weight` float NOT NULL,
  `obtained_weight` float DEFAULT NULL,
  `count` int(11) DEFAULT NULL
) ;

