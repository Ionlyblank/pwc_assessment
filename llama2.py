import replicate

def get_llama2_response(query):
    response = ""
    for event in replicate.stream(
        "meta/llama-2-70b-chat",
        input={
            "debug": False,
            "top_p": 1,
            "prompt": query,
            "temperature": 0.5,
            "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
            "max_new_tokens": 500,
            "min_new_tokens": -1
        },
    ):
        response += str(event)
    return response
