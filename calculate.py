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
    return {
        "no vig first": round(no_vig_first, 3),
        "no vig second": round(no_vig_second, 3)
    }

if __name__ == "__main__":
    print(remove_vig(get_implied(-115), get_implied(-110)))
