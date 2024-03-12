import random

class Person:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Father(Person):
    def __init__(self, allele):
        blood_type = self.convert_allele_to_blood_type(allele)
        super().__init__(blood_type)
        self.allele = allele

    def convert_allele_to_blood_type(self, allele):
        if allele == 'AA' or allele == 'AO':
            return 'A'
        elif allele == 'BB' or allele == 'BO':
            return 'B'
        elif allele == 'AB':
            return 'AB'
        elif allele == 'OO':
            return 'O'

class Mother(Person):
    def __init__(self, allele):
        blood_type = self.convert_allele_to_blood_type(allele)
        super().__init__(blood_type)
        self.allele = allele

    def convert_allele_to_blood_type(self, allele):
        if allele == 'AA' or allele == 'AO':
            return 'A'
        elif allele == 'BB' or allele == 'BO':
            return 'B'
        elif allele == 'AB':
            return 'AB'
        elif allele == 'OO':
            return 'O'

class Child(Person):
    def __init__(self, father, mother):
        allele = self.inherit_alleles(father.allele, mother.allele)
        blood_type = self.convert_allele_to_blood_type(allele)
        super().__init__(blood_type)
        self.allele = allele

    def inherit_alleles(self, father_allele, mother_allele):
        child_allele = ""
        for f, m in zip(father_allele, mother_allele):
            # 50-50 chance of inheriting allele from father or mother
            child_allele += random.choice([f, m])
        return child_allele

    def convert_allele_to_blood_type(self, allele):
        if allele == 'AA' or allele == 'AO':
            return 'A'
        elif allele == 'BB' or allele == 'BO':
            return 'B'
        elif allele == 'AB':
            return 'AB'
        elif allele == 'OO':
            return 'O'

# Example usage:
father_allele = input("Enter the father's allele: ").upper()
mother_allele = input("Enter the mother's allele: ").upper()

father = Father(allele=father_allele)
mother = Mother(allele=mother_allele)
child = Child(father=father, mother=mother)

print(f"Child's allele: {child.allele}")
print(f"Child's blood type: {child.blood_type}")
