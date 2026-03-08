**Disclaimer: This bot was originally developed several years ago as a personal project. It is provided as is for educational or experimental purposes only. I do not take responsibility for how this bot is used or deployed.**

The bot may not run correctly in Visual Studio Code. For best compatibility, it is recommended to run it on replit.com. 

To ensure the bot functions properly, all required dependencies must be installed. The repository includes the following files defining package requirements:

• .pythonlibs
• poetry.lock
• pyproject.toml

Replit typically installs the necessary dependencies automatically. However, if it does not, install them manually using Poetry or your preferred Python environment manager.

You only need to configure the bot’s authentication token.
In the config.json file, do not paste your actual bot token directly—doing so may expose it publicly and compromise your bot’s security.

Instead, create a secret that securely stores your token. In Replit, this can be done as follows:

1. Click the four-square icon on the left sidebar.
2. Scroll down until you find the lock icon labeled Secrets.
3. Click Secrets, then create a new secret and enter your bot token as its value.
4. Ensure the secret name matches the token reference used in your config.json (for example, "TOKEN").

![image](https://github.com/user-attachments/assets/d0d9bff1-6514-4fde-aeb0-81f4daa0523a)
![image](https://github.com/user-attachments/assets/ed526b10-ed80-4cb7-853d-ba6177c7ea7b)



