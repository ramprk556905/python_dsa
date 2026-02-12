"""Sample Binary Search implementation.

Run:
	python bst.py
"""

from __future__ import annotations


def binary_search(values: list[int], target: int) -> int:
	left = 0
	right = len(values) - 1

	while left <= right:
		mid = (left + right) // 2
		if values[mid] == target:
			return mid
		if target < values[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return -1


def main() -> None:
	data = [1, 3, 5, 7, 9, 11, 13, 15]
	print("Data:", data)
	print("Find 7:", binary_search(data, 7))
	print("Find 8:", binary_search(data, 8))


if __name__ == "__main__":
	main()
