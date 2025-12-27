# Required Notice:
# Copyright © 2025 Wolfie
# Licensed under the Polyform Noncommercial License 1.0.0
# https://polyformproject.org/licenses/noncommercial/1.0.0

import anthropic

client = anthropic.Anthropic()

# List Anthropic-managed Skills
skills = client.beta.skills.list(
    source="anthropic",
    betas=["skills-2025-10-02"]
)

for skill in skills.data:
    print(f"{skill.id}: {skill.display_title}")
