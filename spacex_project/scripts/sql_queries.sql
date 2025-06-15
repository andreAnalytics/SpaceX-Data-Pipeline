SELECT *
FROM launchestransform
where success = TRUE;

SELECT *
FROM launchestransform
where LAUNCH_DATE= (SELECT MAX(LAUNCH_DATE) from launchestransform);

SELECT rocket, COUNT(rocket) AS laucnhes_per_rocket
FROM launchestransform
GROUP BY 1;