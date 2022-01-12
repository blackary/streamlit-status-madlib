from datetime import date, timedelta
from typing import List

import streamlit as st

st.set_page_config(page_title="Status Madlib", page_icon="green_heart", layout="centered")

st.title("Status Madlib")
st.write("Copied from https://manager138.com/projects/2021/03/02/status_madlib.html")

RED = ":octagonal_sign:"
YELLOW = ":thinking_face:"
GREEN = ":green_heart:"

color_map = {"Red": RED, "Green": GREEN, "Yellow": YELLOW}

with st.expander("Show instructions"):
    st.write(f"""
    ## Template
    ### Definitions:

    | Color      | Description |
    | ----------- | ----------- |
    | {RED} (Red) |  Needs outside action to succeed. Blocked or will definitely miss planned milestones | 
    | {YELLOW} (Yellow) | Has internal issue(s) or unexpected surprises, but already has a plan to resolve them. If plan doesn't work, could potentially miss planned milestones. |
    | {GREEN} (Green) | Likely to hit planned milestones, no active issues or surprises. |

    We are {{{RED}/{YELLOW}/{GREEN}}} to complete {{name of project or task}} by {{time}}

    (optional – if {RED}) I am {RED} and not {GREEN} because {{SHORT description of blocker}}.

    The next action is for {{name}} to {{deliverable: task AND communication method}} by {{time}}

    (optional – if {YELLOW}) A potential future challenge is {{SHORT description of stumbling block}}. My plan to mitigate is {{SHORT description of mitigation}}.
    """)

default_date = date.today() + timedelta(days=1)

status = st.selectbox("Status", ["Green", "Yellow", "Red"])

red_blocker = ""
stumbling_block = ""
mitigation_plan = ""

if status == "Red":
    red_blocker = st.text_input("Blocker -- reason for being Red and not Green (optional)")
elif status == "Yellow":
    stumbling_block = st.text_input("SHORT description of potential future challenge (optional)")
    mitigation_plan = st.text_input("SHORT description of mitigation (optional)")

project_name = st.text_input("Project name")

completion_date = st.date_input("Completion date", value=default_date)

deliverer = st.text_input("Who is responsible for delivery?")
next_deliverable = st.text_input("Deliverable: task AND communication method")

deliverable_date = st.date_input("Deliverable date", value=default_date)

content: List[str] = []

content += [f"## We are {color_map[status]} to complete {project_name} by {completion_date}."]

if red_blocker:
    content += [f"## I am {RED} and not {GREEN} because {red_blocker}."]

content += [f"## The next action is for {deliverer} to {next_deliverable} by {deliverable_date}"]

if stumbling_block and mitigation_plan:
    content += [f"## A potential future challenge is {stumbling_block}. My plan to mitigate is {mitigation_plan}."]

all_content = "\n".join(content)

st.write(all_content)

with st.expander("Show copiable text"):
    st.code(all_content.replace("## ", ""))

