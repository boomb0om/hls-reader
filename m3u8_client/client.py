from typing import Optional
import m3u8
import requests


class M3U8Client:

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session if session else requests.Session()

    def get_segment(self, data: tuple[int, str]) -> tuple[int, bytes]:
        index, url = data
        return index, self.session.get(url).content

    def parse_segments(self, m3u8_data: m3u8.M3U8) -> bytes:
        data_to_parse = [(c, m3u8_data.base_uri+segment) for c, segment in enumerate(m3u8_data.files)]
        results = sorted(map(self.get_segment, data_to_parse), key=lambda x: x[0])
        result = b''
        for index, data in results:
            result += data
        return result

    def download_url(self, url: str) -> bytes:
        data = self.session.get(url)
        return self.download(data.text, url)

    def download(self, m3u8_content: str, url: str) -> bytes:
        m3u8_data = m3u8.loads(m3u8_content, url)
        return self.parse_segments(m3u8_data)