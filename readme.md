# LEXI BOT BY LADYSAVANT

Introducing to Lexi Bot, a Discord bot created for Savant's Server of Friends! Lexi is designed to enhance the Discord experience through unique commands and server-specific features.

## Features

- Features are modular! They can easily be enabled, disabled, or built upon.
- Custom Commands: Unique commands tailored for Savant's Server of Friends.
- Server Moderation: Helps keep the server safe and organized.

## Getting Started

### Prerequisites

To run Lexi, you'll need:

- Python (v3.8 or higher)
- Discord Python Library
- A Discord bot token ([How to create a bot account](https://discordpy.readthedocs.io/en/stable/discord.html))

### Installation

1. Clone the repository with `git clone https://github.com/TaliBytes/discord-lexi-bot`
2. Navigate to the repository with `cd discord-lexi-bot`
3. Install dependencies `pip install discord.py`
4. [Add the Discord bot to your server using the *Developer Portal*](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal)
5. To disable a feature, move the corresponding file from "/modules" dir to "/modules/disabled" dir. Restart Lexi.

### Running Lexi

Lexi should now be online and ready to use in the server of your choosing.
Run the python script using an internet-enabled device.

## Syntax & Usage

To send commands to Lexi a specific syntax is used. It is broken down as follows:

- `$` - indicates the start of a command.
- `{...}` - curly braces surround the command.
- `|` - pipe characters separate the command name (first argument) from command arguments (remaining arguments).
- `${aCmd|arg1|arg2|etc}` - commands can take any number of arguments; however, some commands require a minimum number. If there are extra arguments supplied, the extras are ignored.
- When sending a command, it must be the ONLY thing in the Discord message. If anything else is added outside of the command, Lexi will ignore it altogether. (This allows users to easily share or explain syntax to others.)

For example:

- `S{say|message}` - Lexi Bot will repeat a message of your choosing and delete your command.
- more examples coming soon (or maybe not)!
Note: The available commands and features may be updated over time. Use `${help}` for the latest list.

## Directories

- /botlib ... included python files and the like for Lexi
- /root ... includes static files, token, etc

## Contributing

This is currently a private project which is not allowing additional contributions.

## License

This project is licensed under the MIT License.
