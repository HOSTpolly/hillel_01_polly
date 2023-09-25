from typing import Any

message = """I load it in python using cPickle.
I tried to ascertain its size using pympler asizeof.
But there is a considerable difference size given by asize of and sys.getsizeof
"""

# message="\n".join (I load it in python using cPickle.
# I tried to ascertain its size using pympler asizeof.
# But there is a considerable difference size given by asize of and sys.getsizeof
# )

message = (
    "I load it in python using cPickle."
    "I tried to ascertain its size using pympler asizeof. "
    "But there is a considerable difference size given by asize of and sys.getsizeof"
)


class PaymentSystem:
    def __init__(self, provider) -> None:
        self.provider: str = provider

    def foo(self):
        return "I'm foo from Payment System"

    # def __getattribute__(self, name: str) -> Any:
    #     if not name in self.__dict__:
    #         raise AttributeError(f"Your class does not have this field:{name}")
    #     return super().__getattribute__(name)

    def get_atr(self, name: str) -> Any:
        if name not in self.__dict__keys():
            raise AttributeError(f"Your class does not have this field:{name}")
        return super().__getattribute__(name)


paypal = PaymentSystem(provider="PayPal")
print(paypal.__dict__)

# print(paypal.provider)
data = paypal.get_atr("providers")

print(paypal.provider)
