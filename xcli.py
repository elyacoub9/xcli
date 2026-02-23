# xcli.py

import config
import urllib3
from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, VSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.key_binding import KeyBindings

from api import list_vms, list_images, list_subnets, list_categories, list_containers, list_clusters
from parse_entities import parse_entities

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = config.HOST
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD


# ------------------ STATIC DATA ------------------

RESOURCES = ["VMs", "Images", "Subnets", "Categories", "Containers", "Prism Central", "Prism Element"]


# ------------------ SIMPLE STATE ------------------

pane = "left"        # left | right
view = "resources"   # resources | list | details
index = 0
items = []
current = None


# ------------------ RENDER ------------------

def render_left():
    lines = []
    for i, name in enumerate(RESOURCES):
        pointer = "➜ " if pane == "left" and i == index else "  "
        lines.append(pointer + name)
    return "\n".join(lines)


def render_right():
    if view == "resources":
        return "Select a resource"

    if view == "list":
        lines = []
        for i, item in enumerate(items):
            pointer = "➜ " if pane == "right" and i == index else "  "
            lines.append(pointer + item["name"])
        return "\n".join(lines)

    if view == "details":
        return f"Name: {current['name']}\nUUID: {current['uuid']}"

    return ""


left_window = Window(FormattedTextControl(render_left), wrap_lines=False)
right_window = Window(FormattedTextControl(render_right), wrap_lines=False)

layout = Layout(VSplit([left_window, right_window]))


# ------------------ DATA LOADER ------------------

def load(resource):
    if resource == "VMs":
        return parse_entities(list_vms(HOST, USERNAME, PASSWORD), "vm")

    if resource == "Images":
        return parse_entities(list_images(HOST, USERNAME, PASSWORD), "image")

    if resource == "Subnets":
        return parse_entities(list_subnets(HOST, USERNAME, PASSWORD), "subnet")
    
    if resource == "Categories":
        return parse_entities(list_categories(HOST, USERNAME, PASSWORD), "category")
    
    if resource == "Containers":
        return parse_entities(list_containers(HOST, USERNAME, PASSWORD), "container")
    
    if resource == "Prism Central":
        return parse_entities(list_clusters(HOST, USERNAME, PASSWORD), "pc")
    
    if resource == "Prism Element":
        return parse_entities(list_clusters(HOST, USERNAME, PASSWORD), "pe")

    return []


# ------------------ KEYBINDINGS ------------------

kb = KeyBindings()


@kb.add("q")
def _(event):
    event.app.exit()


@kb.add("tab")
def _(event):
    global pane
    pane = "right" if pane == "left" else "left"


@kb.add("up")
@kb.add("k")
def _(event):
    global index
    if index > 0:
        index -= 1


@kb.add("down")
@kb.add("j")
def _(event):
    global index

    if pane == "left":
        max_len = len(RESOURCES)
    else:
        max_len = len(items)

    if index < max_len - 1:
        index += 1


@kb.add("enter")
def _(event):
    global view, pane, index, items, current

    # Selecting resource
    if pane == "left":
        selected = RESOURCES[index]
        items = load(selected)
        view = "list"
        pane = "right"
        index = 0
        return

    # Selecting item
    if view == "list" and items:
        current = items[index]
        view = "details"
        index = 0


@kb.add("b")
def _(event):
    global view, pane, index

    if view == "details":
        view = "list"
    elif view == "list":
        view = "resources"
        pane = "left"

    index = 0


app = Application(
    layout=layout,
    key_bindings=kb,
    full_screen=True,
)

if __name__ == "__main__":
    app.run()