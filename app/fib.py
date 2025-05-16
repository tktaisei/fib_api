from functools import lru_cache

@lru_cache(maxsize=10_000)
def fibonacci(n: int) -> int:
    """n 番目のフィボナッチ数を返す（1 始まり）。  
    lru_cache でメモ化→ 1 行で高速 & テストも書きやすい。"""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
