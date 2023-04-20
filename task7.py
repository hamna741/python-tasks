import asyncio
import logging
import time


async def find_divisibles(dividend,  divisor):
    
    logging.info(f"Finding divisible numbers in range 1-{dividend} by {divisor}")
    count = 0
    for num in range(1, dividend + 1):
        if num % divisor == 0:
            count += 1
        if num%20000==0:
            await asyncio.sleep(0.0000000001)
    logging.info(f"Found {count} divisible numbers in range 1-{dividend} by {divisor}")
    return count


async def main():
    logging.basicConfig(filename='divisibles.log', level=logging.INFO)
    logging.info(f" <----ASYNCRONOUS---->")
    start_time = time.time()

    tasks = [
        asyncio.create_task(find_divisibles(50800000, 3411)),
        asyncio.create_task(find_divisibles(100052,3210)),
        asyncio.create_task(find_divisibles(20000,5)),
    ]

    for task in tasks:
        result = await task
        logging.info(f"Result: {result}")
       # await asyncio.sleep(0.000000000001)

    end_time = time.time()
    logging.info(f"Total time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())