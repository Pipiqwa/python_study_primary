while True:
    num_list = []
    num_list.append(input().split())
    if num_list[0] == 0:
        break

    print(sum(num_list[1:]))

'''The authenticity of host 'github.com (20.205.243.166)' can't be established. ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU. This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])?'''