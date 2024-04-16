import asyncio

# 定义一个异步函数，使用async def关键字
async def simple_task(name, seconds):
    print(f'{name}: starting')
    # 模拟耗时操作，使用await asyncio.sleep(seconds)
    await asyncio.sleep(seconds)
    print(f'{name}: finished in {seconds} seconds')

# 主函数，使用asyncio.run()来运行主事件循环
async def main():
    # 创建多个异步任务
    task1 = asyncio.create_task(simple_task('Task 1', 3))
    task2 = asyncio.create_task(simple_task('Task 2', 2))
    task3 = asyncio.create_task(simple_task('Task 3', 1))

    # 等待所有任务完成  # gather 聚集
    await asyncio.gather(task1, task2, task3)

# 运行主函数
asyncio.run(main())


