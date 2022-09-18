from typing import *
import collections
import itertools
import bisect
import math
import re
import copy


# DPテーブル：dp[s1s2s3]: 末尾3文字がs1s2s3であるような文字列の数
# 問題に書かれている条件は、1) 末尾3文字が「AGC, ACG, GAC」でない 2) 末尾4文字が「A?GC, AG?C」でない
# の両方を満たすのと同義である。
# 前者は愚直な照合で、後者は正規表現を用いて判定できる。
#
# c = {A, C, G, T}に対して、連結した文字列s1s2s3cが上記の条件をクリアしていれば、末尾にcを追加しても
# よいことになる。従って、dp[s2s3c] += dp[s1s2s3]で遷移できる。この遷移をN回繰り返す。
# 遷移のステップを行う度にDPテーブルを新しく作り直している。これは辞書のイテレーション中に要素数を増やさないため。
#
# 遷移が終了した時点で、「末尾3文字がSであるような文字列の場合の数」が全てのSについてDPテーブルに記録されているので、
# それらを全て足し合わせる。
# #は何もない文字列を表している。##AはAだけの文字列を表しているので、計算に支障は無い。


def main():
    N: int = int(input())
    mod: int = 1000000007

    pattern = re.compile(r"A.GC|AG.C")

    dp1 = collections.Counter({"###": 1})
    for i in range(N):
        dp2 = collections.Counter()
        for key, value in dp1.items():
            for c in "AGCT":
                S: str = key + c
                if (S[1:] not in ["AGC", "GAC", "ACG"]) and not re.search(pattern, S):
                    dp2[S[1:]] += dp1[key]
                    dp2[S[1:]] %= mod

        dp1 = copy.copy(dp2)

    answer: int = 0
    for key, value in dp1.items():
        answer += value
    print(answer % mod)


if __name__ == "__main__":
    main()
