create database perfumaria;
use perfumaria;

create table usuario(
	id_usuario serial primary key,
	nome_usuario varchar(200) not null unique,
	email varchar(200) not null unique,
	palavra_passe varchar(200) not null,
	data_criaccao date not null
);

create table produto (
	id_produto serial primary key,
	nome_produto varchar(200) not null,
	preco numeric not null unique,
	imagem_client varchar(250),
	data_cadastro date not null
);

create table newsletter(
	id_newsletter serial primary key,
	nome varchar(200) not null,
	email varchar(200) not null unique
);

create table testemunho(
	id_testemunho serial primary key,
	descricao text not null,
	nome_cliente varchar(200) not null,
	imagem_cliente varchar(250)
);


