def my_func():
	print("this is a my_func inside mymodule")


if __name__ == '__main__':
	print("ran directly- mymodule")
else:
	print("ran indirectly- mymodule")