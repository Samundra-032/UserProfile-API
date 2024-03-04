# Flask App

### run app in debug mode

```python
    if __name__ == "__main__":
        app.run(debug=True)
```

```python
    $env:FLASK_ENV="devlopment"
    flask run
```

```python
    flask --app app run --debug
```

### not to create pylance folder

```python
    $env:PYTHONDONTWRITEBYTECODE=1
```
