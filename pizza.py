#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the price of a pizza
#    using the diameter provided by the user

import constants


def main():

    # this function calculates price

    # input
    diameter = int(
        input("Enter the diameter of the pizza you would " + "like (inch): ")
    )

    # process
    sub_total = (
        constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    )
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
