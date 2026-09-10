from trafilatura import fetch_url, extract
import json


def scrape_website(url: str) -> dict:
    # Add https:// if user forgets it
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    html = fetch_url(url)

    if html is None:
        return {"error": "Failed to fetch website"}

    content = extract(html, output_format="json", with_metadata=True)

    if content is None:
        return {"error": "Failed to extract content"}

    return json.loads(content)
