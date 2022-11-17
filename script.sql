-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema proyecto_pañalera
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyecto_pañalera
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proyecto_pañalera` DEFAULT CHARACTER SET utf8 ;
USE `proyecto_pañalera` ;

-- -----------------------------------------------------
-- Table `proyecto_pañalera`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_pañalera`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(300) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_pañalera`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_pañalera`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `imagen` VARCHAR(250) NULL,
  `descripcion` TEXT NULL,
  `precio` INT NULL,
  `inventario` INT NULL,
  `categoria` VARCHAR(250) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_pañalera`.`pedidos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_pañalera`.`pedidos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `fecha` DATE NULL,
  `direccion` VARCHAR(500) NULL,
  `subtotal` INT NULL,
  `iva` INT NULL,
  `total` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pedidos_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_pedidos_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `proyecto_pañalera`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_pañalera`.`productos_del_pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_pañalera`.`productos_del_pedido` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pedido_id` INT NOT NULL,
  `producto_id` INT NOT NULL,
  `cantidad` INT NULL,
  `subtotal` INT NULL,
  `iva` INT NULL,
  `total` INT NULL,
  PRIMARY KEY (`id`, `pedido_id`, `producto_id`),
  INDEX `fk_pedidos_has_productos_productos1_idx` (`producto_id` ASC) VISIBLE,
  INDEX `fk_pedidos_has_productos_pedidos_idx` (`pedido_id` ASC) VISIBLE,
  CONSTRAINT `fk_pedidos_has_productos_pedidos`
    FOREIGN KEY (`pedido_id`)
    REFERENCES `proyecto_pañalera`.`pedidos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pedidos_has_productos_productos1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `proyecto_pañalera`.`productos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
