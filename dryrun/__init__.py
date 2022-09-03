import asyncio
import functools
from typing import Any, Callable


class Dryrun:
    _dryrun = False

    def __init__(
        self,
        return_value: Any = None,
    ):
        self.return_value = return_value
        self.mock_function = None

    def __call__(self, function: Callable) -> Callable:
        @functools.wraps(function)
        def sync_decorator(*args, **kwargs) -> Any:
            if not self._dryrun:
                return function(*args, **kwargs)
            elif self.mock_function:
                return self.mock_function(*args, **kwargs)
            else:
                return self.return_value

        @functools.wraps(function)
        async def async_decorator(*args, **kwargs) -> Any:
            if not self._dryrun:
                return await function(*args, **kwargs)
            elif self.mock_function:
                if asyncio.iscoroutinefunction(self.mock_function):
                    return await self.mock_function(*args, **kwargs)
                else:
                    return self.mock_function(*args, **kwargs)
            else:
                return self.return_value

        def set_mock_function(mock_function: Callable):
            self.mock_function = mock_function

        if asyncio.iscoroutinefunction(function):
            decorator = async_decorator
        else:
            decorator = sync_decorator

        decorator.mock = set_mock_function
        return decorator

    @classmethod
    def set(cls, value: bool):
        cls._dryrun = value


dryrun = Dryrun
