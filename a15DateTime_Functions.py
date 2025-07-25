import datetime

x = datetime.datetime.now()

print(x)

# Modifying the format of the date and time. want to see only hrs:min and am/pm

import datetime

x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d %H:%M"))


