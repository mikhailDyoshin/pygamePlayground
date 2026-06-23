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
            print(f"\n\nModel: {chunk.model}")
            print(f"Input tokens: {chunk.prompt_eval_count}")
            print(f"Output tokens: {chunk.eval_count}")
            print(f"Total duration: {ns_to_s(chunk.total_duration):.2f} sec.")


def run_model(model: str, user_input: str, options: Options = Options()) -> None:
    stream = create_stream(
        model=model, role="user", message_content=user_input, options=options
    )
    print_chat_stream(stream)


def search(input: str) -> str:
    response = web_search(input)
    return "\n".join([r.get("content", "") for r in response.get("results", [])])
