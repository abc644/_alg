# 由chatgpt生成
# 方法 3：用遞迴+查表
def power2n_d(n, memo={}):
    if n in memo:  # 檢查是否已經計算過
        return memo[n]
    if n == 0:  # 基底條件
        memo[n] = 1
    else:
        memo[n] = 2 * power2n_d(n - 1, memo)  # 計算並存入查表
    return memo[n]

# 測試
for i in range(10):
    print(f"2^{i} = {power2n_d(i)}")
