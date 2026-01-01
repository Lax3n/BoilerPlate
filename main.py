import rnet
import asyncio
import aiofiles
import random


async def get_proxy(file:str)->str:
    async with aiofiles.open(file=file,mode="r") as f:
        proxies=(await f.read()).strip().split("\n")
        proxy=random.choice(proxies)
        if "http://" in proxy:
            return proxy
        else:
            ip,port,user,pwd=proxy.split(":")
            return f"http://{user}:{pwd}@{ip}:{port}"


async def main():
    jar=rnet.Jar()
    proxy=rnet.Proxy.all(await get_proxy("./proxies.txt"))
    emulation=rnet.EmulationOption(rnet.Emulation.Chrome142,rnet.EmulationOS.Windows)
    redirect_policy=rnet.redirect.Policy.limited()
    client=rnet.Client(cookie_provider=jar,proxies=[proxy],emulation=emulation,redirect=redirect_policy)
    r=await client.get("https://probe.velys.software/")
    print(r.status)
    print(await r.json())

    
if __name__ == "__main__":
    asyncio.run(main())
