--analyze the total number of anomalies reported by severity , locality and week_day

select severity, locality, week_day, count(*)
from f_incident join d_location on f_incident.id_location = d_location.id_location
                join d_time dt on f_incident.id_time = dt.id_time
group by cube (locality,week_day,severity);

