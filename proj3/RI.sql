--(IC1) For every transformer, pv must correspond to the voltage of the busbar identified by pbbid
--(IC2) For every transformer, sv must correspond to the voltage of the busbar identified by sbbid .
drop function checkId() cascade;

create or replace function checkId()
returns trigger
as $$
    begin
        if new.pv != (select voltage
                      from busbar
                      where id = new.pbbid) then
            raise exception 'Primary voltage must correspond to the voltage of the primary bus bar';
        elsif new.sv != (select voltage
                        from busbar
                        where id = new.sbbid) then
            raise exception 'Secondary voltage must correspond to the voltage of the secondary bus bar';
        end if;
        return new;
    end
$$ language plpgsql;

create trigger checkId_trigger
before insert or update on transformer
for each row execute procedure checkId();

--(IC5) For every analysis concerning a transformer, the name, address values cannot coincide with
-- sname, saddress values of the substation where the transformer is located (i.e., gpslat and gpslong
-- have the same values in transformer and substation).

drop function check_name_address() cascade;

create or replace function check_name_address()
returns trigger as
$$
    begin
        if (select name
            from analyses
            where id = new.id and
                  instant = new.instant)
            =
            (select s.sname
            from substation s join transformer t on s.gpslat = t.gpslat and s.gpslong = t.gpslong
            where t.id = new.id)
            or
            (select address
            from analyses
            where id = new.id and
                  instant = new.instant)
            =
            (select s.saddress
            from substation s join transformer t on s.gpslat = t.gpslat and s.gpslong = t.gpslong
            where id = new.id)
            then
            raise exception 'Person cannot analyse incidents regarding substations they supervise';
        end if;
        return new;
    end;
$$ language plpgsql;


create trigger check_name_address_trigger
before insert or update on analyses
for each row execute procedure check_name_address();

