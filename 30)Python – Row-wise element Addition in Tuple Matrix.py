test_list = [[('manoj', 3), ('is', 3)], [('best', 1)], [('for', 5), ('gaming', 1)]]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing Custom eles
cus_eles = [6, 7, 8]
  
# Row-wise element Addition in Tuple Matrix
# Using enumerate() + list comprehension
res = [[sub + (cus_eles[idx], ) for sub in val] for idx, val in enumerate(test_list)]
  
# printing result 
print("The matrix after row elements addition : " + str(res)) 
