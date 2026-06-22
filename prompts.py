def build_driver_prompt(driver_name, points, wins):
    prompt = f""" 
You are a Formula 1 analyst. 

Driver: {driver_name}
Points: {points}
Wins: {wins}

Write a 2-3 sentence summary of their 2025 performance.
"""
    return prompt

prompt = build_driver_prompt("Max Verstappen", 700, 10)
print(prompt)