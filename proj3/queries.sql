--3. VIEW
--Create a view to get the supervisors and the number of substations that each one of them supervises,
--without including supervisors that do not supervise any substation.
drop view supervisor_substation;

create view supervisor_substation
as
select sname, saddress, count(*) as num_supervised_substations
from substation
group by sname, saddress;

--select * from supervisor_substation;

--4. QUERIES
--1. Who are the analysts that have analyzed every incident of element ‘B-789’?
select name, address, count(*) as num_incidents
from analyses
where id = 'B-789'
group by name, address
having count(*) = (select count(*)
                   from analyses
                   where id = 'B-789');

--2. Who are the supervisors that do not supervise substations south of Rio Maior (Portugal) (Rio Maior coordinates: 39.336775, -8.936379 (cf. Google Maps)?
(select name, address
from supervisor)
except
(select sname, saddress
from substation
where gpslat < 39.336775);

--3. What are the elements with the smallest amount of incidents?
select a.id, count(*)-1 as num_incidents
from ((select id from element) union all (select id from incident)) as a
group by a.id
having count(*) <= all (select count(*)
                        from ((select id from element) union all (select id from incident)) as b
                        group by b.id);

--4. How many substations does each supervisor supervise? (include supervisors that do not supervise any at the moment)
--without using the created view
select a.name, a.address, count(*)-1 as num_substations
from ((select name, address from supervisor) union all (select sname, saddress from substation)) as a
group by a.name, a.address;

--using the created view
select name, address, coalesce(num_supervised_substations, 0) as num_substations
from supervisor a left outer join supervisor_substation b
        on a.name = b.sname and a.address = b.saddress;



