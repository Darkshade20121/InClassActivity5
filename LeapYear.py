def main():
    year = int(input("Enter a year: "))
    leap_year(year)

def leap_year(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


if __name__ == "__main__":
    main()
