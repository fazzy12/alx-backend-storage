-- Script lists all bands with Glam rock as
-- their main style, ranked by their longevity
-- SELECT band_name, IF(split IS NULL, 2020, split) - formed AS lifespan
-- FROM metal_bands
-- WHERE style LIKE '%Glam rock%'
-- ORDER BY lifespan DESC;
SELECT band_name, (YEAR(split) - YEAR(formed)) AS lifespan
FROM metal_bands
WHERE style = '%Glam rock%'
ORDER BY lifespan DESC;