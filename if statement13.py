is_beautiful=False
is_kind=False

if is_beautiful and is_kind:
    print("you are both beautiful and kind")
elif is_beautiful and not(is_kind):#not is used
    print("you are beautiful but not kind!")
elif not(is_beautiful) and is_kind:
    print("you are kind")
else :
    print("you are neither beautiful or kind to exist")


rainy=False
sunny=True

if rainy or sunny:
    print("its either sunny or rainy")