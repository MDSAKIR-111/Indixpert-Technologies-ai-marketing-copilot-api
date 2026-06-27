import json


def build_strategy_prompt(context: dict):
    return f"""
You are a senior Digital Marketing Strategist.

Your task is to create a complete AI-powered content strategy for this business.

Business Context

{json.dumps(context, indent=2,default=str)}

Instructions

1. Analyze the business.
2. Identify the target audience.
3. Recommend the best content strategy.
4. Recommend suitable content pillars.
5. Recommend posting frequency.
6. Recommend social media platforms.
7. Strategy should be practical and realistic.

Return ONLY valid JSON.

Example:

{{
    "strategy_name": "",
    "goal": "",
    "content_pillars": "",
    "posting_frequency": "",
    "platforms": ""
}}

Do not explain anything.

Do not use Markdown.

Return JSON only.
"""