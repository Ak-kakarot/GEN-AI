from datetime import datetime
import pytz

a=pytz.timezone("Asia/tokyo")
b=datetime.now(a)
print(b)
