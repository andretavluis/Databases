--A. List the names of all analysts that analysed element with id 'B-789'

select distinct name, address
from analyses
where id = 'B-789';

--B. What is the name of the analyst that has reported more incidents

select name, address, count(*) as ReportedIncidents
from analyses
group by name, address
having count(*) >= all (select count(*)
                        from analyses
                        group by name, address);

--C. List all substations with more than one transformer

select lat, long, count(*) as NumTransformers
from transformer
group by (lat, long)
having count(*) >1;

--D. Find the names of the localities that have more substations than every other locality

select locality_name, count(*) as NumSubstations
from substation
group by locality_name
having count(*) >= all (select count(*)
                       from substation
                       group by locality_name);
