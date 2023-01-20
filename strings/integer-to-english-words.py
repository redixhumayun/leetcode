class Solution:
    def numberToWords(self, num: int) -> str:
        def get_last_n_digits(num, n, count):
            return_list = []
            number_of_digits = 0
            while n > 0 and num > 0:
                digit = num % 10
                # return_number += digit * count
                return_list.append(digit)
                num = num // 10
                number_of_digits += 1
                count = count * 10
            return_list.reverse()
            return (num, return_list, count // 10, number_of_digits)

        def find_number_of_digits(num):
            count = 0
            while num > 0:
                digit = num % 10
                num = num // 10
                count += 1
            return count

        hash_map = {
            1: ['One', 'Ten'],
            2: ['Two', 'Twenty'],
            3: ['Three', 'Thirty'],
            4: ['Four', 'Forty'],
            5: ['Five', 'Fifty'],
            6: ['Six', 'Sixty'],
            7: ['Seven', 'Seventy'],
            8: ['Eight', 'Eighty'],
            9: ['Nine', 'Ninety'],
            10: ['Ten', 'One Hundred'],
            11: ['Eleven'],
            12: ['Twelve'],
            13: ['Thirteen'],
            14: ['Fourteen'],
            15: ['Fifteen'],
            16: ['Sixteen'],
            17: ['Seventeen'],
            18: ['Eighteen'],
            19: ['Nineteen']
        }

        def recursively_create_string(count, num):
            if count == 0 or len(num) == 0:
                return ""
            if count == 1:
                string = hash_map[num[0]][0]
                return string
            if count == 10:
                string = hash_map[num[0]][1]
                return string + " " + recursively_create_string(count // 10, num[1:])
            if count == 100:
                string = hash_map[num[0]][0]
                return string + " Hundred " + recursively_create_string(count // 10, num[1:])
            if count == 1000:
                string = hash_map[num[0]][0]
                return string + " Thousand " + recursively_create_string(count // 10, num[1:])
            if count == 10000:
                joined_number = num[0] * 10 + num[1]
                string = hash_map[joined_number][0]
                return string + " Thousand " + recursively_create_string(count // 100, num[2:])
            if count == 100000:
                joined_number = num[0] * 100 + num[1] * 10 + num[0]
                string = hash_map[joined_number][0]
                return string + " Thousand " + recursively_create_string(count // 100, num[2:])
        
        count = 1
        number_of_digits = 0
        return_string = ""
        while num > 0:
            (num, ret_num, count, number_of_digits) = get_last_n_digits(num, 3, count)
            print(num, ret_num, count, number_of_digits)
            return_string = recursively_create_string(count, ret_num)
            # if count == 1:
            #     string = hash_map[ret_num[0]][0]
            #     return_string = string + return_string
            # if count == 10:
            #     string = hash_map[ret_num[0]][1] + " " + hash_map[ret_num[1]][0]
            #     return_string = string + return_string
            # if count == 100:
            #     string = hash_map[ret_num[0]][0] + " Hundred " + hash_map[ret_num[1]][1] + " " + hash_map[ret_num[2]][0]
            #     return_string = string + return_string
            # if count == 1000:
            #     string = hash_map[ret_num[0]][0] + " Thousand " + hash_map[ret_num[1]][0] + " Hundred " + hash_map[ret_num[2]][1] + " " + hash_map[ret_num[3]][0]
            #     return_string = string + return_string
        return return_string

if __name__ == '__main__':
    print(Solution().numberToWords(111123))
    # print(Solution().numberToWords(12345))
    # print(Solution().numberToWords(1234567))
    # print(Solution().numberToWords(1234567891))