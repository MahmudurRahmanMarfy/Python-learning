list = []
with open('Que_loop.txt', 'r') as rf:
    for line in rf:
        list.append(line)
    # print(list)

count = 1
for que in list:
    # print(que)
    # "#include<stdio.h>\nint main()\n{\n\n\n\treturn 0;\n}\n"
    str = "# " + que + "\n"
    file_name = f'problem_{count}.py'
    print(file_name)
    count += 1

    with open(file_name, 'w') as file:
        file.write(str)