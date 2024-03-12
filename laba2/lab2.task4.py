def check_balance():
    stack = []

    with open('balance.txt', 'r') as file:
        for line in file:
            for i in line:
                if i == '(':
                    stack.append(i)
                elif i == ')':
                    if not stack:
                        return False
                    stack.pop()#если cтек не пуст, удаляет последний элемент из стека

    if not stack:
        return True
    else:
        return False


if check_balance():
    print("Скобки сбалансированы")
else:
    print("Скобки не сбалансированы")