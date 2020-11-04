class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        invalid = []
        d = {} # name: [[time, amt, city]]
        for transaction in transactions:
            name, time, amt, city = transaction.split(",")
            time, amt = int(time), int(amt)

            # fill the dictionary
            d[name] = d.get(name, []) + [[time, amt, city]]

        for transaction in transactions:
            name, time, amt, city = transaction.split(",")
            time, amt = int(time), int(amt)

            # if the amt exceeds 1000, it's invalid
            if amt > 1000:
                invalid.append(transaction)
                continue

            # if it's within 60 mins of another transaction in diff city, invalid
            arr = d.get(name)
            for prevTime, prevAmt, prevCity in arr:
                if abs(prevTime - time) <= 60 and city != prevCity:
                    invalid.append(transaction)
                    break

        return invalid


