# シンプルな計算機プログラム

# 1つ目の数値を入力させる
try:
    num1 = float(input("1つ目の数値を入力してください: "))
    num2 = float(input("2つ目の数値を入力してください: "))
except ValueError:
    # 数値以外が入力された場合
    print("無効な入力です。数値を入力してください。")
else:
    # 演算子を入力させる
    operator = input("演算子を入力してください（+ - * /）: ")

    # 演算子に応じて計算する
    if operator == "+":
        print("計算結果:", num1 + num2)
    elif operator == "-":
        print("計算結果:", num1 - num2)
    elif operator == "*":
        print("計算結果:", num1 * num2)
    elif operator == "/":
        # 0で割る場合のエラー処理
        if num2 == 0:
            print("エラー：0で割ることはできません。")
        else:
            print("計算結果:", num1 / num2)
    else:
        # サポートされていない演算子の場合
        print("エラー：サポートされていない演算子です。")
