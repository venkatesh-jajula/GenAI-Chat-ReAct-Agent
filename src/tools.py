from langchain_core.tools import Tool
from data_loader import load_entire_data
from search import get_details

sushi_data, parking_data = load_entire_data()

#Tool-1
def tool_get_sushi_places(arg=None):
    "Return sushi places"
    results=[item["title"] for item in sushi_data if "title" in item]     
    if not results:
        return "No SUSHI PLACES found."
    return results

#Tool-2
def tool_get_parking_places(arg=None):
    "Return parking places"
    results=[item["title"] for item in parking_data if "title" in item]   
    if not results:
        return "No PARKING PLACES found."
    return results

#Tool-3
def tool_get_details(title):
    "Return detailed information for any sushi or parking place."
    title=title.strip().strip('"').strip("'")
    details = get_details(sushi_data, title) or get_details(parking_data, title)
    if not details:
        return f"No details found for the place titled : '{title}'."
    return str(details)



tools = [
    Tool(
        name="sushi",
        func=tool_get_sushi_places,
        description="Use this tool to find sushi places, it returns all sushi places.",
    ),
    Tool(
        name="parking",
        func=tool_get_parking_places,
        description="Use this tool to find parking places, it returns all parking places.",
    ),
    Tool(
        name="details",
        func=tool_get_details,
        description="Use this tool to get detailed information about any specific sushi or parking place by providing its title as an input. Note: Extract the title wisely",
    )
    ]

if __name__ == "__main__":
    # print(tool_get_sushi_places())
    # print("\n")
    # print(tool_get_parking_places())
    # print("\n")
    print(tool_get_details("Galeria Restaurant"))