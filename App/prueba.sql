-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


-- -----------------------------------------------------
-- Schema executes_db_argos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `executes_executes_db_argos` DEFAULT CHARACTER SET utf8mb4;
USE `executes_db_argos` ;

-- -----------------------------------------------------
-- Table `executes_db_argos`.`compania`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `executes_db_argos`.`compania` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO compania(nombre) VALUES('EmpresaA');
INSERT INTO compania(nombre) VALUES('EmpresaB');

-- -----------------------------------------------------
-- Table `executes_db_argos`.`modelo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `executes_db_argos`.`modelo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO modelo(descripcion) VALUES('Dell');
INSERT INTO modelo(descripcion) VALUES('Lenovo');

-- -----------------------------------------------------
-- Table `executes_db_argos`.`sede`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `executes_db_argos`.`sede` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO sede(nombre) VALUES('Santillana');
INSERT INTO sede(nombre) VALUES('Mayorca');

-- -----------------------------------------------------
-- Table `executes_db_argos`.`computador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `executes_db_argos`.`computador` (
   `id` INT NOT NULL AUTO_INCREMENT,
  `serial` VARCHAR(30) NOT NULL,
  `placa` VARCHAR(30) NOT NULL,
  `marca` VARCHAR(30) NOT NULL,
  `fecha_registro` DATE,
  `ticket` VARCHAR(255) NOT NULL,
  `modelo_id` INT NOT NULL,
  `compania_id` INT NOT NULL,
  `sede_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `computador_fk0`
    FOREIGN KEY (`modelo_id`)
    REFERENCES `executes_db_argos`.`modelo` (`id`),
  CONSTRAINT `computador_fk1`
    FOREIGN KEY (`compania_id`)
    REFERENCES `executes_db_argos`.`compania` (`id`),
  CONSTRAINT `computador_fk2`
    FOREIGN KEY (`sede_id`)
    REFERENCES `executes_db_argos`.`sede` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `executes_db_argos`.`rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `executes_db_argos`.`rol` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO rol(descripcion) VALUES('Admin');
INSERT INTO rol(descripcion) VALUES('User');

-- -----------------------------------------------------
-- Table `executes_db_argos`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `executes_db_argos`.`usuario` (
  `dni` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(20) NOT NULL,
  `apellidos` VARCHAR(40) NOT NULL,
  `correo` VARCHAR(40) NOT NULL,
  `contrasena` VARCHAR(40) NOT NULL,
  `fecha_nacimiento` DATE NULL,
  `sexo` ENUM('F', 'M') NULL,
  `estado` VARCHAR(2) NULL DEFAULT '1',
  `foto` LONGBLOB NULL,
  `sede_id` INT NOT NULL,
  PRIMARY KEY (`dni`),
  CONSTRAINT `fk_usuario_sede1`
    FOREIGN KEY (`sede_id`)
    REFERENCES `executes_db_argos`.`sede` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO usuario(dni, nombre, apellidos, correo, contrasena, fecha_nacimiento, sexo, estado, sede_id) 
VALUES(123456789, 'Bailon', 'Paucar Montes', 'paucarmontesbailon@gmail.com', 'admin123456', '2020-10-02', 'M', 1, 4);

-- -----------------------------------------------------
-- Table `executes_db_argos`.`transferencia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `executes_db_argos`.`transferencia` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `sede_inicial` INT NOT NULL,
  `fecha_envio` DATETIME NULL,
  `sede_final` INT NOT NULL,
  `computador_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_transferencia_computador1`
    FOREIGN KEY (`computador_id`)
    REFERENCES `executes_db_argos`.`computador` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_transferencia_sede1`
    FOREIGN KEY (`sede_inicial`)
    REFERENCES `executes_db_argos`.`sede` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_transferencia_sede2`
    FOREIGN KEY (`sede_final`)
    REFERENCES `executes_db_argos`.`sede` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `executes_db_argos`.`usuario_rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `executes_db_argos`.`usuario_rol` (
  `usuario_dni` INT NOT NULL,
  `rol_id` INT NOT NULL,
  PRIMARY KEY (`usuario_dni`, `rol_id`),
  CONSTRAINT `fk_usuario_has_rol_usuario1`
    FOREIGN KEY (`usuario_dni`)
    REFERENCES `executes_db_argos`.`usuario` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuario_has_rol_rol1`
    FOREIGN KEY (`rol_id`)
    REFERENCES `executes_db_argos`.`rol` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO usuario_rol(usuario_dni, rol_id)VALUES('123456789', 3);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


