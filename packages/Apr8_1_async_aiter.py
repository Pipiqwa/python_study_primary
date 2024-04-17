"""
还得是用Claude啊... 额？这个注释？
"""

import asyncio

async def generate_numbers():
    """使用aiter()异步生成一些数字"""
    for i in range(1, 6):
        print(f"Generating number: {i}")
        await asyncio.sleep(1)
        yield i    #产生（收益、效益等），产生（结果）；出产（天然产品，农产品，工业产品）；屈服，让步；放弃，让出；给（大路上的车辆）让路；（受压）活动，弯曲，折断

async def main():
    """主函数,使用aiter()从生成器中异步获取数字"""
    async for num in generate_numbers():
        print(f"Received number: {num}")

asyncio.run(main())