months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date :
            month, day, year = date.split("/")
        elif "," in date:
            month, day, year = date.split(" ")
            day = day.replace(",", "")

            if month not in months:
                continue
            else:
                month = months.index(month) + 1
        else:
            continue

        month = int(month)
        day = int(day)
        year = int(year)

        if month > 12:
            continue

        if day > 31:
            continue
        break

    except ValueError:
        pass

print(f"{year}-{month:02}-{day:02}")
