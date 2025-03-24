def select_top_users_by_rate(users, top_size):
    sorted_users = sorted(users, key=lambda user: user.rate, reverse=True)
    ans = []
    for i in range(top_size):
        ans.append(sorted_users[i])
    return ans
