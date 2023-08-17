def calculate_bounce_height(initial_height, num_bounces):
    total_distance = initial_height
    bounce_height = initial_height / 2
    
    for _ in range(num_bounces - 1):
        total_distance += bounce_height * 2
        bounce_height /= 2
    
    return total_distance, bounce_height

initial_height = 100
num_bounces = 10

total_distance, bounce_height = calculate_bounce_height(initial_height, num_bounces)

print("在第{}次落地時，總共經歷過了{}公分。".format(num_bounces, total_distance))
print("第{}次的反彈高度為{}公分。".format(num_bounces, bounce_height))