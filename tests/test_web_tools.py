import pytest

from nanobot.agent.tools.web import SearXNGSearchTool


@pytest.mark.asyncio
async def test_searxng_search_requires_base_url() -> None:
    tool = SearXNGSearchTool()

    result = await tool.execute(query="nanobot")

    assert "SearXNG base URL not configured" in result


@pytest.mark.asyncio
async def test_searxng_search_formats_results(monkeypatch) -> None:
    class _FakeResponse:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {
                "results": [
                    {
                        "title": "Example Result",
                        "url": "https://example.com/post",
                        "content": "Example snippet",
                    }
                ]
            }

    class _FakeClient:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb) -> None:
            return None

        async def get(self, url, params=None, headers=None, timeout=None):
            assert url == "https://searx.example/search"
            assert params["q"] == "nanobot"
            assert params["format"] == "json"
            return _FakeResponse()

    monkeypatch.setattr("nanobot.agent.tools.web.httpx.AsyncClient", _FakeClient)

    tool = SearXNGSearchTool(base_url="https://searx.example", max_results=5)
    result = await tool.execute(query="nanobot")

    assert "Results for: nanobot" in result
    assert "Example Result" in result
    assert "https://example.com/post" in result
    assert "Example snippet" in result