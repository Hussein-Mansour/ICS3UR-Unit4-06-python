#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/May19/2021
# This program uses nested loops


def main():
    # This function prints out ALL the valid RGB values
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    # process & output
    for counter_1 in range(226):
        for counter_2 in range(226):
            for counter_3 in range(226):
                print(
                    "RGB({2},{1},{0})".format(counter_3, counter_2, counter_1))
    print("\nDone.")


if __name__ == "__main__":
    main()
