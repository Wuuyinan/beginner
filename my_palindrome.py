def harder_palindrome(word):
    for i in range(len(word)//2):
        if word[i] == word[-i-1]:
            pass
        else:
            return False
    return True

def my_run():
    print("*"*8+"回文检测程序" + "*"*18)
    print("请输入单词来检测回文，可以带空格\n")

    user_input = input(">>请输入：")

    clean_word = user_input.replace(" ","")
    clean_word = clean_word.lower()

    result = harder_palindrome(clean_word)

    if result:
        print("是回文")
    else:
        print("不是回文")

    again = input("还要继续玩吗？(y/n): ")
    if len(again) > 0 and again.lower()[0] == "y":
        my_run()
    else:
        print("程序结束，再见")

my_run()
