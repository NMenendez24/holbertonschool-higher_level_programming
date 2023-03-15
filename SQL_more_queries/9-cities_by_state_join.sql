-- Lists all the cities and their State
SELECT cities.id, cities.name, states.name FROM cities JOIN states ORDER BY cities.id ASC;