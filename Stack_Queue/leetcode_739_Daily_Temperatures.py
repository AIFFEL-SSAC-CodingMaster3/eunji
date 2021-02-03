"""
leetcode 739. Daily Temperatures
문제링크 https://leetcode.com/problems/daily-temperatures/

매일의 화씨온도 리스트 T를 입력받아, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
만약 더 따뜻한 날씨가 오지 않는다면 0을 대신 넣는다.
"""
from typing import List

"""
코드 1. 이중 for문
Time Limit Exceeded
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = []
        for i in range(len(T)):
            check = True
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    result.append(j-i)
                    check = False
                    break
            if check:
                result.append(0)
        return result


"""
코드 2.
Runtime: 508 ms
Memory Usage: 18.7 MB
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []

        for i, val in enumerate(T):

            while stack and val > T[stack[-1]]:
                last = stack.pop()
                result[last] = i - last

            stack.append(i)

        return result

"""
다른 사람 코드.

float('inf') : 양의 무한대(다른 모든 수보다 큰 수를 표현해야 할 때 사용)
float('-inf') : 음의 무한대(다른 모든 수보다 작은 수를 표현해야 할 때 사용)
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n, right_max = len(T), float('-inf')
        res = [0] * n

        for i in range(n - 1, -1, -1):  # T의 끝에서부터 찾음.
            t = T[i]
            if right_max <= t:
                right_max = t
            else:
                days = 1
                while T[i + days] <= t:
                    days += res[i + days]
                res[i] = days

        return res