from app import my_app


def main(*args):
    my_app.run(host="web", debug=False)


if __name__ == "__main__":
    main()
