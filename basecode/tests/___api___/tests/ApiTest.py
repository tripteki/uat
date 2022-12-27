import asyncio
from ..src.TestCase import TestCase

class ApiTest (TestCase):

    async def api (self) -> None:
        """
        :rtype: None
        """
        async with self.driver ().get ("http://localhost:80", headers = {
            "Accept-Language": "en-US",
            "Accept-Charset": "utf-8",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }) as response:
            self.assertEqual (response.status, 200)

    def test_api (self) -> None:
        """
        :rtype: None
        """
        asyncio.run (self.api ())
