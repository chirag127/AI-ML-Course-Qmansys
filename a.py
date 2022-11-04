import openai

def get_text_from_openai(
    prompt_,
    model="code-davinci-002",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,

):
    number_of_characters = len(prompt_)

    max_number_of_characters = 20000

    if number_of_characters > max_number_of_characters:
        print("The prompt is too long. Please shorten it.")
        prompt_ = prompt_[-max_number_of_characters:]

    number_of_characters = len(prompt_)

    max_tokens = 7000 - number_of_characters // 4
    OPENAI_API_KEYs = [ "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","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"]

    openai.api_key = "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"
    response = openai.Completion.create(
        model=model,
        prompt=prompt_,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=["\n\n\n", "###","\r\n\r\n\r\n"],
    )

    # pretty_print the response
    import pprint

    # pprint.pprint(response)

    text = response.choices[0].text

    print(f"text: {text}")

    with open("openai_response.txt", "a",encoding="utf-8") as file:
        file.write(text)

    return text

prompt = "# write a python program to detect the text from the image by 10 different methods\nimport easyocr"
a = get_text_from_openai(prompt)
print(a)
prompt += a