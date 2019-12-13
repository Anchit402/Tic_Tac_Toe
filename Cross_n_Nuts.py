d = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
i = 1
c = 0
l = []
k = 0
c1 = 0
c2 = 0
print(1, '|', 2, '|', 3)
print('_', '|', '_', '|', '_')
print(4, '|', 5, '|', 6)
print('_', '|', '_', '|', '_')
print(7, '|', 8, '|', 9)
print('Enter positions as per given diagram')
while True:
    if i % 2 == 1:
        print("x's turn")
        value = 'x'
    else:
        print("o's turn")
        value = 'o'
    try:
        l.append(int(input('Enter position: ')))
        k += 1
        while True:
            if l[k - 1] < 1 or l[k - 1] > 9 or l.count(l[k - 1]) > 1 or l[k-1] == '' :
                if l[k - 1] < 1 or l[k - 1] > 9:
                    print('Enter a no b/w 1 and 9 only') 
                elif l.count(l[k - 1]) > 1:
                    print('Already entered')
                else:
                    print('Enter a non-null value')
                del l[k - 1]
                l.append(int(input('Enter a new position: ')))
            else:
                c1+=1
                break
        d[l[k - 1]] = value
    except ValueError:
        print('Enter an integer and non-null value only')
        i-=1
    except IndexError:
        k-=1
    print('List of positions is:',l)
    print(d[1], '|', d[2], '|', d[3])
    print('_', '|', '_', '|', '_')
    print(d[4], '|', d[5], '|', d[6])
    print('_', '|', '_', '|', '_')
    print(d[7], '|', d[8], '|', d[9])
    if d[1] != ' ' and d[2] != ' ' and d[3] != ' ' and d[1] == d[2] and d[2] == d[3]:
        c = 1
        win = value
        break
    elif d[4] != ' ' and d[5] != ' ' and d[6] != ' ' and d[4] == d[5] and d[5] == d[6]:
        c = 1
        win = value
        break
    elif d[7] != ' ' and d[8] != ' ' and d[9] != ' ' and d[7] == d[8] and d[8] == d[9]:
        c = 1
        win = value
        break
    elif d[1] != ' ' and d[4] != ' ' and d[7] != ' ' and d[1] == d[4] and d[4] == d[7]:
        c = 1
        win = value
        break
    elif d[2] != ' ' and d[5] != ' ' and d[8] != ' ' and d[2] == d[5] and d[5] == d[8]:
        c = 1
        win = value
        break
    elif d[3] != ' ' and d[6] != ' ' and d[9] != ' ' and d[3] == d[6] and d[6] == d[9]:
        c = 1
        win = value
        break
    elif d[1] != ' ' and d[5] != ' ' and d[9] != ' ' and d[1] == d[5] and d[5] == d[9]:
        c = 1
        win = value
        break
    elif d[3] != ' ' and d[5] != ' ' and d[7] != ' ' and d[3] == d[5] and d[5] == d[7]:
        c = 1
        win = value
        break
    i = i + 1
    if c1 == 9:
        break

if c == 1:
    print(win, ' wins the game.')
else:
    print("It's a draw.")
