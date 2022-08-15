import time
from django.http import HttpResponse
from scripts.csv_to_sql.commands_core import DBConnection, Copy
from scripts.utils import run_time_calculation
import pandas as pd
from loguru import logger

logger.add('log.log')

connect = DBConnection(db_name='', user_name='', password='', host='', port='')

sql_copy = Copy()


@run_time_calculation
def export_csv_to_database(table_name: str, fields: list, file_path, delimiter: str):
    start = time.time()
    sql_copy.set_command(table_name=table_name, fields=fields, file_path=file_path, delimiter=delimiter)
    connect.connect_and_run(sql_copy.get_command())
    data_frame = pd.read_csv(file_path)
    logger.info(f'Загруженно: {len(data_frame)} записей. Время выполнения: {time.time() - start} секунд')
    return HttpResponse()