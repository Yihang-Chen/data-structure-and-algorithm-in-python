# 括号匹配问题
from sstack import SStack

parens = '()[]{}'
open_parens = '([{'
opposite = {')': '(', ']': '[', '}': '{'}


def parentheses(text):
    for i in range(0, len(text)):
        if text[i] in parens:
            yield text[i], i


def check_parens(text):
    st = SStack()
    for elem, i in parentheses(text):
        if elem in open_parens:
            st.push(elem)
        elif st.is_empty():
            print("Unmatching found at:", i, "for", elem)
        elif st.pop() != opposite[elem]:
            print("Unmatching found at:", i, "for", elem)
        else:
            pass
    if not st.is_empty():
        print("Unmatching at end!")
    else:
        print("Matching!")


#------------------------------------------
if __name__ == "__main__":

    print("Start testing.")

    # # *************************
    # # test parentheses()
    # # *************************
    # for x in parentheses("asd"):
    #     print(x)
    # for x in parentheses("{[]123[])"):
    #     print(x)
    # for x in parentheses("asd()asdf]"):
    #     print(x)


    # # *************************
    # # test check_parens()
    # # *************************
    #check_parens("asdfsafg")
    #check_parens("[asdfsafg")
    #check_parens("asdfs]afg")
    #check_parens("[asdfsa)fg")
    check_parens("[as{d(fs)af]g")


