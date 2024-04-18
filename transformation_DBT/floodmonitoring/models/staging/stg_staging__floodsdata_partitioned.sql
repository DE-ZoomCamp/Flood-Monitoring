with 

source as (

    select * from {{ source('staging', 'floodsdata_partitioned') }}

),

renamed as (

    select
        _id,
        description,
        eaareaname,
        floodareaid,
        istidal,
        severity,
        severitylevel,
        timemessagechanged,
        timeraised,
        timeseveritychanged,
        dateraised,
        DATE_DIFF(DATE(timeraised), DATE(timeseveritychanged), DAY) AS raised_change,
        DATE_DIFF(DATE(timemessagechanged), DATE(timeseveritychanged), DAY) AS severity_notify
    from source

)

select * from renamed

