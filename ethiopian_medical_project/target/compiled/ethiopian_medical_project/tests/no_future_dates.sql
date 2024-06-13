-- tests/no_future_dates.sql

with future_dates as (
    select *
    from "postgres"."public"."cleaned_data"
    where to_date(date, 'YYYY-MM-DD') > current_date
)

select count(*) as errors
from future_dates