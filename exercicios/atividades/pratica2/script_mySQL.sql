create database bdcotacoes;

use bdcotacoes;

create table moedas(
data date, 
dolar float, 
euro float);

INSERT INTO moedas (data, dolar, euro) VALUES (17/09/2021, 5.2928, 6.2021);

select * from moedas;

drop table moedas;