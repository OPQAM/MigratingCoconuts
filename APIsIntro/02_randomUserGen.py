#!/usr/bin/env python3

import requests


# As with other examples, we're getting info from the API.
response = requests.get("https://randomuser.me/api/")

# And here we're getting a confirmation.
print(response)

# But we need a way to actually print what was requested
user_text = response.text

# This will print the response.text, without any care about indentation or paragraphs
print(user_text)

# Obviously, in this case, there is no request for authentication.
