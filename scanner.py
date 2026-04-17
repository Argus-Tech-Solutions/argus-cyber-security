import asyncio, httpx

TARGETS = ["https://example.com"]

async def stress_test(target: str, connections: int = 100):
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [client.get(target) for _ in range(connections)]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    ok = sum(1 for r in results if isinstance(r, httpx.Response) and r.status_code == 200)
    print(f"[{target}] {ok}/{connections} OK")

if __name__ == "__main__":
    for t in TARGETS:
        asyncio.run(stress_test(t))
