# Deploying and Hosting a Machine Learning Model with FastAPI and Heroku

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/fastapi-machine-learning).

## Want to use this project?

1. Install the requirements:

    ```sh
       poetry install
    ```

1. Spawn shell with virtual environment:

    ```sh
       poetry shell
    ```

1. Train the model:

    ```sh
    (venv)$ python

    >>> from model import train, predict, convert
    >>> train()
    >>> train("GOOG")
    >>> train("AAPL")
    >>> train("^GSPC")
    ```

1. Run the app:

    ```sh
    (venv)$ uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
    ```

1. Test:

    ```sh
    $ curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"ticker":"MSFT"}' \
      http://localhost:8000/predict
    ```
