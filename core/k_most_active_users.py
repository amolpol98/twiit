from operator import itemgetter

if __name__ == '__main__':
    K = 3
    users = []
    users_dict = {}

    with open('chats.txt') as fp:
        for line in fp:
            user_name = line.split(' ')[0]
            users.append(user_name[user_name.find("<")+1:user_name.find(">")])

    for user in users:
        users_dict[user] = users_dict.get(user, 0) + 1

    top_users = sorted(users_dict.iteritems(), key=itemgetter(1), reverse=True)[:K]

    for user, frequency in top_users:
        print("%s: %d" % (user, frequency))
