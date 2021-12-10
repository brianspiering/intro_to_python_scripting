"Print today's day of the week"

from datetime import date

def main():
    day_of_week = date.today().strftime('%a')
    print(day_of_week)

if __name__ == '__main__':  # Code to execute if called from command-line. If imported, don't run
    main()    
