# F1 Driver Summary API

## What this does

This project takes data from the F1 2025 season race results and calculates the total points and wins for each driver. It then passes that data to Claude in a formatted prompt and returns an AI-generated summary of the driver's season performance.

## How to run it

1. Install dependencies: `pip install fastapi anthropic uvicorn pandas`
2. Start the server: `python -m uvicorn main:app --reload`
3. Test the endpoint: Go to `http://127.0.0.1:8000/docs` and enter a driver name

## What I learned

1. I learned how to use pandas groupby and agg to calculate statistics from raw CSV data
2. I learned how to build a FastAPI endpoint that takes user input, processes it, and calls Claude API
3. I learned how to work with Claude's API response format and...
