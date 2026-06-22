from fastapi import FastAPI
import anthropic
from data import load_drivers
from prompts import build_driver_prompt
import os

app = FastAPI()

@app.post("/driver/summary")
def get_driver_summary(driver_name: str):
    drivers = load_drivers()
    driver = None
    for d in drivers:
        if d['driver_name'] == driver_name:
            driver = d
            break
    prompt = build_driver_prompt(driver['driver_name'], driver['total_points'], driver['wins'])

    client = anthropic.Anthropic(api_key=os.emviron.get("claude_api_key"))
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role":"user", "content": prompt}]
    )
    
    response = message.content[0].text
    return {"driver": driver_name, "summary": response}
