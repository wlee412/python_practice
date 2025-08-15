def calculate_love_score(name1, name2):
    name1_list = list(name1.upper())
    name2_list = list(name2.upper())
    
    merged_list = name1_list + name2_list 
    
    true_list = ["T","R","U","E"]
    true_total = 0
    for count_name in range(len(merged_list)):
        for count_true in range(len(true_list)):
            if merged_list[count_name] == true_list[count_true]:
                true_total += 1
    
    love_list = ["L","O","V","E"]
    love_total = 0
    for count_name in range(len(merged_list)):
        for count_love in range(len(love_list)):
            if merged_list[count_name] == love_list[count_love]:
                love_total += 1
    
    
    love_score = str(true_total) + str(love_total)
    
    print(love_score)
    
            
    
    