def filter_comments_by_author(comments, author):
    ans = []
    for comment in comments:
        if comment.author_id == author.id:
            ans.append(comment)
    return ans
