"""
Functions to calculate implied probability of American betting odds
and remove house edge (vig) from American odds. Returns a formatted JSON response.
"""

def get_implied(american_odds: int):
    if american_odds < 0:
        implied = (abs(american_odds) / (abs(american_odds) + 100)) * 100
    else:
        implied = (100 / (american_odds + 100)) * 100
    return round(implied, 3)

def remove_vig(first_probability: float, second_probability: float):
    total = first_probability + second_probability
    no_vig_first = first_probability / total
    no_vig_second = second_probability / total
    return [no_vig_first, no_vig_second]

def remove_vig_formatted(first_probability: float, second_probability: float):
    first_formatted = str(round(first_probability * 100, 3)) + "%"
    second_formatted = str(round(second_probability * 100, 3)) + "%"
    return [first_formatted, second_formatted]

def main(odds1: int, odds2: int):
    odds1 = get_implied(odds1)
    odds2 = get_implied(odds2)
    fair_odds = remove_vig(odds1, odds2)
    fair_odds_formatted = remove_vig_formatted(fair_odds[0], fair_odds[1])
    return {
        "no vig first": fair_odds_formatted[0],
        "no vig second": fair_odds_formatted[1]
    }

if __name__ == "__main__":
    print(main(120, -137))
