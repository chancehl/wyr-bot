"""client.py"""
import re
import discord
import instructor
from openai import OpenAI, AsyncOpenAI
from response import ResponseModel


class BotClient(discord.Client):
    """
    Bot client
    """

    openai_client: OpenAI | AsyncOpenAI

    async def on_ready(self):
        """
        Executes on startup
        """

        # patch OpenAI response
        self.openai_client = instructor.patch(OpenAI())

        print(f"Logged on as {self.user}!")

    async def on_message(self, message: discord.Message):
        """
        Executes on message
        """
        print(f"Message from {message.author}: {message.content}")

        if self._should_respond(message=message.content):
            print(self._generate_completion("gross"))
        else:
            print("I should not respond")

    def _should_respond(self, message: str) -> bool:
        """
        Check if a string matches the format '!wyr [topic]'.
        """
        pattern = r"\!wyr .+"

        return bool(re.match(pattern, message))

    def _generate_completion(self, topic: str) -> str:
        completion = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=ResponseModel,
            messages=[
                {
                    "role": "user",
                    "content": f'Generate a {topic} "would you rather" question',
                }
            ],
        )

        return completion
