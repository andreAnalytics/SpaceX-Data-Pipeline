select
    id,
    name,
    date(to_timestamp(date_utc)) as launch_date,
    success,
    rocket
FROM {{ source('public','launches') }}