create database if not exists MVGR ;
USE MVGR;
CREATE TABLE if not exists `Department` (
`id` INT(11) NOT NULL AUTO_INCREMENT,
`Department_name` VARCHAR(255) DEFAULT NULL,
`Description` VARCHAR(255),
`Code` VARCHAR(6) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;