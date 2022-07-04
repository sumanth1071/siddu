# -----------------------------
# if __name__ == "__main__"
# -----------------------------


# why thought ?
# 1.Module can be run as a standalone program
 # or
# 2.Module can be imported and used by another modules

# Python interpreter sets "special vaiable", one of which is __name__
# Python will assign the __name__ varibale "__main__" if it's
# the initial module is being run


# import module_two
# print(__name__)
# print(module_two.__name__)

def main():
	print("hello!")


if __name__ == "__main__":
	main()



if __name__ == "__main__":
	print("running directly")
else:
	print("running indirectly")