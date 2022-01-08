def insertion_sort_inplace(LIST):
    # Traverse through 1 to len(LIST)
    for i in range(1, len(LIST)):

        key = LIST[i]

        # Move elements of LIST[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < LIST[j] :
                LIST[j+1] = LIST[j]
                j -= 1
        LIST[j+1] = key


# Driver code to test above
if __name__ == "__main__":
    LIST = [12, 11, 13, 5, 6]
    
    insertion_sort_inplace(LIST)
    print(LIST)


#################################################################
#################################################################
#################################################################

def insertion_sort(LIST):
    TEMP = LIST.copy()  #or  TEMP = LIST[:]

    for i in range(1, len(TEMP)):
        key = TEMP[i]

        j = i-1
        while j >=0 and key < TEMP[j] :
                TEMP[j+1] = TEMP[j]
                j -= 1
        TEMP[j+1] = key

    return TEMP


# Driver code to test above
if __name__ == "__main__":
    LIST = [12, 11, 13, 5, 6]

    ans = insertion_sort(LIST)
    print(LIST, " --> ", ans)

