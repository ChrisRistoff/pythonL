def string_to_num(string_num):
    num_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,
                "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, 
                "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, 
                "sixty":60, "seventy":70, "eighty":80, "ninety":90, "hundred":100, "thousand":1000}

    num_list = string_num.split()

    if len(num_list) == 1:
        return num_dict[num_list[0]]

    else:
        total_num = 0
        temp_num = 0

        for word in num_list:
            if word == "hundred":
                temp_num *= num_dict[word]
            elif word == "thousand":
                total_num += temp_num * num_dict[word]
                temp_num = 0
            else:
                temp_num += num_dict[word]

        total_num += temp_num

        return total_num


string_num = "seventy seven thousand three hundred fifty two"
numeric_num = string_to_num(string_num)
print(numeric_num)
