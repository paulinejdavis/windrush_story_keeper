#!/usr/bin/env python3
import re
from pathlib import Path

transcript = """
I arrived in London from Jamaica in 1963 when I was 21 years old.
I first worked on London Transport and later became a bus driver.
Housing was difficult to find and many landlords refused to rent to Black people.
My church community became an important source of support.
I eventually bought a home, raised three children and remained active in community organisations.
"""

themes = {
    'Migration': ['arriv', 'journey', 'from', 'left', 'came'],
    'Work': ['work', 'job', 'factory', 'driver', 'transport'],
    'Housing': ['house', 'home', 'flat', 'landlord', 'damp', 'housing'],
    'Family': ['wife', 'children', 'family', 'married', 'apart'],
    'Community': ['church', 'community', 'neighbour', 'organisation', 'support']
}

def find_evidence(text, keywords):
    for kw in keywords:
        m = re.search(r"(.{0,60}" + re.escape(kw) + r".{0,60})", text, re.I)
        if m:
            return m.group(0).strip()
    return ''

output_lines = []
output_lines.append('Generated follow-up questions (mock)\n')

for theme, kws in themes.items():
    evidence = find_evidence(transcript, kws)
    output_lines.append(f'### {theme}\n')
    if theme == 'Migration':
        q = 'Could you tell me more about your journey to the UK and your first impressions when you arrived?'
    elif theme == 'Work':
        q = 'What was a typical day like in your early jobs, and who did you work with?'
    elif theme == 'Housing':
        q = 'Can you describe the places you lived in those early years and any problems you faced?'
    elif theme == 'Family':
        q = 'How did family life change after you moved — especially for the children?'
    else:
        q = 'What kinds of people and activities in the community helped you settle in?'

    output_lines.append('1. ' + q)
    if evidence:
        output_lines.append('   - Rationale: "' + evidence.replace('\n', ' ') + '"')
    else:
        output_lines.append('   - Rationale: evidence not found in transcript')
    sensitive = 'yes' if theme == 'Family' else 'no'
    if sensitive == 'yes':
        output_lines.append('   - Sensitive: yes — gentle rephrase: "Would you feel comfortable sharing more about how family life changed?"')
    else:
        output_lines.append('   - Sensitive: no')
    output_lines.append('')

outpath = Path(__file__).resolve().parents[1] / 'follow_up_questions_generated.md'
outpath.write_text('\n'.join(output_lines), encoding='utf-8')
print(f'Wrote mock follow-up questions to {outpath}')
