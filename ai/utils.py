from dataclasses import dataclass, fields
from pathlib import Path
from typing import Iterator

from ollama import (
    ChatResponse,
    Message,
    Options,
    ProgressResponse,
    create,
    chat,
    web_search,
)
from pydantic.json_schema import JsonSchemaValue


@dataclass(frozen=True)
class ChatResponseMetadata:
    model: str
    input_tokens: str
    output_tokens: str
    total_duration_in_sec: str

    def __str__(self) -> str:
        return "\n\n" + "\n".join([getattr(self, f.name) for f in fields(self)])


def chat_response_metadata(response: ChatResponse) -> ChatResponseMetadata:
    return ChatResponseMetadata(
        model=f"Model: {response.model}",
        input_tokens=f"Input tokens: {response.prompt_eval_count}",
        output_tokens=f"Output tokens: {response.eval_count}",
        total_duration_in_sec=f"Total duration: {ns_to_s(response.total_duration):.2f} sec.",
    )


def chat_response_content(response: ChatResponse) -> str:
    content = response.message.content
    if content:
        return content
    return "No content"


def create_model(*, name: str, system_prompt: str) -> ProgressResponse:
    return create(
        model=name,
        from_="qwen3.5",
        system=system_prompt,
    )


def ns_to_s(ns: int | None) -> float | None:
    if ns:
        return ns / 1e9
    return None


def create_stream(
    model: str, role: str, message_content: str, options: Options
) -> Iterator[ChatResponse]:
    return chat(
        model=model,
        messages=[Message(role=role, content=message_content)],
        stream=True,
        think=False,
        options=options,
    )


def print_chat_stream(stream: Iterator[ChatResponse]) -> None:
    for chunk in stream:
        print(chunk.message.content, end="", flush=True)
        if chunk.done:
            print(chat_response_metadata(chunk))


def run_model_as_stream(
    model: str, user_input: str, options: Options = Options()
) -> None:
    stream = create_stream(
        model=model, role="user", message_content=user_input, options=options
    )
    print_chat_stream(stream)


def get_response(
    model: str,
    user_input: str,
    format: JsonSchemaValue | None = None,
    options: Options = Options(),
) -> ChatResponse:
    return chat(
        model=model,
        messages=[Message(role="user", content=user_input)],
        think=False,
        format=format,
        options=options,
    )


def search(input: str) -> str:
    response = web_search(input)
    return "\n".join([r.get("content", "") for r in response.get("results", [])])


def write_to_file(file_name: str, content: str, folder_path: Path = Path("")):
    with open(folder_path / f"{file_name}.md", "w", encoding="utf-8") as file:
        file.write(content)


def get_file_contents(file_path: Path) -> str:
    """Reads a file and returns its contents as a single string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
