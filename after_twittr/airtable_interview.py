

def my_data():
    return [
        ["header1", "header2", "header3", "header4", "header5"],
        ["text1"  ,  ""      , "tx"     , "us"     ,  "2"      ],
        ["tex2"   ,  "what?" , "mo"     , "mx"     ,  ""       ],
        ["text4"  ,  "now"   , ""       , "mx"     ,  ""       ],
        # ["text4"  ,  "now"   , ""       , "mx"     ,  "hi"     ],
        # ["text4"  ,  "now"   , ""       , "mx"     ,  "3"      ],
    ]


def guess_colum_types(data):
    result = []
    for k in  range(len(data[0])):
        result.append("X")

    for i in range(1, len(data)):
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                if result[j] != 'TEXT':
                    result[j] = "INTEGER"

            elif data[i][j] != "" and isinstance(data[i][j], str):
                    result[j] = "TEXT"

            # if data[i][j] == "":
            #      continue

    return result

data = my_data()
print(guess_colum_types(data))