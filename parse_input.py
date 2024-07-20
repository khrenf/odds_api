"""
Parses American odds string and checks for validity. Ex: removes "+" from "+155" and ensures
the input is in the right format. Returns an integer of the input.
"""

def parse(odds: str):
    odds = odds.strip()
    try:
        number = int(odds)
    except:
        return None
    return number

if __name__ == "__main__":
    print(parse("--155"))
