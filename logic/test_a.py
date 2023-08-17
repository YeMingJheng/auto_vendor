def calculate_new_score(original_score):
    if original_score < 40:
        return original_score
    
    next_multiple_of_5 = (original_score // 5 + 1) * 5
    if next_multiple_of_5 - original_score <= 3:
        return next_multiple_of_5
    else:
        return original_score

original_scores = [33, 73, 63, 39]
new_scores = [calculate_new_score(score) for score in original_scores]
total_score = sum(new_scores)

print("原分數:", original_scores)
print("換算後的分數:", new_scores)
print("總分數:", total_score)