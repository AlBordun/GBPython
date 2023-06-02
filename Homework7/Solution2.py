# Задача 36:
def print_operation_table(res,num_rows=6, num_columns=6):
    print('\n'.join(['\t'.join([str(res(i,y))for y in range(1,num_columns + 1)])for i in range(1,num_rows + 1)]))
res = lambda x,y: x*y
print_operation_table(res,6,6)  