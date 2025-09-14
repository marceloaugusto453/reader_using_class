import schedule
import time
from lib.classes.CsvSources import CsvSources
from lib.classes.TxtSources import TxtSources

def check_for_new_files():
    csv_source.check_for_new_files()  
    txt_source.check_for_new_files()


schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSources()
txt_source = TxtSources()


while True:
    schedule.run_pending()
    time.sleep(1)  