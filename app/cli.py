from argparse import ArgumentParser


def main():
    parser = ArgumentParser(prog='cli')
    parser.add_argument('name', help="The user's name.")
    args = parser.parse_args()
    print("Hello, %s!" % args.name)


if __name__ == '__main__':
    main()
