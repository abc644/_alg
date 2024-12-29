#由chatgpt生成
def halt(f, input):
    """
    判斷函數 f 是否對給定輸入 input 會執行完成
    （實際上，這無法在所有情況下準確判斷，這裡只是模擬一個範例）。
    """
    try:
        f(input)  # 嘗試執行函數
        return True  # 若執行完成，返回 True
    except:
        return False  # 若執行中出現錯誤或無法完成，返回 False

def f1(n):
    return n * n  # 一個簡單的可終止函數

def f2(n):
    s = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                for _ in range(n):
                    s = s + 1  # 計算量非常大的函數

# 測試
if __name__ == "__main__":
    print("halt(f1, 3) =", halt(f1, 3))
    print("halt(f2, 10) =", halt(f2, 10))
    print("halt(f2, 1000) =", halt(f2, 1000))
