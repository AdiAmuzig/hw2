from pythonFuncs import scan_survey, print_info, clear_survey

if __name__ == '__main__':
    s = scan_survey("survey2")
    print_info(s, 0, "Woman", 10, 30, "Omnivore")
    print_info(s, 1, "Woman", 10, 30, "Omnivore")
    # print_info(s, 2, "Woman", 10, 30, "Omnivore")
    # print_info(s, 3, "Woman", 10, 30, "Omnivore")
    # print_info(s, 4, "Woman", 10, 30, "Omnivore")

    # print_info(s, 0, "Woman", 10, 80, "Vegan")
    clear_survey(s)
