import logging

from src import create_app


app = create_app()

if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=8000)


# def main():
#     app.run(port=int(os.environ.get("PORT", 80)))


# if __name__ == "__main__":
#     main()
