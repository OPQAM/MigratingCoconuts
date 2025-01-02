#!/usr/bin/env python3

import argparse
import importlib
from pathlib import Path

# Path to tools
TOOLS_DIR = Path(__file__).parent / "tools"

def list_tools():
    """Dynamically lists available tools in tools/"""
    tools = [f.stem for f in TOOLS_DIR.glob("*.py") if f.name != "__init__.py"]
    return tools

def run_tool(tool_name, args):
    """loads and runs tool by name"""
    try:
        tool_module = importlib.import_module(f"tools.{tool_name}")
        if hasattr(tool_module, "main"):
            tool_module.main(args)
        else:
            print(f"No main func for tool '{tool_name}'")
    except ModuleNotFoundError:
        print(f"Tool '{tool_name}' not found")
    except Exception as e:
        print(f"Error running '{tool_name}': {e}")


def main():
    parser = argparse.ArgumentParser(description="Lazysuite - Automation Suite")
    parser.add_argument("tool", help="Name of tool", choices=list_tools())
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Tool arguments")
    args = parser.parse_args()

    run_tool(args.tool, args.args)

if __name__ == "__main__":
    main()
