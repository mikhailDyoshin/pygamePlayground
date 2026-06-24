from system_prompts import CONCISE, Roles
from utils import (
    chat_response_content,
    chat_response_metadata,
    create_model,
    get_response,
    write_to_file,
)


name, prompt = Roles.CRITIC.value
create_model(
    name=name,
    system_prompt=prompt + CONCISE,
)
# options = Options()
# options.temperature = 1.0


while True:
    try:
        user_input = input("Input: ")
        # content = search(user_input)
        # run_model_as_stream(name, user_input)
        response = get_response(name, user_input)
        content = chat_response_content(response) + str(
            chat_response_metadata(response)
        )
        write_to_file(content)
        print("File is ready")

    except KeyboardInterrupt:
        print("\nGood bye!")
        break
