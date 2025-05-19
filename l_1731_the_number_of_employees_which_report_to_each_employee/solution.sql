SELECT e0.employee_id, e0.name, COUNT(e1.employee_id) AS reports_count, ROUND(AVG(e1.age)) AS average_age
FROM employees e0
JOIN employees e1 ON e0.employee_id = e1.reports_to
GROUP BY e0.employee_id, e0.name
ORDER BY e0.employee_id;
