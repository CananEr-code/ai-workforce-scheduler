from utils import load_data
from scheduler import generate_schedule

def main():
    data = load_data("data/sample_schedule.csv")
    schedule = generate_schedule(data)
    print(schedule)

if __name__ == "__main__":
    main()
