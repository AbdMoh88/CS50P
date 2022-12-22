def main():
    time = input("What time is it? ")
    time_float = convert(time)
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.rstrip("amp.").split(":")
    if time.lower().endswith("a.m."):
        hours = float(hours) + 0
    elif time.lower().endswith("p.m."):
        hours = float(hours) + 12
    time_float = round(float(hours) + float(minutes)/60, 2)
    return(time_float)

main()
