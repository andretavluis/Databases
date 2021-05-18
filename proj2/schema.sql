drop table if exists person cascade;
drop table if exists supervisor cascade;
drop table if exists analyst cascade;
drop table if exists analyses cascade;
drop table if exists incident cascade;
drop table if exists line_incident cascade;
drop table if exists element cascade;
drop table if exists line cascade;
drop table if exists bus_bar cascade;
drop table if exists transformer cascade;
drop table if exists line_connection cascade;
drop table if exists substation cascade;

----------------------------------------
-- Table Creation
----------------------------------------
create table person(
	name varchar(80),
	address varchar(255),
	phone integer,
	tax_id integer,
	primary key(name,address),
	unique (phone),
	unique (tax_id)
);
--Constraint: (Mandatory) Every person must exist in table 'supervisor' or 'analyst'

create table supervisor(
	name varchar(80),
	address varchar(255),
	primary key(name,address),
	foreign key(name,address) references person(name,address)
);

create table analyst(
	name varchar(80),
	address varchar(255),
	primary key(name,address),
	foreign key(name,address) references person(name,address)
);

create table element(
    id varchar(80),
    primary key (id)
);
-- Constraint: (Mandatory) Every element must exist either in table 'line', 'bus_bar' or 'transformer'
-- Constraint: (Disjoint) No element can exist at the same time in both the table 'line', 'bus_bar' or 'transformer'

create table incident( -- weak entity
   description varchar(255) not null,
   instant timestamp,
   id varchar(80),
   severity varchar(80) not null,
   primary key (instant, id),
   foreign key (id) references element(id)
   --  (Disjoint) an Incident can only either be a regular incident or a line incident, not both
);

create table analyses(
    name varchar(80),
    address varchar(255),
    report text not null,
    instant timestamp,
    id varchar(80),
    primary key (instant, id),
    foreign key(name,address) references person(name,address),
    foreign key (instant,id) references incident(instant,id)
    -- (IC-5) Persons cannot /analyse/ incidents regarding Elements of a Substation they /supervise/
);

create table line_incident(
   instant timestamp,
   id varchar(80),
   point numeric(5,2) not null,
   primary key (instant,id),
   foreign key (instant,id) references incident(instant,id)
);

create table line(
    id varchar(80),
    impedance integer not null,
    primary key (id),
    foreign key (id) references element(id)
);
--Constraint: (Mandatory) Every line must exist in the table 'line_connection'

create table bus_bar (
    id varchar(80),
    voltage integer not null,
    primary key (id),
    foreign key (id) references element(id)
);

create table substation(
	lat numeric(9,6),
    long numeric(8,6),
	locality_name varchar(80) not null,
	name varchar(80) not null,
	address varchar(255) not null,
	primary key(lat, long),
	foreign key(name,address) references supervisor(name,address)
);
--Constraint: (Mandatory) Every substation must exist in the table 'transformer'
-- (IC-5) Persons cannot /analyse/ incidents regarding Elements of a Substation they /supervise/

create table transformer(
    id varchar(80),
    primary_voltage integer not null ,
    secondary_voltage integer not null ,
    primary_id varchar(80),
    secondary_id varchar(80),
    lat numeric(9,6),
    long numeric(8,6),
    primary key (id),
    foreign key (id) references element(id),
    foreign key (primary_id) references bus_bar(id),
    foreign key (secondary_id) references bus_bar(id),
    foreign key (lat, long) references substation (lat,long),
    check ( primary_id != secondary_id )
);
-- (IC-1) Constraint: Necessary to check ( primary_voltage = (select voltage
--                                                            from bus_bar bb
--                                                            where bb.id = primary_id ) )
-- (IC-2) Constraint: Necessary to check ( secondary_voltage = (select voltage
--                                                              from bus_bar bb
--                                                              where bb.id = secondary_id ) )

create table line_connection (
    id varchar(80),
    first_id varchar(80),
    second_id varchar(80),
    primary key (id, first_id, second_id),
    foreign key (id) references line(id),
    foreign key (first_id) references bus_bar(id),
    foreign key (second_id) references bus_bar(id),
    check ( first_id != second_id )
);
