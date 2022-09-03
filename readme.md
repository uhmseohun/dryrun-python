# Dryrun-Python
Dryrun-Python makes it very easy to run a python program without actual i/o operations.
It can help you to fully focus on your business-logic without worrying about the i/o operation.

## Key features
- It supports async functions.
- You can specify a return value.
- Or, you can use mock function which is called instead of original function.

## How to install
```
pip install dryrun
```

```python
from dryrun import dryrun
```

## How to use
Just import dryrun and use it as a decorator.
```python
@dryrun()
async def delete_comment(comment_id: str) -> bool:
    response = await api_client.delete_comment(comment_id)
    return response.success
```
If dryrun is enabled, the real function won't be called.

And If you want to specify a return value, you can use `return_value` argument.
```python
@dryrun(return_value=True)
async def delete_comment(comment_id: str) -> bool:
    response = await api_client.delete_comment(comment_id)
    return response.success
```

But it's not enough for some cases. Then, you can use mock function which is called instead of the real function.  
Just like it!
```python
@dryrun()
async def create_comment(payload: dict) -> dict:
    response = await api_client.create_comment(payload)
    return response.paylaod

@create_comment.mock
def create_comment_mock(payload: dict) -> dict:
    return {
        "id": uuid.uuid4(),
        "content": payload["content"],
    }
```
