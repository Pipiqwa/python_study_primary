while True:
    num_list = []
    num_list.append(input().split())
    if num_list[0] == 0:
        break

    print(sum(num_list[1:]))

