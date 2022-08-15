from scripts.csv_to_sql.commands_core import DBConnection

connection = DBConnection(db_name='', user_name='', password='', host='', port='')

sql_create = """CREATE TABLE [IF NOT EXISTS] reports (
                id SERIAL PRIMARY KEY , 
                crime_id INT NOT NULL ,
                original_crime VARCHAR ( 50 ),
                report_date TIMESTAMP WITH TIME ZONE NOT NULL,
                call_date TIMESTAMP WITH TIME ZONE NOT NULL,
                offense_date TIMESTAMP WITH TIME ZONE NOT NULL,
                call_time TIME NOT NULL,
                call_date_time TIMESTAMP WITH TIME ZONE NOT NULL,
                disposition TEXT,
                address VARCHAR ( 255 ),
                city VARCHAR ( 50 ),
                state VARCHAR ( 50 ),
                agency_id INT NOT NULL ,
                address_type VARCHAR ( 255 ),
                common_location VARCHAR ( 255 ));
"""


def create_table() -> None:
    connection.connect_and_run(sql_create)

