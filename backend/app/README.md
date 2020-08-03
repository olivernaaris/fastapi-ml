# Deploying and Hosting a Machine Learning Model with FastAPI and Heroku

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/fastapi-machine-learning).

## Want to use this project?

1. Install the requirements:

    ```sh
       poetry install
    ```

2. Spawn shell with virtual environment:

    ```sh
       poetry shell
    ```

3. Train the model:

    ```sh
    (venv)$ python

    >>> from app.machine_learning.model import convert, PredictStocks
    >>> obj = PredictStocks()
    >>> obj.train()
    >>> obj.train("GOOG")
    >>> obj.train("AAPL")
    >>> obj.train("^GSPC")
    >>> prediction_list = obj.result
    >>> convert(prediction_list)
    ```

4. Run the app:

    ```sh
    (venv)$ uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
    ```

5. Test:

    ```sh
    $ curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"ticker":"MSFT"}' \
      http://localhost:8000/api/predict
    ```

6. Check API docs
    http://localhost:8000/docs#/

7. Check if service heartbeat is working
    ```sh
   $ curl http://localhost:8000/api/heartbeat
   ```