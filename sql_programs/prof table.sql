create database if not exists MVGR ;
USE MVGR;
CREATE TABLE if not exists `Professor` (
`id` INT(11) NOT NULL AUTO_INCREMENT,
`First_name` VARCHAR(255) DEFAULT NULL,
`Last_name` VARCHAR(255),
`Age` int(4),NOT Null
`Sex` CHAR(4) NOT NULL,
`degree` char(20) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;