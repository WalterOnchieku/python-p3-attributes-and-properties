#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unemployed"):
        self.name = name  # Validate and format name
        self.job = job  # Validate job

    # Getter for the name property
    def get_name(self):
        return self._name

    # Setter for the name property with validation and title case conversion
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case before setting
        else:
            print("Name must be string between 1 and 25 characters.")

    # Getter for the job property
    def get_job(self):
        return self._job

    # Setter for the job property with validation
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    # Define the name and job properties
    name = property(get_name, set_name)
    job = property(get_job, set_job)

