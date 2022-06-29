test_tup = (10,20,30,40,5,6,7)
 
print("The original tuple is : " + str(test_tup))
 
# initializing K
K = 2
 
# Maximum and Minimum K elements in Tuple
# Using sorted() + loop
res = []
test_tup = list(sorted(test_tup))
 
for idx, val in enumerate(test_tup):
    if idx < K or idx >= len(test_tup) - K:
        res.append(val)
res = tuple(res)
 
# printing result
print("The extracted values : " + str(res))