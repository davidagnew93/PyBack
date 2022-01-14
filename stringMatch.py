string = 'ABCDCDC'
sub_string='CDC'


def count_substring(string, sub_string):
    length = len(sub_string)
    count = 0

    for i in range(len(string)):
        chunck = str(string[i:i+length])
        print(count)
        print(chunck)
        print(sub_string)
        if sub_string == chunck:
            count=+1
            
    return count

print(count_substring(string, sub_string))
