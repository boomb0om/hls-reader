# m3u8-downloader
A python package for async download hls and m3u8 files.

Currently is implemented only for m3u8 with segments.

## Installation

```bash
pip install git+https://github.com/boomb0om/m3u8-downloader
```

## Example

```python
from m3u8_client import M3U8Client
client = M3U8Client()
client.download_url("https://example.com/path/to/file.m3u8")
```

Async example:
```python
from m3u8_client import AsyncM3U8Client
import asyncio

async def main():
    url = "https://example.com/path/to/file.m3u8"
    client = AsyncM3U8Client()
    data = await client.download_url(url)

    with open('test.mp3', 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    asyncio.run(main())
```


