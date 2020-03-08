

def compare_version(v1, v2):
    """
    比较两个version版本的大小
    params: v1 string
    parmas: v2 string
    return: 1/-1/0 int
    """
    v1 = [int(i) for i in v1.split(".")]
    v2 = [int(j) for j in v2.split(".")]
    max_v = max([len(v1), len(v2)])
    for k in range(min([len(v1), len(v2)])):
        if v1[k] > v2[k]:
            return 1
        if v1[k] < v2[k]:
            return -1

    if len(v1) > len(v2):
        indeed = v1[len(v2)-1:]
        for i in indeed:
            if i > 0:
                return 1
    elif len(v1) < len(v2):
        indeed = v2[len(v1)-1:]
        for i in indeed:
            if i > 0:
                return -1
    return 0

print(compare_version("0.1", "1.1"))
print(compare_version("1.0.1", "1"))
print(compare_version("7.5.2.4", "7.5.3"))
print(compare_version("1.01", "1.001"))
print(compare_version("1.0", "1.0.0"))
