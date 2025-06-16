SELECT *
FROM launchestransform
where success = TRUE;

SELECT *
FROM launchestransform
where LAUNCH_DATE= (SELECT MAX(LAUNCH_DATE) from launchestransform);

SELECT rocket, COUNT(rocket) AS laucnhes_per_rocket
FROM launchestransform
GROUP BY 1;

SELECT
    rocket,
    AVG (
        CASE WHEN success = TRUE THEN 1
        ELSE 0
        END
    ) AS success_rate
FROM dbt_spacex.launchestransform
GROUP BY rocket;

SELECT
    YEAR(launch_date) AS launch_year,
    COUNT(*) AS launches_per_year
FROM dbt_spacex.launchestransform
GROUP BY 1;