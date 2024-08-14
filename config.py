from urllib.parse import urlparse

ENV = "prod"

if ENV == 'dev':
    DATABASE_CONFIG = {
        'host': "localhost",
        'database': "babyfoot",
        'user': "postgres",
        'password': "**"
    }
else: 

    uri = "****"
    parsed_uri = urlparse(uri)

    DATABASE_CONFIG = {
        'host': "dpg-cquc0qbqf0us73a9tg10-a",
        'database': "ratingdb",
        'user': "ratinguser",
        'password': "l8Lz3Nh9y6JBEX7UBBABHGCbyUuvY1mF",
        'port': "5432"
    } 
