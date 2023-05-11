# use stack

"""
true and false or true
false and true or false
not false and true
false or false and true and false or false
true or not false not
false or true and not true
"""

def bool_operation(op, val, item):
    op_item = op.pop()
    val_item = val.pop()
    if op_item == 'and':
        val.append(val_item and item)
    else:
        res = val_item or item
        if val_item == True:  # 短路操作，但还需要判断后面是否有语法错误
            final = True  # 所以无法直接return
        val.append(res)


def main():
    s = input().split()
    final = 0
    val = []
    op = []
    for item in s:  # loop through expression
        if item in ['true', 'false']:   # deal with "true false"
            item = (item == 'true')

            # deal with not
            if len(val) > 0 and val[-1] == -1:
                item = not item
                val.pop()

            if len(val) == 0:   # push the first value
                val.append(item)
                continue

            if len(op) == 0:  # no op
                print('error')
                return
            bool_operation(op, val, item)

        elif item in ['and', 'or']:  # deal with "and or"
            # not allow "and and"
            # val stack should not be empty
            # val stack should not end with "not"
            if len(op) >= 1 \
                    or len(val) == 0 \
                    or (len(val)>0 and val[-1] == -1):
                print('error')
                return
            op.append(item)

        else:   # deal with "not not"
            if len(val)>0 and val[-1] == -1:
                val.pop()
            else:
                val.append(-1)

    # op stack should be empty
    if len(op) > 0 or len(val) == 0:
        print('error')
        return

    # val stack should not end with "not"
    if val[-1] == -1:
        print('error')
        return

    # true or xxx shortcircuit
    if final == True:
        print('true')
        return

    if val[-1] == True:
        print('true')
    else:
        print('false')

main()