CREATE DATABASE expense_db ;
use expense_db;
CREATE TABLE users (
user_id int primary key auto_increment,
name varchar(50)
);


CREATE TABLE expenses (
exp_id int primary key auto_increment,
user_id int,
amount float,
category varchar(50),
description varchar(100),
date date,
foreign key (user_id) references users(user_id)
);
select * from users;

select * from expenses;
