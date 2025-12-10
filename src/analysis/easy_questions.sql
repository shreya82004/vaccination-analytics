-- 1. Row count per table
SELECT 'coverage' AS table, COUNT(*) AS rows FROM coverage
UNION ALL
SELECT 'incidence', COUNT(*) FROM incidence
UNION ALL
SELECT 'reported_cases', COUNT(*) FROM reported_cases
UNION ALL
SELECT 'vaccine_introduction', COUNT(*) FROM vaccine_introduction
UNION ALL
SELECT 'vaccine_schedule', COUNT(*) FROM vaccine_schedule;

-- 2. Distinct countries in coverage table
SELECT COUNT(DISTINCT code) AS num_countries
FROM coverage;

-- 3. Year range available in data
SELECT MIN(year) AS min_year, MAX(year) AS max_year
FROM coverage;

-- 4. List all vaccines (antigens) tracked
SELECT DISTINCT antigen
FROM coverage
ORDER BY antigen;

-- 5. Coverage distribution (latest year, global)
WITH latest AS (SELECT MAX(year) AS y FROM coverage)
SELECT
  antigen,
  ROUND(AVG(coverage)::numeric, 2) AS avg_coverage
FROM coverage
WHERE year = (SELECT y FROM latest)
GROUP BY antigen
ORDER BY avg_coverage DESC;

-- 6. Simple country summary (example: India)
SELECT
  year,
  antigen,
  coverage
FROM coverage
WHERE code = 'IND'
ORDER BY year, antigen;
