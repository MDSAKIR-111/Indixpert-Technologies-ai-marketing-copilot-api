import httpx


class FacebookPublisher:

    GRAPH_URL = "https://graph.facebook.com/v23.0"

    @staticmethod
    async def publish_text(
        page_id: str,
        access_token: str,
        message: str,
    ):
        url = f"{FacebookPublisher.GRAPH_URL}/{page_id}/feed"

        payload = {
            "message": message,
            "access_token": access_token,
        }

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, data=payload)

        return {
            "status_code": response.status_code,
            "response": response.json()
        }