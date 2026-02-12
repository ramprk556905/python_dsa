"""Simple iterator example.

Run:
	python iterator.py
"""


def main() -> None:
	items = [10, 20, 30]
	print("Items:", items)

	# Create an iterator from the list
	it = iter(items)
	print("First:", next(it))
	print("Second:", next(it))
	print("Third:", next(it))

	print("\nUsing a for loop:")
	for value in items:
		print(value)


if __name__ == "__main__":
	main()
