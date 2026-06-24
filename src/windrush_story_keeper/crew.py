from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

ollama_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)


@CrewBase
class WindrushStoryKeeper:
    """WindrushStoryKeeper crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def life_events_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["life_events_agent"],
            llm=ollama_llm,
            verbose=True,
        )

    @agent
    def themes_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["themes_agent"],
            llm=ollama_llm,
            verbose=True,
        )

    @agent
    def follow_up_questions_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["follow_up_questions_agent"],
            llm=ollama_llm,
            verbose=True,
        )

    @task
    def extract_life_events_task(self) -> Task:
        return Task(
            config=self.tasks_config["extract_life_events_task"],
        )

    @task
    def identify_themes_task(self) -> Task:
        return Task(
            config=self.tasks_config["identify_themes_task"],
            output_file="windrush_story_summary.md",
        )

    @task
    def follow_up_questions_task(self) -> Task:
        return Task(
            config=self.tasks_config["follow_up_questions_task"],
            output_file="follow_up_questions.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )