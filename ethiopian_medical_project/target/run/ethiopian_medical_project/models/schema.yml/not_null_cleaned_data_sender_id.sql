select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select sender_id
from "postgres"."public"."cleaned_data"
where sender_id is null



      
    ) dbt_internal_test