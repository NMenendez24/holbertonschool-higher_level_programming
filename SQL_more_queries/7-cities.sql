-- Creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    state_id INT UNSIGNED NOT NULL,
    name VARCHAR(256),
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
)