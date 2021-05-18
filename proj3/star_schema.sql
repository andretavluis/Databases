DROP INDEX if exists idx_incident;
DROP TABLE IF EXISTS f_incident;
DROP TABLE IF EXISTS d_reporter;
DROP TABLE IF EXISTS d_time;
DROP TABLE IF EXISTS d_location;
DROP TABLE IF EXISTS d_element;

create table d_time (
    id_time serial,
    day integer not null,
    week_day varchar(20) not null,
    week integer not null,
    month integer not null,
    trimester integer not null,
    year integer not null,
    primary key (id_time)
);

create table d_reporter (
    id_reporter serial,
    name varchar(80) not null,
    address varchar(80) not null,
    primary key (id_reporter)
);

create table d_location (
    id_location serial,
    latitude NUMERIC(9,6) not null,
    longitude NUMERIC(8,6) not null,
    locality VARCHAR(80) not null,
    primary key (id_location)
);

create table d_element (
    id_element serial,
    element_id varchar(10) not null,
    element_type varchar(50) not null,
    primary key (id_element)
);

create table f_incident (
    id_reporter integer,
    id_time integer,
    id_location integer,
    id_element integer,
    severity VARCHAR(30) not null,
    primary key (id_reporter, id_time, id_location, id_element),
    foreign key (id_reporter) references d_reporter(id_reporter),
    foreign key (id_time) references d_time(id_time),
    foreign key (id_location) references d_location(id_location),
    foreign key (id_element) references d_element(id_element)
);

create index idx_incident on f_incident (id_reporter, id_element, id_location, id_time);

