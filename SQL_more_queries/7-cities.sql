-- Creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id),
    state_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
    name VARCHAR(256)
)