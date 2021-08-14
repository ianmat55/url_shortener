DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	original_url TEXT NOT NULL,
	clicks INTEGER NOT NULL DEFAULT 0
);
-- delete 'urls' table if already exists
-- *important: will delete all data whenever the schema file executes
