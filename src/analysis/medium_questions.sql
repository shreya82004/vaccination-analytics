-- 1. Join: coverage + reported_cases for a disease (e.g., Measles)
WITH latest AS (SELECT MAX(year) AS y FROM coverage)
SELECT
  c.code,
  c.name,
  c.year,
  c.coverage AS measles_coverage,
  r.cases AS measles_cases
FROM coverage c
LEFT JOIN reported_cases r
  ON c.code = r.code
 AND c.year = r.year
 AND r.disease = 'Measles'
WHERE c.antigen = 'MCV1'
  AND c.year = (SELECT y FROM latest)
ORDER BY measles_cases DESC NULLS LAST;

-- 2. Region-wise average DTP3 coverage (latest year)
WITH latest AS (SELECT MAX(year) AS y FROM coverage)
SELECT
  v.region,
  ROUND(AVG(c.coverage)::numeric, 2) AS avg_dtp3_coverage,
  COUNT(DISTINCT c.code) AS num_countries
FROM coverage c
JOIN vaccine_introduction v
  ON c.code = v.code
WHERE c.antigen = 'DTPCV3'
  AND c.year = (SELECT y FROM latest)
GROUP BY v.region
ORDER BY avg_dtp3_coverage DESC;

-- 3. Top 10 countries with lowest MCV1 coverage (latest year)
WITH latest AS (SELECT MAX(year) AS y FROM coverage)
SELECT
  code,
  name,
  coverage
FROM coverage
WHERE antigen = 'MCV1'
  AND year = (SELECT y FROM latest)
  AND coverage IS NOT NULL
ORDER BY coverage ASC
LIMIT 10;

-- 4. Vaccine introduction timeline for HPV
SELECT
  country,
  region,
  year,
  description,
  introduced
FROM vaccine_introduction
WHERE description ILIKE '%HPV%'
ORDER BY year, country;

-- 5. Number of doses scheduled for DTP-like vaccines
SELECT
  code,
  country,
  vaccine_code,
  COUNT(*) AS num_doses
FROM vaccine_schedule
WHERE vaccine_code ILIKE 'DTP%' 
   OR vaccine_description ILIKE '%diphtheria%'
GROUP BY code, country, vaccine_code
ORDER BY num_doses DESC
LIMIT 20;
