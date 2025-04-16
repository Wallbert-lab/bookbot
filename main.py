import sys
from stats import word_count, letter_count, sort_on, sys_test

system_arguments = sys.argv



def main():
    sys_test(system_arguments)
    w_count = word_count()
    sort_alg = sort_on(letter_count(system_arguments[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {system_arguments[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    for i in range(len(sort_alg)):
        print(f"{sort_alg[i]['char']}: {sort_alg[i]['num']}")
    print("============= END ===============")

try:
    sys_test(system_arguments)
    main()
except Exception as e:
    print(e)
    sys.exit(1)