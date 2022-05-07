import tushare as ts
import datetime as dt
import string

class StockData:
	def __init__(self):
		self.pro = ts.pro_api('e19aafa11f448013391188bb7a008ed542cc823a9c6bab386efedc03')
		
	def get_daily_data(self, ts_code, days):
		current_date = dt.date.today()
		last_date = dt.date.today() - dt.timedelta(days)
		data = self.pro.daily(ts_code=ts_code,
							start_date=('%04d'%last_date.year) + ('%02d'%last_date.month) + ('%02d'%last_date.day),
							end_date=('%04d'%current_date.year) + ('%02d'%current_date.month) + ('%02d'%current_date.day)
						)
		return data

if __name__ == '__main__':
	sd = StockData()
	print(sd.get_daily_data('002415.SZ', 100))