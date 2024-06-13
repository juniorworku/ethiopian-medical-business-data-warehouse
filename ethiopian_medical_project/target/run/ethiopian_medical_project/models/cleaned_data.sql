
  create view "postgres"."public"."cleaned_data__dbt_tmp"
    
    
  as (
    -- models/cleaned_data.sql

with chemed as (
    select 
        message_id::text,
        date,
        sender_id::text,
        message,
        media_path
    from raw.chemed
),
doctorset as (
    select 
        message_id::text,
        date,
        sender_id::text,
        message,
        NULL as media_path
    from raw.doctorset
),
eahci as (
    select 
        message_id::text,
        date,
        sender_id::text,
        message,
        NULL as media_path
    from raw.eahci
),
lobelia4cosmetics as (
    select 
        message_id::text,
        date,
        sender_id::text,
        message,
        media_path
    from raw.lobelia4cosmetics
),
yetenaweg as (
    select 
        message_id::text,
        date,
        sender_id::text,
        message,
        NULL as media_path
    from raw.yetenaweg
)

select * from chemed
union all
select * from doctorset
union all
select * from eahci
union all
select * from lobelia4cosmetics
union all
select * from yetenaweg
  );