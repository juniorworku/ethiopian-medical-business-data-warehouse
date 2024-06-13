select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      -- tests/no_future_dates.sql

with future_dates as (
    select *
    from "postgres"."public"."cleaned_data"
    where to_date(date, 'YYYY-MM-DD') > current_date
)

select count(*) as errors
from future_dates
      
    ) dbt_internal_test