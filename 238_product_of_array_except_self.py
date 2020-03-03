# -*- coding:utf-8 -*-
from typing import List

__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = []
        cur_product = 1
        for num in nums:
            prefix_products.append(cur_product)
            cur_product *= num
        postfix_products = [0] * len(nums)
        cur_product = 1
        nums_len = len(nums)
        for index, num in enumerate(nums[::-1]):
            prefix_products[nums_len - index - 1] *= cur_product
            cur_product *= num
            # postfix_products[nums_len - index - 1] = cur_product
        # ret = [0]*nums_len
        # for i in range(0, nums_len):
        #     if i == 0:
        #         ret[i] = postfix_products[i+1]
        #     elif i == nums_len-1:
        #         ret[i] = prefix_products[i-1]
        #     else:
        #         ret[i] = prefix_products[i-1] * postfix_products[i+1]
        return prefix_products
