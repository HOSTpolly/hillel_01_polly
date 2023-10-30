# import asyncio
# import sys

# # from time import perf_counter


# BASE_URL = "https://pokeapi.co/api/v2"


# async def pokemons_requests(urls: list[str]):
#     import requests

#     tasks = [asyncio.to_thread(requests.get, url) for url in urls]
#     results = await asyncio.gather(*tasks)

#     return results


# def pokemons_grequests(urls: list[str]):
#     import grequests

#     results = grequests.map((grequests.get(url) for url in urls))

#     return results


# async def pokemons_httpx(urls: list[str]):
#     import httpx
#     from typing import Coroutine
#     results = []
#     async with httpx.AsyncClient() as client:
#         tasks: list[Coroutine] = [client.get(url) for url in urls]
#         results = await asyncio.gather(*tasks)

#     return results


# async def _pokemons_aiohttp(session, url):
#     async with session.get(url) as response:
#         return await response.json()


# async def pokemons_aiohttp(urls: list[str]):
#     import aiohttp
#     from typing import Coroutine
#     results = []
#     async with aiohttp.ClientSession() as session:
#         tasks: list[Coroutine] = [_pokemons_aiohttp(session, url) for url in urls]
#         results = await asyncio.gather(*tasks)

#     return results


# def main():
#     urls = [f"{BASE_URL}/pokemon/{i}" for i in range(1, 30)]

#     match sys.argv[1]:
#         case "requests":
#             results =asyncio.run(pokemons_requests(urls))
#         case "grequests":
#             results = pokemons_grequests(urls)
#         case "httpx":
#             results = asyncio.run(pokemons_httpx(urls))
#         case "aiohttp":
#             results = asyncio.run(pokemons_aiohttp(urls))
#         case _:
#             raise Exception("Unknown choise")

#     # print(results)


# if __name__ == "__main__":
#     main()
