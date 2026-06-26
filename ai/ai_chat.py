from pathlib import Path

from ollama import Options

from system_prompts import CONCISE, FILE_JSON_FORMAT, Roles
from utils import (
    chat_response_content,
    chat_response_metadata,
    create_model,
    get_file_contents,
    get_response,
    write_to_file,
)
from pydantic import BaseModel, Field


class File(BaseModel):
    title: str
    content: str = Field(
        description="The content of the response, formatted as markdown text (e.g., **Bold**, *Italics*, or `code`)."
    )


def create_prompt(*prompts) -> str:
    return " ".join(prompts)


name, prompt = Roles.SUMMARY_ENGINE.value
create_model(name=name, system_prompt=create_prompt(prompt, CONCISE, FILE_JSON_FORMAT))
options = Options()
options.temperature = 0

project_dir = Path(__file__).parent

REQUEST_FILE = project_dir / "request.md"
RESPONSES_FOLDER = project_dir / "resps"


def run_model():
    print(f"Model: {name}")
    try:
        user_input = get_file_contents(REQUEST_FILE)
        # content = search(user_input)
        # run_model_as_stream(name, user_input)
        print("Working...")
        response = get_response(
            name, user_input, format=File.model_json_schema(), options=options
        )
        file = File.model_validate_json(chat_response_content(response))
        write_to_file(
            file.title,
            file.content + str(chat_response_metadata(response)),
            folder_path=RESPONSES_FOLDER,
        )
        print("Response is ready")
        return

    except KeyboardInterrupt:
        print("\nGood bye!")
        return


run_model()
