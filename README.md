# Python Classes for Data Ingestion Project

This project demonstrates the use of Object-Oriented Programming **(OOP)** to build a data ingestion system for Data Engineering. 

It monitors local folders for new files (CSV and TXT), using abstract classes and inheritance for a modular and reusable codebase.

## Key Features
* **Object-Oriented Architecture:** Specialized classes like `CsvSources` and `TxtSources` inherit from a base class, making it easy to add new data sources.

* **Folder Monitoring:** The script periodically checks folders for new files.

* **Data Processing:** Uses the Pandas library to read and transform data into DataFrames.

* **Scheduling:** The schedule library automates file checks at defined intervals.

## Potential Improvements
The project serves as a solid foundation and can be expanded to:

* Process data from other sources (JSON, APIs, databases).

* Add more complex data transformation rules.

* Save the data to a database or a data lake.