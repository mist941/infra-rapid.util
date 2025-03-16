import json
import os
import pathlib


def copy_store_template(path, store_name):
    # Get the directory of the current script
    current_dir = pathlib.Path(__file__).parent.absolute()
    template_path = os.path.join(current_dir, "store-template.ts")

    with open(
        template_path,
        "r",
    ) as template_file:
        template_content = template_file.read()

    # Customize the store name if needed
    customized_content = template_content.replace(
        "useStore", f"use{store_name.capitalize()}"
    )

    with open(f"{path}/{store_name}.ts", "w") as f:
        f.write(customized_content)


def copy_button_component(dest_path):
    # Get the directory of the current script
    current_dir = pathlib.Path(__file__).parent.absolute()
    button_folder_path = os.path.join(current_dir, "Button")

    # Create Button directory in destination
    button_dest_path = os.path.join(dest_path, "Button")
    os.makedirs(button_dest_path, exist_ok=True)

    # Copy all files from Button folder
    if os.path.exists(button_folder_path):
        for file_name in os.listdir(button_folder_path):
            source_file = os.path.join(button_folder_path, file_name)
            dest_file = os.path.join(button_dest_path, file_name)

            if os.path.isfile(source_file):
                with open(source_file, "r") as src_file:
                    content = src_file.read()

                with open(dest_file, "w") as dst_file:
                    dst_file.write(content)


def update_components_json(architecture: str):
    current_dir = pathlib.Path(__file__).parent.parent.absolute()
    components_json_path = os.path.join(current_dir, "components.json")

    with open(components_json_path, "r") as f:
        components_config = json.load(f)

    if architecture == "atomic":
        components_config["aliases"] = {
            "components": "@/components/atoms",
            "utils": "@/lib/utils",
            "ui": "@/components/atoms",
            "lib": "@/lib",
            "hooks": "@/hooks",
        }
    elif architecture == "feature-based":
        components_config["aliases"] = {
            "components": "@/shared/ui",
            "utils": "@/lib/utils",
            "ui": "@/shared/ui",
            "lib": "@/lib",
            "hooks": "@/shared/hooks",
        }

    with open(components_json_path, "w") as f:
        json.dump(components_config, f, indent=2)


def setup(architecture: str = "atomic"):
    # Update components.json based on architecture
    update_components_json(architecture)

    # Copy the store template instead of creating it

    if architecture == "atomic":
        atomic_dirs = [
            "src/components/atoms",
            "src/components/molecules",
            "src/components/organisms",
            "src/components/templates",
            "src/components/pages",
            "src/utils",
            "src/hooks",
            "src/context",
            "src/services",
            "src/types",
        ]

        # Create each directory
        for directory in atomic_dirs:
            os.makedirs(directory, exist_ok=True)

        # Copy Button component to atoms directory
        copy_button_component("src/components/atoms")

        # Create index files in each component directory
        component_dirs = [
            "/components/pages",
            "/components/atoms",
            "/components/molecules",
            "/components/organisms",
            "/components/templates",
        ]
        for dir_name in component_dirs:
            with open(f"src/{dir_name}/index.ts", "w") as f:
                f.write("// Export all components from this directory\n")

        # Add single store directory in root
        os.makedirs("src/store", exist_ok=True)

        # Create example Zustand store using template
        copy_store_template("src/store", "appStore")

        # Create index file for store
        with open("src/store/index.ts", "w") as f:
            f.write(
                """// Export all stores from this directory
export * from './appStore'
"""
            )
    elif architecture == "feature-based":
        # Create feature-based architecture folders

        # Create main src directories
        feature_dirs = [
            "src/features",
            "src/shared",
            "src/layouts",
            "src/types",
        ]

        # Create each directory
        for directory in feature_dirs:
            os.makedirs(directory, exist_ok=True)

        # Create example feature structure
        example_feature = "src/features/auth"
        feature_subdirs = [
            f"{example_feature}/ui",
            f"{example_feature}/hooks",
            f"{example_feature}/services",
            f"{example_feature}/utils",
            f"{example_feature}/types",
        ]

        for directory in feature_subdirs:
            os.makedirs(directory, exist_ok=True)

        # Create shared structure
        shared_subdirs = [
            "src/shared/ui",
            "src/shared/hooks",
            "src/shared/utils",
            "src/shared/services",
            "src/shared/constants",
        ]

        for directory in shared_subdirs:
            os.makedirs(directory, exist_ok=True)

        # Copy Button component to shared/ui directory
        copy_button_component("src/shared/ui")

        # Add shared store using template
        os.makedirs("src/shared/store", exist_ok=True)
        copy_store_template("src/shared/store", "sharedStore")

        # Create feature-specific store for each feature
        # For the example auth feature
        os.makedirs(f"src/features/auth/store", exist_ok=True)
        copy_store_template("src/features/auth/store", "authStore")

        # Create index files
        with open("src/features/index.ts", "w") as f:
            f.write("// Export all features from this directory\n")

        with open("src/shared/index.ts", "w") as f:
            f.write("// Export all shared modules from this directory\n")

        with open("src/shared/store/index.ts", "w") as f:
            f.write(
                """// Export shared store
export * from './sharedStore'
"""
            )

        with open("src/features/auth/store/index.ts", "w") as f:
            f.write(
                """// Export feature store
export * from './authStore'
"""
            )

        # Update shared index to include store
        with open("src/shared/index.ts", "a") as f:
            f.write("export * from './store'\n")

    elif architecture == "layered":
        pass
    else:
        raise ValueError(f"Invalid architecture: {architecture}")


if __name__ == "__main__":
    setup("feature-based")
