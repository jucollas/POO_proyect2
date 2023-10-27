from person import Person

class Crew(Person):
    def __init__(self, cedula: str, name: str, surname: str, birthDate: str, genre: str, address: str, phoneNumber: str, email: str, jobPosition: str, dailyWorkingHours: int, yearsExperience: int):
        super().__init__(cedula, name, surname, birthDate, genre, address, phoneNumber, email)
        self.jobPosition = jobPosition
        self.dailyWorkingHours = dailyWorkingHours
        self.yearsExperience = yearsExperience

    def info(self):
        print(super().info())
        print(f".Position: {self.jobPosition}")