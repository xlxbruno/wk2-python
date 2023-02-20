class Person:
    name = "Hanks"
    age = "18"
    gender = "Male"

    def set(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get(self, name, age, gender):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))

    def info(self):
        print("Name: " + self.name + "Age: " + self.age + "Gender: " + self.gender)

    def voter_check(self):
        pass

person = Person()
person.info()
















class Voter(Person):

    voter = "Voter"

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def get(self, name, age, gender):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))

    def voter_check(self):
        age = self.age
        try:
            print(self.age + " ,can vote")
        except:
            print("An error occurred, check if a number was given")
        if age > 0 and age < 18:
            raise TypeError(self.age + " ,cannot vote")

    def print_info(self):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))


person = Voter()
person.set_name("Bruno")
person.set_age("22")
person.set_gender("Male")
person.print_info()
person.voter_check()
