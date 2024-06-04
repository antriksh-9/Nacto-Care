# utils.py
import httpx

async def verify_recaptcha(token: str) -> bool:
    url = "https://www.google.com/recaptcha/api/siteverify"
    payload = {
        'secret': "6LfsY-8pAAAAANjrT-Y7an1-Va3NkUTgDp9Y_oHS",
        'response': token
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=payload)
        result = response.json()

        score = result.get("score", 0)
        threshold = 0.5
        return score >= threshold and result.get("success", False)