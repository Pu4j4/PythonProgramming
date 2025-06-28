# if __name__ == '__main__'

# why?
#1. module can be run as a standalone program
#2. module can be imported and used by other modules

# python interpreter sets "special variables", one of which is __name--
# then python will execute the code found within __main__
# python will assign the __name__ variable a value of '__main__'
# if it's the initial module being run


def main():
    print("Hello")

if __name__ == '__main__':
    main()
#     print("running this module directly")
# else:
#     print("running another module indirectly")