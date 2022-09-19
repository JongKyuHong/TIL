def solution(n, words):
    answer = []
    ans = 1
    last = words[0][-1]
    words_list = [words[0]]
    for word in words[1:]:
        ans += 1
        if word not in words_list:
            if last == word[0]:
                words_list.append(word)
                last = word[-1]
            elif last != word[0]:
                l = ans%n
                if l == 0:
                    l = n
                r = 0
                if ans % n == 0:
                    r = ans//n
                else:
                    r = ans//n + 1
                return [l, r]
        else:
            l = ans%n
            if l == 0:
                l = n
            r = 0
            if ans % n == 0:
                r = ans//n
            else:
                r = ans//n + 1
            return [l, r]
    return [0 ,0]