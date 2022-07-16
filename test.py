import time
from datetime import datetime
start = datetime.now()

#start = time.time()

for i in range(100000000):
    continue

print('elapsed time : {} '.format(datetime.now()-start))


