
import random
from datetime import datetime,timedelta,date
print("Random integer between 0 to 6:",random.randint(0,5))
print("Random integer between 5 to 10:",random.randint(5,9))
print("Random integer between 0 to 10:",random.randint(0,10))
sd=date(2003,8,7)
ed=date(2023,9,13)

difference=(ed-sd).days
random_d=random.randint(1,difference)
rd=sd+timedelta(days=random_d)
print("The random date is:",rd)
