import pandas as pd
from boring_stuff import today

PEOPLE = [
    {"fname": "Koug", "lname": "Farrell", "timestamp": today.get_timestamp1()},
    {"fname": "Kent", "lname": "Brockman","timestamp": today.get_timestamp1()},
    {"fname": "Bunny","lname": "Easter", "timestamp": today.get_timestamp1()}
]

if __name__ == "__main__":
    select = pd.DataFrame(PEOPLE)
    print(select)
    print("---")
    print(select.iloc[0,:].ndim)
    print("---")
    l = select[ (select["fname"] == "Kent") | (select["lname"] == "Easter")]
    print(l)
    print("---")
    for a in l:
        print(a)
