#!/bin/bash

echo "Starting deployment..."

# 1️⃣ Activate virtual environment
source venv/bin/activate

# 2️⃣ Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3️⃣ Load environment variables (if you have .env)
export $(grep -v '^#' .env | xargs)

# 4️⃣ Run the FastAPI app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
