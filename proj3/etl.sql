--d_time
CREATE OR REPLACE FUNCTION load_date_dim()
    RETURNS VOID AS
$$
DECLARE instant_value TIMESTAMP;
DECLARE count INTEGER;
BEGIN
    instant_value := '2020-01-01 00:00:00';
    count:= 1;
    WHILE instant_value < '2022-01-01 00:00:00' LOOP
        INSERT INTO d_time(
                           day,
                           week_day,
                           week,
                           month,
                           trimester,
                           year
        ) VALUES (
                  CAST(EXTRACT(DAY FROM instant_value) AS INTEGER),
                  CASE WHEN count =1 THEN 'Wednesday'
                       WHEN count =2 THEN 'Thursday'
                       WHEN count =3 THEN 'Friday'
                       WHEN count =4 THEN 'Saturday'
                       WHEN count =5 THEN 'Sunday'
                       WHEN count =6 THEN 'Monday'
                       ELSE 'Tuesday'
                  END,
                  CAST(EXTRACT(WEEK FROM instant_value) AS INTEGER),
                  CAST(EXTRACT(MONTH FROM instant_value) AS INTEGER),
                  CASE WHEN EXTRACT(MONTH FROM instant_value) <= 3 THEN 1
                       WHEN EXTRACT(MONTH FROM instant_value) > 3 AND EXTRACT(MONTH FROM instant_value)<=6 THEN 2
                       WHEN EXTRACT(MONTH FROM instant_value) > 6 AND EXTRACT(MONTH FROM instant_value)<=9 THEN 3
                       ELSE 4
                  END,
                  EXTRACT(YEAR FROM instant_value)
        );
        count := count + 1;
        IF count = 8 then count := 1; END IF;
        instant_value := instant_value + INTERVAL '1 DAY';
    END LOOP;
END;
$$ LANGUAGE plpgsql;

select load_date_dim();
--select * from d_time;

--d_reporter
insert into d_reporter(name, address)
select distinct a.name, a.address
from analyses a join incident i on a.instant = i.instant and a.id = i.id;

--select * from d_reporter;

--d_location
insert into d_location(latitude, longitude, locality)
select gpslat, gpslong, locality
from substation;

insert into d_location values (21, 0, 0, 'unknow');

--select * from d_location;

--d_element
insert into d_element(element_id, element_type)
select distinct id, description
from incident;

--select * from d_element;

--f_incident
insert into f_incident
select dr.id_reporter, dt.id_time, dl.id_location, de.id_element, severity
from (select  i.instant, i.id, coalesce(gpslong,0) as gpslong, coalesce(gpslat,0) gpslat, name, address, severity, description
      from incident i join analyses a on i.instant = a.instant and i.id = a.id
                      left outer join transformer s on a.id = s.id or a.id = pbbid or a.id = sbbid ) T
    left outer join d_location dl
        on T.gpslat = dl.latitude and T.gpslong = dl.longitude
    left outer join d_reporter dr
        on T.name = dr.name and T.address = dr.address
    left outer join d_element de
        on T.id = de.element_id and T.description = de.element_type
    left outer join d_time dt
        on extract(year from T.instant) = dt.year
            and extract(month from T.instant) = dt.month
            and extract(week from T.instant) = dt.week
            and extract(day from T.instant)= dt.day;




--select * from f_incident;

--SELECT * FROM d_time;
--select * from d_location;
--select * from d_reporter;
--select * from d_element;