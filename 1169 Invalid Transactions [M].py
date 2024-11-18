from collections import defaultdict

def invalidTransactions(transactions: list[str]) -> list[str]:
    name_to_city = defaultdict(set)
    namecity_to_id = defaultdict(set)

    added = set()
    invalid = []

    for i,t in enumerate(transactions):
        name, time, amount, city = t.split(",")
        time = int(time)
        amount = int(amount)
        namecity = (name,city)

        name_to_city[name].add(city)
        namecity_to_id[namecity].add(i)

        # for each city associated with a given name...
        for _city in name_to_city[name]:
            if _city == city:
                continue
            _namecity = (name,_city)
            # find all transactions for a given (name, city) pair
            idxs = namecity_to_id[_namecity]
            # for each one of those transactions...
            for _i in idxs:
                _,_time,_,_ = transactions[_i].split(",")
                _time = int(_time)
                # check if they are within 60 seconds, and add it as invalid if so
                if abs(_time - time) <= 60:
                    if i not in added:
                        invalid.append(t)
                        added.add(i)
                    if _i not in added:
                        invalid.append(transactions[_i])
                        added.add(_i)
        # if the amount > 1000 add it as invalid
        if amount > 1000 and i not in added:
            invalid.append(t)
            added.add(i)
    return invalid

CASE = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]

print(invalidTransactions(CASE))