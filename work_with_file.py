

def finder_password(passwd):
    """ function search password in popular password """
    input_file = "passwd.txt"  # file with popular password
    output_file = "search_password.txt"  # file for save founded password
    password_file = open(input_file, mode='r', encoding='latin_1')
    output_file = open(output_file, mode='a', encoding='latin_1')
    for num, line in enumerate(password_file):
        if passwd in line:
            print("line number  " + str(num) + " " + line.strip())
            output_file.write("found password :" + line)
    print("Result will be save in search_password.txt file")

    password_file.close()
    output_file.close()


print("Input searching password")
finder_password(input())
