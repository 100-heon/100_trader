# AI-Trader FastAPI Dashboard on Railway

This guide shows how to expose the trading data through the bundled FastAPI service (`webapp/main.py`) and deploy it to [Railway](https://railway.app/).

## 1. Local quick start

```bash
# From the project root
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r webapp/requirements.txt
uvicorn webapp.main:app --reload
```

Navigate to `http://127.0.0.1:8000/api/signatures` to see the detected agent signatures. Endpoints include:

- `GET /api/summary` — overview of known signatures and latest cash balance.
- `GET /api/positions/{signature}?limit=100` — recent position records.
- `GET /api/metrics/{signature}` — stored performance metrics (if any).

## 2. Docker image (used by Railway)

```bash
docker build -t ai-trader-dashboard .
docker run --rm -p 8000:8000 ai-trader-dashboard
```

Ensure the `data/agent_data` directory is present inside the container. For production you can mount it or sync via CI.

## 3. Deploying to Railway

1. Create a Railway account and install the CLI (`npm i -g @railway/cli`).
2. In the project root run:
   ```bash
   railway login
   railway init        # create / link a project
   railway up          # builds Dockerfile, deploys, assigns a URL
   ```
3. Railway uses the root `Dockerfile`; no extra configuration is required. The default command runs `uvicorn webapp.main:app --host 0.0.0.0 --port 8000`.
4. Add any environment variables (if needed) through the Railway dashboard or `railway variables set KEY=value`.

## 4. Keeping data fresh

The API reads JSONL files from `data/agent_data/<signature>/position/`. To keep the hosted dashboard current you have a few options:

- Commit updated JSONL files to the repository and redeploy.
- Push data artifacts to cloud storage (S3, Railway Storage) and mount/download them during container start-up.
- Add a background job or webhook that syncs files to Railway on each trading run.

## 5. Frontend ideas

With the API live, you can host a lightweight frontend (e.g., React + Vite) on Railway, Vercel, or Cloudflare Pages. Fetch the endpoints above to render leaderboards, PnL charts, and latest trade logs.

For local development, enable CORS origins in `webapp/main.py` if you prefer to lock down access.
