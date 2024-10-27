def palin(drom):
    prwyalebi = ""
    for char in drom:
        if char.isalnum():
            prwyalebi += char.lower()
    
    shebrunebuli = prwyalebi[::-1]
    
    return prwyalebi == shebrunebuli


result = palin("nika")
print(result)  