class Category():

    def __init__(self, name):

        self.name = name
        self.ledger = dict()

    def deposit(self, amount, description = ""):

        if description in self.ledger:

            self.ledger[description] += amount

        else:

            self.ledger[description] = amount

    def withdraw(self, amount, description = ""):

        if description in self.ledger:

            self.ledger[description] -= amount

        else:

            self.ledger[description] = - amount

    def get_balance(self):

        n_stars = 30 - len(self.name)
        n_stars_per_side = n_stars // 2
        n_characters = 23

        rows = []
        total = 0
        for key, values in self.ledger.items():

            if len(key) > 23:

                row = key[:23] + " " + str(values)
                rows.append(row)
                total += values
            else:

                row = key + (n_characters - len(key)) * " " + str(values)
                rows.append(row)
                total += values

        rows.append(f"Total: {total}")

        string = n_stars_per_side * "*" + str(self.name) \
                 + (n_stars - n_stars_per_side) * "*" + "\n"

        for row in rows:

            string = string + row + "\n"


        return string
