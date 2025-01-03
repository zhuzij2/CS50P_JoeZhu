# Low FODMAP Chinese Dish Recipe Generator for IBS Management

#### Video Demo:  [<https://youtu.be/oEI-crhu7kc>]

#### Description

This project provides a unique solution for individuals with Irritable Bowel Syndrome (IBS) who are fans of Chinese cuisine and are starting a low FODMAP diet. The Python script is specifically designed to generate Chinese Dish Recipes that align with low FODMAP dietary standards. This initiative is particularly crucial during the first month of dieting, where identifying potential food triggers is key for people with IBS. My script simplifies this process by offering tailored recipes randomly selected from a sizable database of recipe options, helping IBS sufferers enjoy their favorite dishes without compromising their health.

#### Core Features

- **Automated Recipe Creation**: Users can specify the number of dishes, and the script will automatically generate low FODMAP recipes.
- **Health-Conscious Design**: Every dish is selected with IBS dietary restrictions in mind, ensuring a safe and enjoyable meal experience.
- **Customized Output**: Depending on the time of the request, the recipes are classified as either Lunch or Dinner, aligning with typical meal times (Lunch: 0:00 - 14:00, Dinner: 14:00 - 24:00). The script generates a text file for the recipes, named according to the meal time and date, for easy reference and record-keeping.

#### Purpose of the files and subfolder in the project:

- File1: dish_recipe.csv - Input CSV file used by the program to randomly generate recipes from.
- File2: fodmap_repo.json - Input JSON file used as a database for the program to look up a particular ingredient from a recipe in order to determine whether it's low or high FODMAP.
- File3: project.py - this is the file that contains the main function as well as additional functions for user to generate the number of dish recipes as needed.
- File4: test_project.py - this is the file that contains script for testing three of the functions in the program using pytest.
- File5: requirements.txt - this is the dependant external modules that the project.py imports, which needs to be preinstalled before running it.
- Subfolder: output - used for storing dish recipes as generated by the program.

#### Ingredient Processing: Design Choices

To ensure accurate validation of ingredients for low FODMAP compliance, the script employs:

- #### Singularization (Inflect)
  Converts plurals like "tomatoes" to "tomato" for consistent dictionary matching.

- #### Noun Extraction (SpaCy)
  Extracts core nouns from descriptions, e.g., "fresh garlic cloves" > "garlic."

- #### Matching Strategy
  - **Direct Match**: Quickly finds exact matches in the FODMAP dictionary.
  - **Close Match**: Maps approximate matches like "baby spinach" to "spinach."

These choices ensure precise and flexible ingredient handling tailored to real-world recipes.

#### Usage

```bash
python project.py -n <number_of_dishes>
```

Replace `<number_of_dishes>` with the desired number of items for the recipes. The script will process this input and create a recipes that respects both the culinary preferences and dietary needs of IBS sufferers.

#### Detailed Functionality

1. **Command-Line Interface**: Users interact with the script through a simple command-line interface, making it accessible for non-technical users.
2. **Dish Selection Algorithm**: The script intelligently selects dishes from a pre-compiled list, ensuring variety and adherence to dietary guidelines.
3. **Output File Generation**: The final recipes are written to a conveniently named text file, making it simple to print or share electronically.

#### Importance for IBS Sufferers

Adhering to a low FODMAP diet, especially in the initial phase, is crucial for managing IBS symptoms. This script empowers users by simplifying the often overwhelming process of meal planning. It opens up a world where enjoying a diverse range of Chinese dishes is possible, without the fear of triggering IBS symptoms.

#### Getting Started

To get started with this project, clone the repository and ensure Python is installed on your system. Run "pip install -r requirements.txt", to set up the necessary environment.

#### Author

* **Zijian Zhu**
