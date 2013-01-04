CREATE DATABASE if not exists ase;
CREATE USER 'ase'@'localhost' IDENTIFIED BY 'asep4s5';
GRANT ALL PRIVILEGES ON ase.* TO 'ase'@'localhost';
FLUSH PRIVILEGES;

