import os
import time
import random
rr = ['18dRKncZayMGrE7Y1rUUQ4DVpqE97e2PXF', '1tf6QnAsDfkhS7b9EeqwFJtfFEpJjxo92', '136wKFtMX4trEbPKDUeP4d7rYBynxukDCZ']

if __name__ == "__main__":
	while 1:
		aa = "./bitcoin-cli sendtoaddress %s %f" % (random.choice(rr), random.random()/10.0)
		os.system(aa)
		os.system("./bitcoin-cli getwalletinfo")
		print aa
		time.sleep(random.random() * 3)