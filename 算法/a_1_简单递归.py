def Fact(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * Fact(n - 1)


print(Fact(4))

from functools import reduce


def fact(n: int) -> int:
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# reduce
# 减少，降低；（烹调中）使变浓稠，收汁；<美>节食减肥；使沦为，使陷入（不好的境地）；迫使，使不得不（做）；（通过破裂、燃烧等）使变成，使化为；归纳，简化
# 将分数约到（最小项）；（使）进行还原反应；减薄（底片或图片）；（语音）弱化；使（脱臼，断骨）复位；<古>攻克，征服（尤指围攻并占领城镇或要塞）
print(fact(4))
