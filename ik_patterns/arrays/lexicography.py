def solution(s, t):
    s_new_str = ''
    count = 0
    for i in range(len(s)):
        if s[i].isdigit():
            # s_new_str += s[i]
            if s_new_str + s[i+1:] < t:
                count += 1
            
        s_new_str += s[i]
                
                
                
    t_new_str = ''
    for j in range(len(t)):
        if t[j].isdigit():
            if s < t_new_str + t[j+1:]:
                count += 1
                
        t_new_str += t[j] 
        
        
    return count

print(solution("ab12c", "ab24z"))
            