from numpy import *


def create_data_csv(project_name):
    csv_name = project_name + ".csv"
    with open(csv_name, "w"):
        pass


def create_urls_set(url_part_1, n, url_part_2):
    iterator_array_num = arange(n)
    iterator_array_str = iterator_array_num.astype(str)
    url_part_1_array = repeat(url_part_1, n)
    url_part_2_array = repeat(url_part_2, n)
    urls_array = url_part_1_array + iterator_array_str + url_part_2_array
    return urls_array

