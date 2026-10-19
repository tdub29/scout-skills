# Search Tools

Exa AI search engine.

## Exa AI Search

High-quality AI search engine, well suited to finding technical documentation, official examples, and relevant web pages.

```bash
mcporter call exa.web_search_exa query="query" numResults=5
mcporter call exa.web_search_exa query="library API code example" numResults=5
```

### When to use it

| Scenario | Parameters |
|-----|------|
| Web search | `web_search_exa(query: "...", numResults: 5)` |
| Technical / code material | `web_search_exa(query: "framework name API example", numResults: 5)` |

> Exa MCP's `get_code_context_exa` is deprecated and is not registered by default. Use
> `web_search_exa` for code questions too; when you need to search the contents of a repository
> precisely, use the GitHub search in `dev.md` instead.

### Characteristics

- Strong on English-language content and technical documentation
- Query terms can pinpoint official docs and code examples
- High result quality

## Compared with the other search tools

| Tool | Source | Best for |
|-----|------|---------|
| Exa | agent-reach | English / technical / code search |
| Zhipu search (æ™ºè°±æœç´¢) | my-mcp-tools | Chinese-language search |
| GitHub search | agent-reach (dev.md) | Repository / code search |
