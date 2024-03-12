def check_balance():
    deque = []

    with open('balance.txt', 'r') as file:
        for line in file:
            for i in line:
                if i == '[':
                    deque.append(i)
                elif i == ']':
                    if not deque:
                        return False
                    deque.pop()#если дек не пуст, удаляет последний элемент из дека

    if not deque:
        return True#если дек пуст, возвращает `True`, что означает, что скобки сбалансированы.
    else:
        return False


if check_balance():
    print("Квадратные скобки сбалансированы")
else:
    print("Квадратные скобки не сбалансированы")