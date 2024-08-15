for _ in range(4):
    dot = list(map(int, input().split()))
    x1, y1, p1, q1, x2, y2, p2, q2 = dot    # 언패킹해서 각각 변수로 할당

    # 각각의 경우를 판단
    if (x1, y1) == (p2, q2) or (x2, y2) == (p1, q1) or (p1, y1) == (x2, q2) or (x1, q1) == (p2, y2):
        # 한 점에서만 만날 경우
        result = 'c'
    elif p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        # 안 만날 경우
        result = 'd'
    elif x1 == p2 or y1 == q2 or q1 == y2 or p1 == x2:
        # 선분으로 만날 경우
        result = 'b'
    else:
        # 그 외의 경우 = 직사각형으로 만날 경우
        result = 'a'

    print(result)