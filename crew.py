from person import Person

class Crew(Person):
    def __init__(self, cedula: str, name: str, surname: str, birthDate: str, genre: str, address: str, phoneNumber: str, email: str, jobPosition: str, dailyWorkingHours: int, yearsExperience: int):
        super().__init__(cedula, name, surname, birthDate, genre, address, phoneNumber, email)
        self._jobPosition = jobPosition
        self._dailyWorkingHours = dailyWorkingHours
        self._yearsExperience = yearsExperience

    def setJobPosition( self, jobPosition: str ) -> None :
        self._jobPosition = jobPosition;

    def getJobPosition( self ) -> str :
        return self._jobPosition;

    def setDailyWorkingHours( self, dailyWorkingHours: int ) -> None :
        self._dailyWorkingHours = dailyWorkingHours;

    def anotherYear( self ) -> None :
        self._yearsExperience += 1;

    def getYearsExperience( self ) -> int :
        return self._yearsExperience;

    def __str__( self ) -> str:
        tmp = [super().__str__()]
        tmp.append(f" Position: {self._jobPosition}")
        return ". ".join( tmp );

if __name__ == "__main__":
    pas = Crew( "1110101", "oscar", "vargas", "hoy", "macho", "en tu casa", "0135462013", "hola@gmail.com", "jesucristo", 5, 3 );
    print( pas )