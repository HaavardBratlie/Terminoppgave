-- Create the database
CREATE DATABASE IF NOT EXISTS HBdesigns;

-- Select the database
USE HBdesigns;

-- Create the 'bruker' table (users table)
CREATE TABLE IF NOT EXISTS bruker (
    id INT AUTO_INCREMENT PRIMARY KEY,
    E_post VARCHAR(255) NOT NULL UNIQUE,
    passord VARCHAR(255) NOT NULL
);
