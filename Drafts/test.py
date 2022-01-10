from datetime import date

today = date.today()

print(f"Shopping List: Week of Sunday, {today.strftime('%B')} {today.strftime('%w')}, {today.strftime('%Y')}")