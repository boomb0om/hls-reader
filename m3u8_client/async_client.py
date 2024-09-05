import asyncio
import m3u8
import httpx


class AsyncM3U8Client:

    async def get_segment(self, index: int, url: str) -> tuple[int, bytes]:
        async with httpx.AsyncClient() as client:
            content = (await client.get(url)).content
        return index, content

    async def parse_segments(self, m3u8_data: m3u8.M3U8) -> bytes:
        tasks = [self.get_segment(c, m3u8_data.base_uri+segment) for c, segment in enumerate(m3u8_data.files)]
        results = await asyncio.gather(*tasks)
        result = b''
        for index, data in results:
            result += data
        return result

    async def download_url(self, url: str) -> bytes:
        async with httpx.AsyncClient() as client:
            data = (await client.get(url)).text
        return await self.download(data, url)

    async def download(self, m3u8_content: str, url: str) -> bytes:
        m3u8_data = m3u8.loads(m3u8_content, url)
        return await self.parse_segments(m3u8_data)