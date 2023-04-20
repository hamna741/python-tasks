import asyncio
import time
import logging

def divisbility_check(dividend, divisor):
    
    logging.info(f"finding divisible numbers in range 1 -{dividend} by {divisor}")
    count = 0
    for i in range(1,dividend+1):
        if i%divisor==0:
            count+=1
    logging.info(f"Found {count} divisible numbers in range 1-{dividend} by {divisor}")
logging.basicConfig(filename='divisibles.log', level=logging.INFO)
logging.info(f" <----SYNCRONOUS---->")
start_time =time.time()
divisbility_check(50800000, 3411)
divisbility_check(100052,3210)
divisbility_check(20000,5)
end_time=time.time()
logging.info(f"Total time taken: {end_time - start_time} seconds")

