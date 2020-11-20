
class Pet:

    # data common to ALL the pets
    default_owner = "scott"

    def __init__(self, owner="", name="", age=1):
        self._owner = None
        self._name = None
        self._age = 0
        self.owner = owner
        self.name = name
        self.age = age

    def summarize(self):
        summary = f"Name: {self._name}\n"
        summary += f"Age: {self._age}\n"
        summary += f"Owner: {self._owner}\n"
        return summary

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if new_owner is None:
            raise ValueError("All pets have owners")
        else:
            self._owner = new_owner

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 0 <= new_age <= 100:
            self._age = new_age
        else:
            raise ValueError("age must be between 0 and 100")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name is None:
            raise ValueError("All pets need a name")
        else:
            self._name = new_name

    # using a class method to implements a "factory pattern"

    @classmethod
    def create(cls, name, age):
        p = Pet(owner=cls.default_owner, name=name, age=age)
        return p

    @classmethod
    def change_owner(cls, new_owner):
        cls.default_owner = new_owner



    class Dog(Pet, Omnivore):
        pass



def main():
    # pr1 = Pet()
    # pr1.Owner = "..."
    # pr1.Name = ".."
    # pr1.Age = ".."
    # summary = pr1.Summarize()

    p1 = Pet(owner="rob", name="chewie", age=4)
    p2 = Pet(owner="Rickie", name="Grace")
    p3 = Pet.create("waldo", 2)

    print(p3.summarize())
    print(p2.summarize())

    p1.owner = "jessica"
    print("p1 owner", p1.owner)

    p1.age = 4
    print(p1.summarize())


if __name__ == "__main__":
    main()


# Problems with data
# data may have rules not expressed in data type
# data may have to changed in consort with other data
# data changes may have to be logged/recorded
# data changes may trigger other events
##
# Never expose any data directly
