from TestSuite import Assert
"""
Given a list of people with their birth and death years, implement a method to compute
the year with the most number of people alive. You may assume that all people were born between 1900
and 2000 (inclusive). If a person was alive during any portion of that year, they should be
included in that year's count. For example, Person(birth=1908, death=1909) is included in the
counts for both 1908 and 1909.
"""
EARLIEST_YEAR = 1900
LATEST_YEAR = 2000

class Person:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death


def get_sorted_birth(people):
    return sorted(p.birth for p in people)


def get_sorted_deaths(people):
    return sorted(p.death for p in people)


def living_people_info2(people):
    """
    Since every time there's a birth it constitutes to a +1 in number of people alive on the YOB, and a death constitutes
    a -1 on the number of people alive in the YOD + 1, we can create a list of "deltas" to reflect this. Then, we can simply
    walk through our deltas list looking fo the max_value and saving the year.
    :param people:
    :return:
    """
    deltas = [0]* (LATEST_YEAR - EARLIEST_YEAR + 1)
    for p in people:
        y = p.birth - EARLIEST_YEAR
        deltas[y] += 1

        y = p.death - EARLIEST_YEAR + 1
        deltas[y] -= 1

    current_alive = 0
    max_year = 0
    max_alive = 0

    for year, delta in enumerate(deltas):
        current_alive += delta
        if current_alive > max_alive:
            max_year = year + EARLIEST_YEAR
            max_alive = current_alive

    return max_year


def living_people_info(people):
    """
    We will sort the birth_years and death_years of the people. Then, we will initialize two pointers, birth_index, death_index
    to 0. We will use those pointers to walk through the birth_years and death_years and compare them. If a birth year occurs before a death,
    we increment the current_alive count, else we decrement the current alive count. We will then move the respective ptr.
    :param people:
    :return:
    """
    birth_years = get_sorted_birth(people)
    death_years = get_sorted_deaths(people)
    current_alive = 0
    birth_index = 0
    death_index = 0
    max_year = 0
    max_alive = 0

    while birth_index < len(birth_years):
        if birth_years[birth_index] <= death_years[death_index]:
            current_alive += 1
            if current_alive > max_alive:
                max_year = birth_years[birth_index]
                max_alive = current_alive
            birth_index += 1
        else:
            current_alive -= 1
            death_index += 1

    return max_year


def test():
    f = living_people_info
    f2 = living_people_info2
    people = [Person(1908,1909),Person(1906,1920), Person(1950,1990)]
    Assert(f(people),f2, people)
    people = [Person(1912,1950), Person(1920,1990), Person(1910,1998), Person(1901,1972), Person(1923, 1982), Person(1990, 1998)]
    Assert(f(people), f2, people)

if __name__ == '__main__':
    test()