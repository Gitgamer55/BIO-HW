def evaluate_expression(s, index=0):
    total = None
    while index < len(s):
        char = s[index]
        if char == '(':
            sub_value, next_index = evaluate_expression(s, index + 1)
            index = next_index
            if total is None: total = sub_value
            else: total = total * sub_value + total + sub_value

        elif char.isdigit():
            val = int(char)
            index += 1
            if total is None: total = val
            else: total = total * val + total + val

        elif char == ')': return total, index + 1
        else: index += 1
            
    return total, index


s = input()
result, temp = evaluate_expression(s)
print(result)
