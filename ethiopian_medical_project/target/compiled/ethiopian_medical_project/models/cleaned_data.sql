-- models/cleaned_data.sql

with chemed as (
    select * from raw.chemed
),
doctorset as (
    select * from raw.doctorset
),
eahci as (
    select * from raw.eahci
),
lobelia4cosmetics as (
    select * from raw.lobelia4cosmetics
),
yetenaweg as (
    select * from raw.yetenaweg
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