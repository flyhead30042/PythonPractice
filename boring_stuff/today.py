from datetime import datetime


timestamp1 = datetime.now().strftime("%Y%m%d %a %H%M%S")
print(timestamp1)

timestamp2 = datetime.now().strftime("%Y%m%d %a %I%M%S  %p")
print(timestamp2)