print()
print()
# gets user string input
def edit_distance_alg(word_one, word_two):
    str1 = word_one
    print()

    while not str1:
        print("Please enter string!")
        print()
        str1 = input("Enter string 1: ")
        print()


    str2 = word_two
    print()
    while not str2:
        print("Please enter string!")
        print()
        str2 = input("Enter string 2: ")
        print()






    # initializes 2d array of zeros for matrix output

    twodarray = []

    # I used this array of zeros to keep track of back tracking and visualize.
    back_track_record = []

    for j in range(len(str1) + 1):
        column = []
        for i in range(len(str2) + 1):
            column.append(0)
        twodarray.append(column)

    for j in range(len(str1) + 1):
        column = []
        for i in range(len(str2) + 1):
            column.append(0)
        back_track_record.append(column)


    # creates first row and first column
    for i in range(len(str2) + 1):

        twodarray[0][i] = i

    for k in range(len(str1) + 1):
        twodarray[k][0] = k


    # fills out rest of table

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] != str2[j-1]:
                diagelt = 1
            else:
                diagelt = 0
            twodarray[i][j] = min(twodarray[i - 1][j - 1] + diagelt, twodarray[i - 1][j] + 1, twodarray[i][j - 1] + 1)

    for k in range(len(str1) + 1):
        print(twodarray[k])


    print()

    # prints edit distance using last row last column value
    print(f"The edit distance is: {twodarray[len(str1)][len(str2)]} ")
    distance = twodarray[len(str1)][len(str2)]
    # prints alignment

    align1 = ""
    align2 = ""
    i, j = len(str1), len(str2)
    back_track_record[i][j] = twodarray[i][j]

    # backtrace algorithm


    while (i, j) != (0, 0):
        if i == 0:
            align1 = "_" + align1
            align2 = str2[j - 1] + align2
            j -= 1

        elif j == 0:
            align2 = "_" + align2
            align1 = str1[i - 1] + align1
            i -= 1
        else:

            if str1[i - 1] == str2[j - 1]:
                back_track_record[i - 1][j - 1] = twodarray[i - 1][j - 1]
                align1 = str1[i - 1] + align1
                align2 = str2[j - 1] + align2
                i -= 1
                j -= 1
            elif str1[i - 1] != str2[j - 1]:
                smallest = min(twodarray[i - 1][j - 1], twodarray[i - 1][j], twodarray[i][j - 1] )
                if smallest == twodarray[i - 1][j - 1]:
                    back_track_record[i - 1][j - 1] = twodarray[i - 1][j - 1]
                    align1 = str1[i - 1] + align1
                    align2 = str2[j - 1] + align2

                    i -= 1
                    j -= 1
                elif smallest == twodarray[i - 1][j]:
                    back_track_record[i - 1][j] = twodarray[i - 1][j]

                    align1 = str1[i - 1] + align1
                    align2 = "_" + align2

                    i -= 1
                elif smallest == twodarray[i][j - 1]:
                    back_track_record[i][j -1] = twodarray[i][j - 1]

                    align1 = "_" + align1
                    align2 = str2[j-1] + align2
                    j -= 1


    print()
    print()
    for k in range(len(str1) + 1):
        print(back_track_record[k])

    print()
    print()
    print("Alignment is: ")
    print(align1)
    print(align2)
    print()
    print()

    return align1, align2, distance
