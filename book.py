from collections import UserDict
from record import Record
from datetime import datetime, date, timedelta


class AddressBook(UserDict):

    def add_record(self, record:Record) -> Record | None:
        self.data[record.name.value]=record
    
    def find(self, name: str) -> Record:
        return self.data.get(name)
    
    def delete(self, name) -> None:
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Запис {name} не знайдено")

    def get_upcoming_birthdays(self):
        today = date.today()
        upcoming = []
        for name, record in self.data.items():
            if not record.birthday is None:
                
                bday_this_year = datetime.strptime(record.birthday.value,"%d.%m.%Y").replace(year=today.year).date()
                if bday_this_year<today:
                    bday_this_year = datetime.strptime(record.birthday.value,"%d.%m.%Y").replace(year=today.year+1).date()
                next_week = today + timedelta(days = 7)
                if bday_this_year.weekday() >= 5:
                    bday_this_year = bday_this_year + timedelta(7-bday_this_year.weekday())
                    
                if today <= bday_this_year <= next_week:
                   upcoming.append({"name": name, "birthday_date": bday_this_year.strftime("%d.%m.%Y")})
                
            
        return upcoming
     
    def __str__(self) ->str:
        result=''
        for name, record in self.data.items():
            result+=str(record)+'\n'
        return result.strip()

    



