# MediaHub API (Login MVP)

## Setup

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env  # edit JWT_SECRET!
uvicorn app.main:app --reload
