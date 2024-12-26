### Your README.md file should be minimally multiple paragraphs in length, and should explain what your project is, what each of the files you wrote for the project contains and does, and if you debated certain design choices, explaining why you made them. Ensure you allocate sufficient time and energy to writing a README.md that documents your project thoroughly. Be proud of it! A README.md in the neighborhood of 500 words is likely to be sufficient for describing your project and all aspects of its functionality. If unable to reach that threshold, that probably means your project is insufficiently complex.


# Low FODMAP Chinese Dish Recipe Generator for IBS Management

#### Video Demo:  <URL HERE>

#### Description

This project provides a unique solution for individuals with Irritable Bowel Syndrome (IBS) who are fans of Chinese cuisine and are starting a low FODMAP diet. The Python script at the heart of this project is specifically designed to generate Chinese Dish Recipes that align with low FODMAP dietary standards. This initiative is particularly crucial during the first month of dieting, where identifying potential food triggers is key for people with IBS. My script simplifies this process by offering tailored recipes, helping IBS sufferers enjoy their favorite dishes without compromising their health.

#### Core Features

- **Automated Recipe Creation**: Users can specify the number of dishes, and the script will automatically generate low FODMAP recipes.
- **Health-Conscious Design**: Every dish is selected with IBS dietary restrictions in mind, ensuring a safe and enjoyable meal experience.
- **Adaptive Meal Categorization**: Depending on the time of the request, the recipes are classified as either Lunch or Dinner, aligning with typical meal times (Lunch: 0:00 - 14:00, Dinner: 14:00 - 24:00).
- **Customized Output**: The script generates a text file for the recipes, named according to the meal time and date, for easy reference and record-keeping.

#### Purpose of the files in the project:

File1: dish_recipe.csv - Input CSV file used by the program to randomly generate recipes from.
File2: fodmap_repo.json - Input JSON file used as a database for the program to look up a particular ingredient from a recipe in order to determine whether it's low or high FODMAP.
File3: project.py - this is the file that contains the main function as well as additional functions for user to generate the number of dish recipes as needed.
File4: test_project.py - this is the file that contains code for testing three of the functions in the program using pytest.
File5: requirements.txt - this is the dependant external modules that the project.py imports, which needs to be preinstalled before running it.

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

#### Built With

- Python: The core programming language used in the project.
- Spacy, Inflect: Python libraries used for text processing and natural language tasks.
- CSV, JSON: Utilized for data handling and storage.

#### Getting Started

To get started with this project, clone the repository and ensure Python is installed on your system. Run "pip install -r requirements.txt", to set up the necessary environment.

#### Author

* **Zijian Zhu** - *Initial work*
