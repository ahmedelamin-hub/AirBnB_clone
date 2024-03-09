#!/usr/bin/python3
"""Test script for BaseModel class."""


from models.base_model import BaseModel

def main():
    """Main function to demonstrate BaseModel functionality."""
    my_model = BaseModel()
    """Create an instance of BaseModel."""
    my_model.name = "My First Model"
    my_model.my_number = 89

    print(my_model)
    """Print the instance (using __str__ method)."""

    my_model.save()
    print(my_model)
    """Update the instance and print it again to see the updated_at change."""

    my_model_json = my_model.to_dict()
    print("JSON of my_model:")
    for key, value in my_model_json.items():
        print(f"\t{key}: ({type(value).__name__}) - {value}")
    """Convert the instance to a dictionary and print the dictionary."""

if __name__ == "__main__":
    unittest.main()
