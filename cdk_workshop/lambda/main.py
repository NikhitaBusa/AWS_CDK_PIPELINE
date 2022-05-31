import time
import aiohttp
import asyncio

# Asynchronous solution - Hits 200k calls in 2mins using ascyncio
urls = ['https://q0zjgslzg5.execute-api.us-west-2.amazonaws.com/prod/']*20
start_time = int(time.time())


async def call_endpoint(session, url):
    async with session.get(url) as response:
        print(response)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(call_endpoint(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)

def lambda_handler(event, context):
    # body = json.loads(event["body"])
    statusCode = 200
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))
    return {"statusCode": statusCode, "headers": {}, "body": "HELLO NIKHITA!!"}
