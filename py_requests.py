"""Sample API automation using requests.

Run:
	python py_requests.py
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class ApiConfig:
	base_url: str
	api_key: str | None = None
	timeout_seconds: float = 10.0


class ApiClient:
	def __init__(self, config: ApiConfig) -> None:
		self._config = config
		self._session = requests.Session()
		if config.api_key:
			# Example of an API key header; change to match your API.
			self._session.headers.update({"Authorization": f"Bearer {config.api_key}"})
		self._session.headers.update({"Content-Type": "application/json"})

	def _url(self, path: str) -> str:
		return f"{self._config.base_url.rstrip('/')}/{path.lstrip('/')}"

	def get(self, path: str) -> requests.Response:
		return self._session.get(self._url(path), timeout=self._config.timeout_seconds)

	def post(self, path: str, payload: dict[str, Any]) -> requests.Response:
		return self._session.post(
			self._url(path),
			data=json.dumps(payload),
			timeout=self._config.timeout_seconds,
		)

	def put(self, path: str, payload: dict[str, Any]) -> requests.Response:
		return self._session.put(
			self._url(path),
			data=json.dumps(payload),
			timeout=self._config.timeout_seconds,
		)

	def delete(self, path: str) -> requests.Response:
		return self._session.delete(self._url(path), timeout=self._config.timeout_seconds)


def assert_status(response: requests.Response, expected: int) -> None:
	if response.status_code != expected:
		raise AssertionError(
			f"Expected {expected}, got {response.status_code}: {response.text}"
		)


def pretty_json(response: requests.Response) -> str:
	try:
		return json.dumps(response.json(), indent=2, sort_keys=True)
	except ValueError:
		return response.text


def run_sample() -> None:
	# Public test API for samples: https://jsonplaceholder.typicode.com
	config = ApiConfig(
		base_url=os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com"),
		api_key=os.getenv("API_KEY"),
	)
	client = ApiClient(config)

	# GET
	get_response = client.get("/posts/1")
	assert_status(get_response, 200)
	print("GET /posts/1")
	print(pretty_json(get_response))

	# POST
	create_payload = {"title": "hello", "body": "from requests", "userId": 1}
	post_response = client.post("/posts", create_payload)
	assert_status(post_response, 201)
	print("\nPOST /posts")
	print(pretty_json(post_response))

	# PUT
	update_payload = {"id": 1, "title": "updated", "body": "changed", "userId": 1}
	put_response = client.put("/posts/1", update_payload)
	assert_status(put_response, 200)
	print("\nPUT /posts/1")
	print(pretty_json(put_response))

	# DELETE
	delete_response = client.delete("/posts/1")
	assert_status(delete_response, 200)
	print("\nDELETE /posts/1")
	print(delete_response.text or "<no content>")


if __name__ == "__main__":
	run_sample()
