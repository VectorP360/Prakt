-- Если оставить name для всех таблиц, то читаемость хуже не станет.
-- Случай с первичным ключом (workshop_id) иной: он используется в составных запросах, 
-- поэтому конкретизировать в названии надло
CREATE TABLE workshop(
    workshop_id SERIAL PRIMARY KEY,
    name VARCHAR(128)
);

-- Меня за это ругал в одно время старший коллега.
-- Это на мой взгляд вкусовщина moment, поэтому для тебя просто на заметку.
-- Сокращение id (которое образовалось от слова identificator) в некотором смысле стало самостоятельным словом,
-- которое в названиях переменных пишется с учетом регистра как полноценное слово.
-- То есть, вместо facility_type_ID пишем facility_type_id 
CREATE TABLE facility_type(
    facility_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(128)
);

-- Если ограничиться 30 символами для поля name, то все, что длинее 30 символов, будет сокращено
-- Почитай пример в официальной документации postgresql: https://www.postgresql.org/docs/current/datatype-character.html
-- Поэтому вместо varchar(30) я указал тут varchar(128). 
-- С расчетом на то, что не будет должностей, в чьем названии будет больше 128 символов.
-- Пробелы, которые идут после символов, сокращаются до одного и тоже считаются символом. 
-- Например "word     " (9 символов) --> "word " (5 символов)

CREATE TABLE post(
    post_id SERIAL PRIMARY KEY,
    name VARCHAR(128)
);

-- Способов называть первичный ключ таблицы много. Можно просто писать id, можно ID. 
-- Можно так, как мы у себя на работе делаем: название_таблицы_id.


-- Я всюду стираю запросы на DROP и IF EXISTS из соображений, что данный скрипт файл расскажет мне, 
-- как база данных устроена в момент его инициализации (грубо говоря, в момент рождения)
CREATE TABLE facility(
    facility_id SERIAL PRIMARY KEY,
    name VARCHAR(128),

    type_id INTEGER,
    workshop_id INTEGER,

    FOREIGN KEY (type_id) REFERENCES facility_type (facility_type_id),
    FOREIGN KEY (workshop_id) REFERENCES workshop (workshop_id)
);


CREATE TABLE scada_scheme(
    scada_scheme_id SERIAL PRIMARY KEY,
    name VARCHAR(128),
    content text, -- пусть тут будет лежать прям текст SVG разметки схемы из того самого задания со звездочкой.

    -- И будет лучше наоборот указать внешний ключ для схемы на установку. 
    -- Потому что схема описывает установку (ссылается на нее). 
    -- Схема является дополнительной информацией для установки. Как с facilty_types. 

    -- В твоем прошлом варианте, когда таблица facility ссылается на scada_scheme, получается, 
    -- что установка описывает SCADA-схему, 
    -- а значит установка является дополнительной инфорацией для SCADA-схемы.
    facility_id INTEGER NOT NULL,
    FOREIGN KEY (facility_id) REFERENCES facility (facility_id)
);
-- Тут при указании внешнего ключа дублируешь название первичного ключа той таблицы, 
-- на которую тебе нужно сослаться.

-- Записи можно разграничить. В самом низу пишутся поля, которые будут внешними ключами

CREATE TABLE user(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(128),
    surname VARCHAR(128),
    fathersname VARCHAR(128),
    hire_date DATE,
    login VARCHAR(128),
    password VARCHAR(128),

    facility_id INTEGER,
    post_id INTEGER,

    FOREIGN KEY (facility_id) REFERENCES facility_id (facility_ID),
    FOREIGN KEY (post_id) REFERENCES posts (post_id)
);