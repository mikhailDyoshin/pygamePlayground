from system_prompts import Roles
from utils import create_model, run_model


name, prompt = Roles.CRITIC.value
create_model(
    name=name,
    system_prompt=prompt,
)
# options = Options()
# options.temperature = 1.0


while True:
    user_input = input("Input: ")
    # content = search(user_input)
    run_model(name, user_input)
