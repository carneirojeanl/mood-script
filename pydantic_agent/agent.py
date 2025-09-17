import os

from dataclasses import dataclass

from pydantic import BaseModel, Field

from pydantic_ai import Agent, RunContext

from pydantic_ai.exceptions import AgentRunError

from dotenv import load_dotenv

from tts.google_tts import GoogleTTS

# Load environment variables
load_dotenv()

@dataclass
class AgentDependencies():
    user_id: int
    user_first_name: str

class AgentOutput(BaseModel):
    agent_response: str = Field(description='Response returned to the user')
    audio_path: str = Field(default=None, description='The path to the podcast audio file')
    script_file_path: str = Field(default=None, description='The path to the script file')

class ScriptAgent:
    def __init__(self, user_id: int, user_first_name: str, user_input: str):
        self.user_id = user_id
        self.user_first_name = user_first_name
        self.user_input = user_input

    with open("instructions.md", "r", encoding="utf-8") as f:
        instructions = f.read()

    script_agent = Agent(
        'gemini-2.0-flash-lite',
        deps_type=AgentDependencies,
        output_type=AgentOutput,
        instructions=instructions,
        retries=3
    )

    def run_agent(self):
        try:
            deps = AgentDependencies(user_id=self.user_id, user_first_name=self.user_first_name)
            result = self.script_agent.run_sync(self.user_input, deps=deps)
            result_output = result.output
            return result_output
        except AgentRunError as e:
            return f"Error running agent. Try again later. Error: {e}"
        except Exception as e:
            return f"Error running agent. Try again later. Error: {e}"
        

    @staticmethod
    @script_agent.instructions
    async def add_user_name(ctx: RunContext[AgentDependencies]) -> str:
        user_name = ctx.deps.user_first_name
        return f"The user first name is {user_name!r}"

    @staticmethod
    @script_agent.tool
    async def generate_audio_from_script(ctx: RunContext[AgentDependencies], script: str, theme: str):
        """
        Use this tool ONLY IF the user asks to generate an audio from a script.
        """
        print("THE TOOL GENERATE_AUDIO_FROM_SCRIPT IS CALLED")

        # It creates a folder called scripts if it doesn't exist
        os.makedirs("scripts", exist_ok=True)

        # it creates a file called scripts/{theme}.txt
        script_file_path = os.path.join("scripts", f"{theme}.txt")

        formatted_theme = theme.strip().replace(" ", "_").lower()
        with open(script_file_path, "w") as script_file:
            script_file.write(script)
            script_file.close()
        
        tts = GoogleTTS(text=script, file_name=formatted_theme)
        audio_path = tts.generate()
        return {
            "audio_path": audio_path,
            "script_file_path": script_file_path
        }
