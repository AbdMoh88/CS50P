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
        if "," in date:
            year = date.split()[2]
            month = months.index(date.split()[0]) + 1
            day = int(date.split()[1].split(",")[0])
            if 1 <= day <= 31 and 1 <= month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
        elif "/" in date:
            year = date.split("/")[2]
            month = int(date.split("/")[0])
            day = int(date.split("/")[1])
            if 1 <= day <= 31 and 1 <= month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
    except ValueError:
        pass

