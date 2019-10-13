# arquivo-data
Data from twitter scrapping

# Creating the postgres database

$ su - postgres
$ create user db_owner
$ createdb -O db_owner db_name 
$ psql db_name
DB_NAME=# ALTER USER db_owner WITH PASSWORD 'db_password';
DB_NAME=# CREATE TABLE tweets (id serial primary key not null, tweet jsonb, content text, time timestamptz);
DB_NAME=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO "db_owner";
DB_NAME=# CREATE ROLE authenticator nologin;
DB_NAME=# GRANT authenticator TO "db_owner";
DB_NAME=# GRANT USAGE ON SCHEMA public TO authenticator ;
DB_NAME=# GRANT SELECT ON tweets TO authenticator ;
DB_NAME=# GRANT USAGE ON SEQUENCE tweets_id_seq TO authenticator ;
