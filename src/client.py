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
            topic = self._parse_topic(message=message.content)

            completion = self._generate_completion(topic)

            await message.reply(content=completion.question)

    def _should_respond(self, message: str) -> bool:
        """
        Check if a string matches the format '!wyr [topic]'.
        """
        pattern = r"\!wyr .+"

        return bool(re.match(pattern, message))

    def _parse_topic(self, message: str) -> str:
        parts = message.split("!wyr")

        return parts[1]

    def _generate_completion(self, topic: str) -> str:
        completion = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=ResponseModel,
            messages=[
                {
                    "role": "user",
                    # pylint: disable=line-too-long
                    "content": f'Generate a thought-provoking "would you rather" question about the following topic: {topic}',
                }
            ],
        )

        return completion
