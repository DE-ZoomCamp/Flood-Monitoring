with 

source as (

    select * from {{ source('staging', 'floodsdata') }}

),

renamed as (

    select
        int64_field_0,
        _id,
        description,
        eaareaname,
        floodarea,
        floodareaid,
        istidal,
        severity,
        severitylevel,
        timemessagechanged,
        timeraised,
        timeseveritychanged,
        dateraised,
        DATE_DIFF(DATE(timeraised), DATE(timemessagechanged), DAY) AS raised_change,
        DATE_DIFF(DATE(timeseveritychanged), DATE(timemessagechanged), DAY) AS severity_notify
FROM



    from source

)

select * from renamed

