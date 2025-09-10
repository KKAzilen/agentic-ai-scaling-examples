import asyncio, aiohttp

async def fetch(session, url, payload):
    async with session.post(url, json=payload) as resp:
        return await resp.json()

async def batch_call(url, payloads):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, p) for p in payloads]
        return await asyncio.gather(*tasks)

# Usage
# asyncio.run(batch_call("https://api.example.com/agent", payloads))
