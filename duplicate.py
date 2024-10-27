#  Remove Duplicates from a List
def mechqareba(dzalian):
    result = []
    for i in dzalian[::-1]:
        if i not in result:
            result.append(i)
    return result[::-1]

print(mechqareba(["andria","andria",1,1,1]))