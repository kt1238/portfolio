import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='mysqlpass')
cursor = cnx.cursor()

db_name = 'kmbd'

# Making kmdb database ready to use
try:
    cursor.execute(f"CREATE DATABASE {db_name} DEFAULT CHARACTER SET 'utf8';")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DB_CREATE_EXISTS:
        print('Database already exists.')
    else:
        print('Issue in creating database.')
else:
    print('Database created successfully')
finally:
    cursor.execute(f"USE {db_name}")
    print(f'{db_name} is now accessible.')

# Creating Table (if not present)
try:
    cursor.execute(
    """
    CREATE TABLE `kmbd`.`movies` (
    `movie_id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `release_year` INT NULL,
    `language` VARCHAR(45) NULL,
    `genre_1` VARCHAR(45) NULL,
    `watched` TINYINT NULL,
    `priority` INT NULL,
    `extra_info` VARCHAR(100) NULL,
    PRIMARY KEY (`movie_id`));
    """
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print('movies table already exists.')
else:
    print('movies table created successfully.')
finally:
    print('movies table is accessible')

# Adding values to table
try:
    # MySQL can only read from this location due to secure-file-priv setting.
    cursor.execute(
    """
    LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/movies.csv' 
    INTO TABLE movies
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
    """
        )

    cnx.commit()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DUP_ENTRY:
        print('Table already filled.')
else:
    print('Added values to movies table')
finally:
    print('movies table filled and ready to be queried.')