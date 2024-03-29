
# Low FODMAP Chinese Dish Menu Generator for IBS Management

## Introduction

This project provides a unique solution for individuals with Irritable Bowel Syndrome (IBS) who are fans of Chinese cuisine and are starting a low FODMAP diet. The Python script at the heart of this project is specifically designed to generate Chinese dish menus that align with low FODMAP dietary standards. This initiative is particularly crucial during the first month of dieting, where identifying potential food triggers is key for people with IBS. My script simplifies this process by offering a tailored menu, helping IBS sufferers enjoy their favorite dishes without compromising their health.

## Project Description

The script uses advanced programming techniques, including libraries like `csv`, `json`, `spacy`, and `inflect`, to process dish information and generate user-friendly menus. It's crafted to consider the complexities of dietary restrictions while maintaining the essence of Chinese culinary traditions.

### Core Features

- **Automated Menu Creation**: Users can specify the number of dishes, and the script will automatically generate a low FODMAP menu.
- **Health-Conscious Design**: Every dish is selected with IBS dietary restrictions in mind, ensuring a safe and enjoyable meal experience.
- **Adaptive Meal Categorization**: Depending on the time of the request, the menu is classified as either Lunch or Dinner, aligning with typical meal times (Lunch: 0:00 - 14:00, Dinner: 14:00 - 24:00).
- **Customized Output**: The script generates a text file for the menu, named according to the meal time and date, for easy reference and record-keeping.

### Usage

```bash
python project.py -n <number_of_dishes>
```

Replace `<number_of_dishes>` with the desired number of items for the menu. The script will process this input and create a menu that respects both the culinary preferences and dietary needs of IBS sufferers.

## Detailed Functionality

1. **Command-Line Interface**: Users interact with the script through a simple command-line interface, making it accessible for non-technical users.
2. **Dish Selection Algorithm**: The script intelligently selects dishes from a pre-compiled list, ensuring variety and adherence to dietary guidelines.
3. **Output File Generation**: The final menu is written to a conveniently named text file, making it simple to print or share electronically.

## Importance for IBS Sufferers

Adhering to a low FODMAP diet, especially in the initial phase, is crucial for managing IBS symptoms. This script empowers users by simplifying the often overwhelming process of meal planning. It opens up a world where enjoying a diverse range of Chinese dishes is possible, without the fear of triggering IBS symptoms.

## Built With

- Python: The core programming language used in the project.
- Spacy, Inflect: Python libraries used for text processing and natural language tasks.
- CSV, JSON: Utilized for data handling and storage.

## Getting Started

To get started with this project, clone the repository and ensure Python is installed on your system. Follow the installation instructions provided in the repository to set up the necessary environment.

## Author

* **Zijian Zhu** - *Initial work*

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for more details.

## Final Thoughts

This project stands as a testament to how technology can be harnessed to make life easier and healthier for individuals with specific dietary needs. It's more than just a script; it's a tool for better health and well-being.
