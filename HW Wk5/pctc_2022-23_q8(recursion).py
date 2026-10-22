def decrypt_cipher(s, index=0):
    current_digits = []
    results = []
    while index < len(s):
        char = s[index]
        if char == '[':
            sub_results, next_index = decrypt_cipher(s, index + 1)
            results.extend(sub_results)
            index = next_index
            
        elif char.isdigit():
            current_digits.append(int(char))
            index += 1
            
        elif char == ']':
            if current_digits:
                first = current_digits[0]
                last = current_digits[-1]
                avg = (first + last) // 2
                results.append(str(avg))
            return results, index + 1
            
        else: index += 1
            
    return results, index


s = input()
final_decrypted_number, _ = decrypt_cipher(s)
print("".join(final_decrypted_number))
