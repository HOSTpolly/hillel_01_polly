import argparse
import asyncio
from pprint import pprint as print

import requests
from pydantic import BaseModel, Field

API_KEY = "YOUR_API_KEY"  # Replace with your API key
BASE_URL = "https://www.alphavantage.co"


class AlphavantageCurrencyExchangeRatesRequest(BaseModel):
    currency_from: str
    currency_to: str


class AlphavantageCurrencyExchangeRatesResults(BaseModel):
    currency_from: str = Field(alias="1. From_Currency Code")
    currency_to: str = Field(alias="3. To_Currency Code")
    rate: float = Field(alias="5. Exchange Rate")


class AlphavantageCurrencyExchangeRatesResponse(BaseModel):
    results: AlphavantageCurrencyExchangeRatesResults = Field(
        alias="Realtime Currency Exchange Rate"
    )


async def fetch_currency_exchange_rates(
    schema: AlphavantageCurrencyExchangeRatesRequest,
) -> AlphavantageCurrencyExchangeRatesResponse:
    """This function claims the currency exchange rate information
    from the external service: Alphavantage.
    """
    payload: str = (
        "/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={schema.currency_from.upper()}&"
        f"to_currency={schema.currency_to.upper()}&"
        f"apikey={API_KEY}"
    )
    url: str = "".join([BASE_URL, payload])

    raw_response: requests.Response = requests.get(url)
    response = AlphavantageCurrencyExchangeRatesResponse(**raw_response.json())

    return response


def initialize_args_parser():
    parser = argparse.ArgumentParser(
        prog="Currency exchange rates fetcher",
        description="This app fetches exchange rates from Alphavantage",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("currency_from", nargs="+", help="List of source currencies")
    parser.add_argument("--target", help="Target currency", required=True, dest="currency_to")

    return parser.parse_args()


async def main():
    args: argparse.Namespace = initialize_args_parser()
    target_currency = args.currency_to
    source_currencies = args.currency_from

    tasks = []

    for source_currency in source_currencies:
        task = asyncio.create_task(
            fetch_currency_exchange_rates(
                AlphavantageCurrencyExchangeRatesRequest(
                    currency_from=source_currency, currency_to=target_currency
                )
            )
        )
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    for source_currency, result in zip(source_currencies, results):
        print(f"Exchange rate from {source_currency} to {target_currency}:{result.results.rate}")


if __name__ == "__main__":
    asyncio.run(main())
