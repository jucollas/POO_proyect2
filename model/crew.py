from model.person import Person
import datetime

class Crew(Person):
    def __init__(self, cedula: str, name: str, surname: str, birthDate: datetime.date, genre: str, address: str, phoneNumber: str, email: str, jobPosition: str, dailyWorkingHours: int, yearsExperience: int):
        super().__init__(cedula, name, surname, birthDate, genre, address, phoneNumber, email)
        self._jobPosition = jobPosition
        self._dailyWorkingHours = dailyWorkingHours
        self._yearsExperience = yearsExperience

    def getJobPosition( self ) -> str :
        return self._jobPosition
    
    def getYearsExperience( self ) -> int :
        return self._yearsExperience
    
    def getDailyWorkingHours( self ) -> int:
        return self._dailyWorkingHours

    def setJobPosition( self, jobPosition: str ) -> None :
        self._jobPosition = jobPosition

    def setYearsExperience(self, yearsExperience : int) -> None:
        self._yearsExperience = yearsExperience

    def setDailyWorkingHours( self, dailyWorkingHours: int ) -> None :
        self._dailyWorkingHours = dailyWorkingHours

    def anotherYear( self ) -> None :
        self._yearsExperience += 1

    def __str__( self ) -> str:
        tmp = [super().__str__()]
        tmp.append(f" Position: {self._jobPosition}")
        return ". ".join( tmp )

if __name__ == "__main__":
    pas = Crew( "1110101", "oscar", "vargas", "hoy", "macho", "en tu casa", "0135462013", "hola@gmail.com", "jesucristo", 5, 3 );
    print( pas )