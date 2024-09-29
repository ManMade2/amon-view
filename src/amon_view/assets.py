import os
import json


assetsPath = os.getcwd() + "/src/amon_view/static/assets"

def getAssetsStructure() -> dict[str, list[str]]:
    structure: dict[str, list[str]] = {}

    for folder in os.listdir(assetsPath):
        files = []

        for file in os.listdir(f"{assetsPath}/{folder}"):
            files.append(file.removesuffix(".json"))

        structure[folder] = files

    return structure


def _readJson(filePath: str) -> str|None:

    try:
        with open(f"{assetsPath}{filePath}.json", "r") as file:
            return json.load(file)
    except:
        print(f'failed to load file: {filePath}')


def loadMap(name: str) -> str|None:
    return _readJson(f"/maps/{name}")
