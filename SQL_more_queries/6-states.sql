-- Create the database hbtn_0d_usa and
-- the table states (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY (`id`),
    `id` INT UNIQUE AUTO_INCREMENT NOT NULL,
    `name` VARCHAR(256) NOT NULL
);
