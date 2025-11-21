import asyncio
import aiohttp

max_pokemon = 1010  # numero totale di Pokémon
pokemon_gif_urls = []

async def fetch(session, url, idx):
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            name = data['name']
            try:
                gif_url = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
                if gif_url:
                    pokemon_gif_urls.append((name, gif_url))
            except KeyError:
                pass
        else:
            print(f"Errore nel recuperare Pokémon ID {idx}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, max_pokemon + 1):
            url = f"https://pokeapi.co/api/v2/pokemon/{i}"
            tasks.append(fetch(session, url, i))
        await asyncio.gather(*tasks)

# Esegui il loop asincrono
asyncio.run(main())

# Stampa tutti i link
for name, gif_url in pokemon_gif_urls:
    print(f"{name}: {gif_url}")
