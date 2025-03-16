from src.generators.frontend_generator import generate_frontend


def generate_project(preset: dict, name: str):
    generate_frontend(preset["preset"]["frontend"], name)
