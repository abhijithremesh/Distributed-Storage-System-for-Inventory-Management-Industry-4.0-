CREATE TABLE `distributedstorage`.`inventorydb` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `article_number` INT NOT NULL,
  `article_name` VARCHAR(45) NOT NULL,
  `unit_weight` FLOAT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `article_number_UNIQUE` (`article_number` ASC) VISIBLE,
  UNIQUE INDEX `article_name_UNIQUE` (`article_name` ASC) VISIBLE);

INSERT INTO `distributedstorage`.`inventorydb` (`id`,`article_number`,`article_name`,`unit_weight`) 
VALUES ('1','731308','wascheklammer', 4);
INSERT INTO `distributedstorage`.`inventorydb` (`id`,`article_number`,`article_name`,`unit_weight`) 
VALUES ('2','708763','tintenpatrone', 1.4);
INSERT INTO `distributedstorage`.`inventorydb` (`id`,`article_number`,`article_name`,`unit_weight`) 
VALUES ('3','700555','screw', 3);
