create database webdb ; 

use webdb ; 

create table job(
job_number int primary key identity (1 , 1 ) , 
company varchar(255)  , 
loction  varchar(255)  ,
since  varchar(30)  ,
jtype  varchar(30)  ,
)
