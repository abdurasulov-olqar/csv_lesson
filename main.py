def get_column(data):
    column_name = []
    s = data.split('\n')
    
    for i in s[1:]:
        l = i.split(',') 
        column_name.append(l[-1])
    
    return column_name

data = open('data.csv').read()
print(get_column(data))
