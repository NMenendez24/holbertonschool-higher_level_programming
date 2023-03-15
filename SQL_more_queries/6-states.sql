-- Creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(256),
    PRIMARY KEY (id)
)