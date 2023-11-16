def count_even_number(number_list):
    
    even_count = 0
     
    for num in number_list:
    
        if num % 2 == 0:
            
            even_count += 1;
    
    return even_count


numbers1 = [1,2,3,4,5,6,7,8,9]
numbers2 = [42,421,52,523,23,23]

print(count_even_number(numbers1))
print(count_even_number(numbers2))