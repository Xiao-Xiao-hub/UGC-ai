# Miliastra Toolbox

AI-assisted tools for working with the Miliastra sandbox editor.

## Deployment and development

Start with the module documentation:

1. [Docker deployment](./docker/README.md)
2. [Knowledge-base construction](./knowledge/rag_v1/README.md)
3. [Frontend build](./frontend/README.md)
4. [Backend startup](./backend/README.md)

Frontend build output under `backend/static/` is not committed. Build the frontend with `cd frontend && npm run build` before restarting the backend. The repository contains source and configuration rather than generated bundles.

## Capabilities and roadmap

- [x] Knowledge Q&A across guide and tutorial collections.
- [x] FastAPI backend and React frontend, including configured model access.
- [x] Shared knowledge-query capabilities through MCP and the HTTP Skill API.
- [ ] Parameter-data aggregation and conversational design assistance.
- [ ] Multimodal retrieval for finding assets from descriptions.

Much of the code was generated with AI assistance.

## Project structure

```text
backend/                    FastAPI, chat, retrieval, and Skill API
frontend/                   React interface
mcp/                        MCP knowledge tools
knowledge/spider/           Official-documentation crawler
knowledge/bbs_spider/       Community Q&A crawler
knowledge/rag_v1/           Vector indexing and retrieval
knowledge/Miliastra-knowledge/  Markdown knowledge submodule
docker/                     Docker Compose configuration
```
