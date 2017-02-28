from sstack import SStack


def suffix_exp_evaluation(line):
    exp = line.split(' ')
    operators = '+-*/'
    st = SStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue

        if st.depth() < 2:
            raise SyntaxError('操作数错误！')
        b = st.pop()
        a = st.pop()

        if x == '+':
            c = a + b
        elif x == '-':
            c = a - b
        elif x == '*':
            c = a * b
        elif x == '/':
            c = a / b

        st.push(c)

    if st.depth() != 1:
        raise SyntaxError("操作数错误")
    else:
        return st.pop()

#------------------------------------------
if __name__ == "__main__":

    print("Start testing.")
    print(suffix_exp_evaluation('3 5 - 6 17 4 * + * 3 /'))