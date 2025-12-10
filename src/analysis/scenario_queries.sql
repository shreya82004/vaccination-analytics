-- 1. Time-Series: Global coverage trends for key vaccines
SELECT 
  year,
  antigen,
  ROUND(AVG(coverage)::numeric, 2) AS global_avg_coverage
FROM coverage
WHERE antigen IN ('BCG', 'DTPCV3', 'MCV1', 'POL3')
GROUP BY year, antigen
ORDER BY year, antigen;

-- 2. YoY growth rate for DTP3 global average coverage
WITH yearly_avg AS (
  SELECT 
    year,
    antigen,
    AVG(coverage) AS avg_cov
  FROM coverage
  WHERE antigen = 'DTPCV3'
  GROUP BY year, antigen
)
SELECT 
  year,
  ROUND(avg_cov::numeric, 2) AS coverage,
  ROUND(((avg_cov - LAG(avg_cov) OVER (ORDER BY year)) / 
         LAG(avg_cov) OVER (ORDER BY year) * 100)::numeric, 2) AS yoy_growth_pct
FROM yearly_avg
ORDER BY year;

-- 3. Top 5 best & worst performers for MCV1 (latest year)
WITH latest AS (
  SELECT MAX(year) AS y FROM coverage
)
(SELECT 
   name AS country,
   coverage,
   'Top Performer' AS category
 FROM coverage
 WHERE antigen = 'MCV1' AND year = (SELECT y FROM latest)
 ORDER BY coverage DESC
 LIMIT 5)
UNION ALL
(SELECT 
   name,
   coverage,
   'Needs Improvement' AS category
 FROM coverage
 WHERE antigen = 'MCV1' AND year = (SELECT y FROM latest)
 ORDER BY coverage ASC
 LIMIT 5);

-- 4. Regional inequality (STDDEV, coefficient of variation) for DTP3
WITH latest AS (SELECT MAX(year) AS y FROM coverage)
SELECT 
  v.region,
  COUNT(DISTINCT c.code) AS num_countries,
  ROUND(AVG(c.coverage)::numeric, 2) AS mean_coverage,
  ROUND(STDDEV(c.coverage)::numeric, 2) AS std_dev,
  ROUND((STDDEV(c.coverage) / AVG(c.coverage) * 100)::numeric, 2) AS coeff_variation_pct
FROM coverage c
JOIN vaccine_introduction v
  ON c.code = v.code
WHERE c.antigen = 'DTPCV3'
  AND c.year = (SELECT y FROM latest)
GROUP BY v.region
ORDER BY coeff_variation_pct DESC;
