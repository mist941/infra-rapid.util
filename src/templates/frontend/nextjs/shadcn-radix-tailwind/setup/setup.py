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


def copy_button_component(source_path, dest_path):
    # Get the directory of the current script
    current_dir = pathlib.Path(__file__).parent.absolute()
    button_path = os.path.join(current_dir, "Button.tsx")

    # Copy Button component to the appropriate directory
    if os.path.exists(button_path):
        with open(button_path, "r") as button_file:
            button_content = button_file.read()

        with open(f"{dest_path}/Button.tsx", "w") as f:
            f.write(button_content)


def setup(architecture: str):
    # Copy the store template instead of creating it

    if architecture == "atomic":
        atomic_dirs = [
            "src/components/atoms",  # Smallest, indivisible components (buttons, inputs, etc.)
            "src/components/molecules",  # Combinations of atoms (form fields, search bars, etc.)
            "src/components/organisms",  # Complex UI sections (headers, forms, etc.)
            "src/components/templates",  # Page layouts without specific content
            "src/components/pages",  # Complete pages using templates and organisms
            "src/utils",  # Utility functions
            "src/hooks",  # Custom React hooks
            "src/context",  # React context providers
            "src/services",  # API services and external integrations
            "src/assets",  # Images, fonts, and other static assets
            "src/types",  # TypeScript type definitions
        ]

        # Create each directory
        for directory in atomic_dirs:
            os.makedirs(directory, exist_ok=True)

        # Copy Button component to atoms directory
        copy_button_component("setup", "src/components/atoms")

        # Create index files in each component directory
        component_dirs = [
            "/components/pages",
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
            "src/features",  # Main features directory
            "src/shared",  # Shared components, hooks, utils
            "src/layouts",  # Layout components
            "src/assets",  # Images, fonts, and other static assets
            "src/types",  # TypeScript type definitions
        ]

        # Create each directory
        for directory in feature_dirs:
            os.makedirs(directory, exist_ok=True)

        # Create example feature structure
        example_feature = "src/features/auth"
        feature_subdirs = [
            f"{example_feature}/components",  # Feature-specific components
            f"{example_feature}/hooks",  # Feature-specific hooks
            f"{example_feature}/services",  # Feature-specific API services
            f"{example_feature}/utils",  # Feature-specific utilities
            f"{example_feature}/types",  # Feature-specific types
        ]

        for directory in feature_subdirs:
            os.makedirs(directory, exist_ok=True)

        # Create shared structure
        shared_subdirs = [
            "src/shared/ui",  # Reusable UI components
            "src/shared/hooks",  # Reusable hooks
            "src/shared/utils",  # Utility functions
            "src/shared/services",  # Common API services
            "src/shared/constants",  # App constants
        ]

        for directory in shared_subdirs:
            os.makedirs(directory, exist_ok=True)

        # Copy Button component to shared/ui directory
        copy_button_component("setup", "src/shared/ui")

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
