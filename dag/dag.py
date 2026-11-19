--jobbbb

--ccc

--ddd

-- Data Quality Check: Memastikan tidak ada email atau ID yang duplikat   ----- проверка гарантирует отсутствие дублирующихся электронных писем или идентификаторов
SELECT
    email,
    COUNT(*) as duplicate_count
FROM users_etl
GROUP BY email
HAVING COUNT(*) > 1;

-- Audit Data: Cek apakah ada kolom krusial yang bernilai NULL/Kosong ----- Аудит данных: проверяет, есть ли важный столбец, который является нулевым / пустым
SELECT
    COUNT(*) FILTER (WHERE first_name IS NULL) as missing_first_name,
    COUNT(*) FILTER (WHERE email IS NULL) as missing_email,
    COUNT(*) FILTER (WHERE university IS NULL) as missing_university
FROM users_etl;