from fastapi import FastAPI, HTTPException
import uvicorn
from calculate import main as calculate
import parse_input
"""
Runs an API that takes American odds as input and serves results
as no-vig "fair odds" 
"""

app = FastAPI()
@app.get("/novig")
def get_no_vig(param1: str, param2: str):
    print(param1, param2)
    odds_one = parse_input.parse(param1)
    odds_two = parse_input.parse(param2)
    if odds_one is None:
        raise HTTPException(status_code=400, detail=f"Invalid format: '{param1}'")
    if odds_two is None:
        raise HTTPException(status_code=400, detail=f"Invalid format: '{param2}'")
    return calculate(odds_one, odds_two)
    
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)