CREATE DATABASE EdyodaLMS;

USE EdyodaLMS;

CREATE TABLE users(
fullname VARCHAR(80),
mobile VARCHAR(10) UNIQUE,
email VARCHAR(30) UNIQUE,
username VARCHAR(30) UNIQUE,
password VARCHAR(50),
moduleid VARCHAR(20));

CREATE TABLE Modules(
moduleid int unique,
modulename varchar(30),
start_date DATE,
end_date DATE,
units INT,
status varchar(20),
primary key(moduleid)); 

CREATE TABLE units(
unitid int UNIQUE,
unitname VARCHAR(80),
unittype VARCHAR(80),
modulename VARCHAR(30),
unitstart_date DATE,
unitend_date DATE);
