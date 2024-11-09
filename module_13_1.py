# import time
import asyncio

async def start_strongman(name, power):
    k = 1
    delay = k / power
    print(f'Силач {name} начал соревнование')
    for num_ball in range(1, 6):
        if power >= num_ball:
            await asyncio.sleep(delay)
            print(f'Силач {name} поднял {num_ball} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Timur', 5))
    # tasks = [task_1, task_2, task_3]
    # for task in tasks:
    #     await task
    await task_1
    await task_2
    await task_3

if __name__ == '__main__':
    asyncio.run(start_tournament())
