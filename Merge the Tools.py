def merge_the_tools(string, k):
    # your code goes here
    i = 0
    t = 1
    l = []
    while i != len(string) and t <= len(string)//k:
        wrd = ''
        for j in range(k):
            wrd = wrd+string[i]
            i = i+1
        l.append(wrd)
    
        t = t+1
    
    for i in l:
        print(''.join(sorted(set(i), key=i.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
