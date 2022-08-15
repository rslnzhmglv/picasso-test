# from csv_to_db_api.models import Report
import pandas as pd


# def csv_to_db(url):
#     """Парсер csv через pandas"""
#     data = pd.read_csv(url)
#     row_iter = data.iterrows()
#     reports = [Report(
#         crime_id=row['Crime Id'],
#         original_crime=row['Original Crime Type Name'],
#         report_date=row['Report Date'].replace('T', ' '),
#         call_date=row['Call Date'].replace('T', ' '),
#         offense_date=row['Offense Date'].replace('T', ' '),
#         call_time=row['Call Time'],
#         call_date_time=row['Call Date Time'].replace('T', ' '),
#         description=row['Disposition'],
#         address=row['Address'],
#         city=row['City'],
#         state=row['State'],
#         agency_id=row['Agency Id'],
#         address_type=row['Address Type'],
#         common_location=row['Common Location'],
#     ) for index, row in row_iter
#     ]
#     Report.objects.bulk_create(reports)
#     return len(reports)
