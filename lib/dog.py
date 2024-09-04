#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Mutt"):
        # Validate and set the name first
        self.name = name  
        
        # Then validate and set the breed
        self.breed = breed

    # Getter for the name property
    def get_name(self):
        return self._name

    # Setter for the name property with validation
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    # Getter for the breed property
    def get_breed(self):
        return self._breed

    # Setter for the breed property with validation
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    # Define the name and breed properties
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
